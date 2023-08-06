import numpy as np

from astropy_healpix import HEALPix
from astropy.coordinates import ICRS

from astropy.wcs.utils import skycoord_to_pixel

from matplotlib.path import Path
from matplotlib.patches import PathPatch

#This method is multiprocessed using the concurrent.futures python package.
def compute_healpix_vertices(x):
    path_vertices = np.array([])
    codes = np.array([])

    order_str = x[0]
    ipixels = x[1]
    wcs = x[2]

    order = int(order_str)

    hp = HEALPix(nside=(1 << order), order='nested', frame=ICRS())
    step = 1
    if order < 3:
        step = 2

    ipix_boundaries = hp.boundaries_skycoord(ipixels, step=step)
    # Projection on the given WCS
    xp, yp = skycoord_to_pixel(ipix_boundaries, wcs=wcs)

    if order < 3:
        c1 = np.vstack((xp[:, 0], yp[:, 0])).T
        c2 = np.vstack((xp[:, 1], yp[:, 1])).T
        c3 = np.vstack((xp[:, 2], yp[:, 2])).T
        c4 = np.vstack((xp[:, 3], yp[:, 3])).T

        c5 = np.vstack((xp[:, 4], yp[:, 4])).T
        c6 = np.vstack((xp[:, 5], yp[:, 5])).T
        c7 = np.vstack((xp[:, 6], yp[:, 6])).T
        c8 = np.vstack((xp[:, 7], yp[:, 7])).T

        cells = np.hstack((c1, c2, c3, c4, c5, c6, c7, c8, np.zeros((c1.shape[0], 2))))

        path_vertices = cells.reshape((9*c1.shape[0], 2))
        single_code = np.array([Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.CLOSEPOLY])
    else:
        c1 = np.vstack((xp[:, 0], yp[:, 0])).T
        c2 = np.vstack((xp[:, 1], yp[:, 1])).T
        c3 = np.vstack((xp[:, 2], yp[:, 2])).T
        c4 = np.vstack((xp[:, 3], yp[:, 3])).T

        cells = np.hstack((c1, c2, c3, c4, np.zeros((c1.shape[0], 2))))

        path_vertices = cells.reshape((5*c1.shape[0], 2))
        single_code = np.array([Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.CLOSEPOLY])
    

    codes = np.tile(single_code, c1.shape[0])

    return path_vertices, codes

def fill(moc, ax, wcs, **kw_mpl_pathpatch):
    from . import culling_backfacing_cells
    from ...parallel_task import send_to_multiple_processes
    
    depth_ipix_d = moc.serialize(format="json")
    depth_ipix_clean_d = culling_backfacing_cells.from_moc(depth_ipix_d=depth_ipix_d, wcs=wcs)

    # Send a (depth, hash, wcs) tuple to compute_healpix_vertices
    args = [depth_ipix + (wcs,) for depth_ipix in depth_ipix_clean_d.items()]

    # Use multiprocessing for computing the healpix vertices of the cells
    # cleaned from those backfacing the viewport.
    res = send_to_multiple_processes(func=compute_healpix_vertices, args=args, workers=4)
    
    path_vertices = np.array(res[0][0])
    codes = np.array(res[0][1])

    for p, c in res[1:]:
        path_vertices = np.vstack((path_vertices, p))
        codes = np.hstack((codes, c))

    # Cast to a numpy array
    path = Path(path_vertices, codes)
    patch = PathPatch(path, **kw_mpl_pathpatch)

    # Add the patch to the mpl axis
    ax.add_patch(patch)

    from . import axis_viewport
    axis_viewport.set(ax, wcs)
