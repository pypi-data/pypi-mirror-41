""" transforms involving ECI earth-centered inertial """

from datetime import datetime
import numpy as np
from .sidereal import datetime2sidereal
try:
    from astropy.time import Time
except ImportError:
    Time = None


def eci2ecef(eci: np.ndarray,
             time: datetime,
             useastropy: bool = True) -> np.ndarray:
    """
     Observer => Point

    input
    -----
    eci [meters] Nx3 target ECI location (x,y,z)                    [0,Infinity)
    t  time (datetime.datetime)   time of obsevation (UTC)

    output
    ------
    x,y,z  [meters] target ECEF location                             [0,Infinity)
    """
    useastropy = useastropy and Time

    if useastropy:
        gst = Time(time).sidereal_time('apparent', 'greenwich').radian
    else:
        gst = datetime2sidereal(time, 0.)

    gst = np.atleast_1d(gst)
    assert gst.ndim == 1 and isinstance(gst[0], float)  # must be in radians!

    eci = np.atleast_2d(eci)
    assert eci.shape[0] == gst.size, 'length of time does not match number of ECI positions'

    N, trip = eci.shape
    if eci.ndim > 2 or trip != 3:
        raise ValueError('eci triplets must be shape (N,3)')

    ecef = np.empty_like(eci)

    for i in range(N):
        ecef[i, :] = _rottrip(gst[i]) @ eci[i, :]

    return ecef.squeeze()


def ecef2eci(ecef: np.ndarray,
             time: datetime,
             useastropy: bool = True) -> np.ndarray:
    """
    Point => Point

    input
    -----
    ecef:  Nx3  x,y,z  (meters)
    time:  datetime.datetime


    output
    ------
    eci  x,y,z (meters)
    """
    useastropy = useastropy and Time

    if useastropy:
        gst = Time(time).sidereal_time('apparent', 'greenwich').radian
    else:
        gst = datetime2sidereal(time, 0.)

    gst = np.atleast_1d(gst)
    assert gst.ndim == 1 and isinstance(gst[0], float)  # must be in radians!

    ecef = np.atleast_2d(ecef)
    assert ecef.shape[0] == gst.size, 'length of time does not match number of ECEF positions'

    N, trip = ecef.shape
    if ecef.ndim > 2 or trip != 3:
        raise ValueError('ecef triplets must be shape (N,3)')

    eci = np.empty_like(ecef)
    for i in range(N):
        eci[i, :] = _rottrip(gst[i]).T @ ecef[i, :]  # this one is transposed

    return eci.squeeze()


def _rottrip(ang: np.ndarray) -> np.ndarray:
    ang = ang.squeeze()
    if ang.size > 1:
        raise ValueError('only one angle allowed at a time')
    """ported from:
    https://github.com/dinkelk/astrodynamics/blob/master/rot3.m
    """
    return np.array([[np.cos(ang), np.sin(ang), 0],
                     [-np.sin(ang), np.cos(ang), 0],
                     [0, 0, 1]])
