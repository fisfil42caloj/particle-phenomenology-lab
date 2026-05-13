"""Relativistic kinematics for long-lived-particle toy studies.

Masses and energies are expressed in GeV. Distances are expressed in meters.
The proper decay length ``ctau`` is passed directly in meters, so no conversion
from seconds is performed here.
"""

from __future__ import annotations

from typing import TypeAlias

import numpy as np
import numpy.typing as npt

FloatArray: TypeAlias = npt.NDArray[np.float64]
FloatLike: TypeAlias = float | FloatArray


def gamma_from_energy(E: FloatLike, m: float) -> FloatLike:
    """Return the Lorentz factor ``gamma = E / m``.

    Parameters
    ----------
    E:
        Total energy in GeV.
    m:
        Particle mass in GeV.

    Raises
    ------
    ValueError
        If ``m <= 0`` or if any energy value satisfies ``E < m``.
    """

    _validate_mass(m)
    energy = _as_array(E)
    _validate_energy_at_least_mass(energy, m)
    return _return_scalar_if_scalar(E, energy / m)


def momentum_from_energy(E: FloatLike, m: float) -> FloatLike:
    """Return the momentum magnitude ``p = sqrt(E^2 - m^2)`` in GeV."""

    _validate_mass(m)
    energy = _as_array(E)
    _validate_energy_at_least_mass(energy, m)
    momentum_squared = np.maximum(energy**2 - m**2, 0.0)
    return _return_scalar_if_scalar(E, np.sqrt(momentum_squared))


def beta_from_energy(E: FloatLike, m: float) -> FloatLike:
    """Return ``beta = v / c`` for a particle with total energy ``E``."""

    energy = _as_array(E)
    momentum = _as_array(momentum_from_energy(energy, m))
    beta = momentum / energy
    return _return_scalar_if_scalar(E, beta)


def betagamma_from_energy(E: FloatLike, m: float) -> FloatLike:
    """Return ``beta * gamma = p / m`` from total energy and mass."""

    momentum = _as_array(momentum_from_energy(E, m))
    betagamma = momentum / m
    return _return_scalar_if_scalar(E, betagamma)


def betagamma_from_momentum(p: FloatLike, m: float) -> FloatLike:
    """Return ``beta * gamma = p / m`` from momentum and mass."""

    _validate_mass(m)
    momentum = _as_array(p)
    _validate_finite(momentum, "p")
    if np.any(momentum < 0.0):
        raise ValueError("Momentum magnitude p must be non-negative.")
    return _return_scalar_if_scalar(p, momentum / m)


def lab_decay_length(ctau: FloatLike, betagamma: FloatLike) -> FloatLike:
    """Return the mean lab-frame decay length ``L_lab = beta*gamma*ctau``.

    The input ``ctau`` must be expressed in meters. The boost ``beta*gamma`` is
    dimensionless. The returned decay length is in meters.
    """

    ctau_array = _as_array(ctau)
    betagamma_array = _as_array(betagamma)
    _validate_finite(ctau_array, "ctau")
    _validate_finite(betagamma_array, "beta*gamma")
    if np.any(ctau_array < 0.0):
        raise ValueError("The proper decay length ctau must be non-negative.")
    if np.any(betagamma_array < 0.0):
        raise ValueError("The boost beta*gamma must be non-negative.")

    length = ctau_array * betagamma_array
    scalar_input = np.isscalar(ctau) and np.isscalar(betagamma)
    return float(length) if scalar_input else length


def _as_array(value: FloatLike) -> FloatArray:
    return np.asarray(value, dtype=float)


def _return_scalar_if_scalar(original: FloatLike, value: FloatArray) -> FloatLike:
    return float(value) if np.isscalar(original) else value


def _validate_mass(m: float) -> None:
    if not np.isfinite(m) or m <= 0.0:
        raise ValueError("Particle mass m must be positive.")


def _validate_energy_at_least_mass(E: FloatArray, m: float) -> None:
    _validate_finite(E, "E")
    if np.any(E < m):
        raise ValueError(
            "Total energy E must satisfy E >= m in natural units; "
            "a particle cannot have total energy below its rest mass."
        )


def _validate_finite(value: FloatArray, name: str) -> None:
    if np.any(~np.isfinite(value)):
        raise ValueError(f"{name} must be finite.")
