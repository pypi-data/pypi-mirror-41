# -*- coding: utf-8 -*-

"""Functions directly related to atmospheric sciences.
"""
import numpy as np
from scipy.interpolate import interp1d

from . import constants
from . import math
from .physics import thermodynamics

from typhon.utils import deprecated


__all__ = [
    'iwv',
    'moist_lapse_rate',
    'relative_humidity',
    'vmr',
    'standard_atmosphere',
]


@deprecated(new_name='typhon.physics.integrate_water_vapor')
def iwv(vmr, p, T, z, axis=0):
    """Calculate the integrated water vapor (IWV).

    Parameters:
        vmr (float or ndarray): Volume mixing ratio,
        p (float or ndarray): Pressue [Pa].
        T (float or ndarray): Temperature [K].
        z (ndarray): Height [m]. Size must match vmr.
        axis (int): Axis to intergrate along.

    Returns:
        float: Integrated water vapor [kg/m**2].
    """
    R_v = constants.gas_constant_water_vapor
    rho = thermodynamics.density(p, T, R=R_v)  # Water vapor density.

    return math.integrate_column(vmr * rho, z, axis=axis)


@deprecated(new_name='typhon.physics.moist_lapse_rate')
def moist_lapse_rate(p, T, e_eq=None):
    r"""Calculate the moist-adiabatic temperature lapse rate.

    Bohren and Albrecht (Equation 6.111, note the **sign change**):

    .. math::
        \frac{dT}{dz} =
            \frac{g}{c_p} \frac{1 + l_v w_s / RT}{1 + l_v^2 w_s/c_p R_v T^2}

    Parameters:
        p (float or ndarray): Pressure [Pa].
        T (float or ndarray): Temperature [K].
        e_eq (callable): Function object which is used to calculate the
            equilibrium water vapor pressure in Pa. The function must implement
            the signature ``e_eq = f(T)`` where ``T`` is temperature in Kelvin.
            If ``None`` the function :func:`typhon.physics.e_eq_water_mk` is
            used.

    Returns:
        float or ndarray: Moist-adiabatic lapse rate [K/m].

    Examples:
        >>> moist_lapse_rate(1013.25e2, 288.15)
        0.004728194612232855

    References:
        Bohren C. and Albrecht B., Atmospheric Thermodynamics, p. 287-92
    """
    if e_eq is None:
        e_eq = thermodynamics.e_eq_water_mk

    # Use short formula symbols for physical constants.
    g = constants.earth_standard_gravity
    Lv = constants.heat_of_vaporization
    Rd = constants.gas_constant_dry_air
    Rv = constants.gas_constant_water_vapor
    Cp = constants.isobaric_mass_heat_capacity

    gamma_d = g / Cp  # dry lapse rate
    w_saturated = thermodynamics.vmr2mixing_ratio(e_eq(T) / p)

    lapse = (
        gamma_d * (
            (1 + (Lv * w_saturated) / (Rd * T)) /
            (1 + (Lv**2 * w_saturated) / (Cp * Rv * T**2))
        )
    )

    return lapse


@deprecated(new_name='typhon.physics.vmr2relative_humidity')
def relative_humidity(vmr, p, T):
    r"""Calculate relative humidity (RH).

    .. math::
        RH = \frac{VMR \cdot p}{e_s(T)}

    Parameters:
        vmr (float or ndarray): Volume mixing ratio,
        p (float or ndarray): Pressure [Pa].
        T (float or ndarray): Temperature [K].

    Returns:
        float or ndarray: Relative humiditity [unitless].

    See also:
        :func:`~typhon.atmosphere.vmr`
            Complement function (returns VMR for given RH).
        :func:`~typhon.physics.e_eq_water_mk`
            Used to calculate the equilibrium water vapor pressure.

    Examples:
        >>> relative_humidity(0.025, 1013e2, 300)
        0.71604995533615401
    """
    return vmr * p / thermodynamics.e_eq_water_mk(T)


@deprecated(new_name='typhon.physics.relative_humidity2vmr')
def vmr(RH, p, T):
    r"""Calculate the volume mixing ratio (VMR).

    .. math::
        VMR = \frac{RH \cdot e_s(T)}{p}

    Parameters:
        RH (float or ndarray): Relative humidity.
        p (float or ndarray): Pressue [Pa].
        T (float or ndarray): Temperature [K].

    Returns:
        float or ndarray: Volume mixing ratio [unitless].

    See also:
        :func:`~typhon.atmosphere.relative_humidity`
            Complement function (returns RH for given VMR).
        :func:`~typhon.physics.e_eq_water_mk`
            Used to calculate the equilibrium water vapor pressure.

    Examples:
        >>> vmr(0.75, 101300, 300)
        0.026185323887350429
    """
    return RH * thermodynamics.e_eq_water_mk(T) / p


@deprecated(new_name='typhon.physics.standard_atmosphere')
def standard_atmosphere(z, fill_value='extrapolate'):
    """International Standard Atmosphere (ISA) as a function of height.

    Parameters:
        z (float or ndarray): Geopotential height above MSL [m].
        fill_value (str): See :func:`~scipy.interpolate.interp1d` for
            available options.

    Returns:
        ndarray: Atmospheric temperature [K].

    Examples:

    .. plot::
        :include-source:

        import numpy as np
        from typhon.plots import profile_z
        from typhon.atmosphere import standard_atmosphere


        z = np.linspace(0, 80_000, 100)
        T = standard_atmosphere(z)

        fig, ax = plt.subplots()
        profile_z(z, T)

        plt.show()

    """
    h = np.array([-610, 11000, 20000, 32000, 47000, 51000, 71000, 84852])
    temp = np.array([+19.0, -56.5, -56.5, -44.5, -2.5, -2.5, -58.5, -86.28])

    return interp1d(h, temp + constants.K, fill_value=fill_value)(z)
