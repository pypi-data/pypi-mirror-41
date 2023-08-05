""" transforms involving ENU East North Up """
from typing import Tuple
from numpy import radians, sin, cos, hypot, arctan2, degrees
import numpy as np
try:
    from math import tau
except ImportError:
    tau = 2 * np.pi

from .ecef import geodetic2ecef, ecef2geodetic, enu2ecef, uvw2enu


__all__ = ['enu2aer', 'aer2enu', 'enu2geodetic', 'geodetic2enu']


def enu2aer(e: np.ndarray, n: np.ndarray, u: np.ndarray, deg: bool = True) -> Tuple[float, float, float]:
    """
    ENU to Azimuth, Elevation, Range

    ## Inputs

    * e,n,u  [meters]  East, north, up                                [0,Infinity)
    * deg    degrees input/output  (False: radians in/out)

    ## Outputs

    * azimuth, elevation (degrees/radians)                             [0,360),[0,90]
    * slant range [meters]                                             [0,Infinity)
    """
    # 1 millimeter precision for singularity

    e = np.atleast_1d(e)
    n = np.atleast_1d(n)
    u = np.atleast_1d(u)

    with np.errstate(invalid='ignore'):
        e[abs(e) < 1e-3] = 0.
        n[abs(n) < 1e-3] = 0.
        u[abs(u) < 1e-3] = 0.

    r = hypot(e, n)
    slantRange = hypot(r, u)
    elev = arctan2(u, r)
    az = arctan2(e, n) % tau

    if deg:
        az = degrees(az)
        elev = degrees(elev)

    return az[()].squeeze(), elev[()].squeeze(), slantRange[()].squeeze()


def aer2enu(az: float, el: float, srange: float, deg: bool = True) -> Tuple[float, float, float]:
    """
    input:
    ------
    azimuth, elevation (degrees/radians)                             [0,360),[0,90]
    slant range [meters]                                             [0,Infinity)
    deg    degrees input/output  (False: radians in/out)

    output:
    -------
    e,n,u   East, North, Up [m]

    """
    if deg:
        el = radians(el)
        az = radians(az)

    with np.errstate(invalid='ignore'):
        if (np.asarray(srange) < 0).any():
            raise ValueError('Slant range  [0, Infinity)')

    r = srange * cos(el)

    return r * sin(az), r * cos(az), srange * sin(el)


def enu2geodetic(e: float, n: float, u: float,
                 lat0: float, lon0: float, h0: float,
                 ell=None, deg: bool = True) -> Tuple[float, float, float]:
    """

    input
    -----
    e,n,u   East, North, Up [m]
    Observer: lat0, lon0, h0 (altitude, meters)
    ell    reference ellipsoid
    deg    degrees input/output  (False: radians in/out)


    output:
    -------
    target: lat,lon, h  (degrees/radians,degrees/radians, meters)

    """

    x, y, z = enu2ecef(e, n, u, lat0, lon0, h0, ell, deg=deg)

    return ecef2geodetic(x, y, z, ell, deg=deg)


def geodetic2enu(lat: float, lon: float, h: float,
                 lat0: float, lon0: float, h0: float,
                 ell=None, deg: bool = True) -> Tuple[float, float, float]:
    """
    input
    -----
    target: lat,lon, h
    Observer: lat0, lon0, h0 (altitude, meters)
    ell    reference ellipsoid
    deg    degrees input/output  (False: radians in/out)


    output:
    -------
    e,n,u   East, North, Up [m]
    """
    x1, y1, z1 = geodetic2ecef(lat, lon, h, ell, deg=deg)
    x2, y2, z2 = geodetic2ecef(lat0, lon0, h0, ell, deg=deg)
    dx = x1 - x2
    dy = y1 - y2
    dz = z1 - z2

    return uvw2enu(dx, dy, dz, lat0, lon0, deg=deg)
