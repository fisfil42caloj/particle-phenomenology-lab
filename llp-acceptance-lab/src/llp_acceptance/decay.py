"""Spatial decay probabilities for a one-dimensional LLP toy model."""

from __future__ import annotations

from typing import TypeAlias

import numpy as np
import numpy.typing as npt

FloatArray: TypeAlias = npt.NDArray[np.float64]
FloatLike: TypeAlias = float | FloatArray


def survival_probability(L: FloatLike, L_lab: FloatLike) -> FloatLike:
    """Return ``S(L) = exp(-L / L_lab)``.

    Parameters
    ----------
    L:
        Path length in meters.
    L_lab:
        Mean lab-frame decay length in meters. It must be strictly positive.
    """

    distance = _as_array(L)
    lab_length = _as_array(L_lab)
    _validate_non_negative(distance, "L")
    _validate_positive(lab_length, "L_lab")
    survival = np.exp(-distance / lab_length)
    return _return_scalar_if_scalar(L, L_lab, survival)


def decay_probability_before(L: FloatLike, L_lab: FloatLike) -> FloatLike:
    """Return the probability to decay before path length ``L``."""

    distance = _as_array(L)
    lab_length = _as_array(L_lab)
    _validate_non_negative(distance, "L")
    _validate_positive(lab_length, "L_lab")
    probability = -np.expm1(-distance / lab_length)
    return _return_scalar_if_scalar(L, L_lab, probability)


def decay_probability_between(L1: float, L2: float, L_lab: FloatLike) -> FloatLike:
    """Return the probability to decay between ``L1`` and ``L2``.

    ``L1`` and ``L2`` are path lengths in meters. ``L2`` may be ``np.inf``, in
    which case the result is the survival probability beyond ``L1``.

    The finite-interval calculation uses ``expm1`` to avoid loss of precision
    when ``L2 - L1`` is very small.
    """

    _validate_interval(L1, L2)
    lab_length = _as_array(L_lab)
    _validate_positive(lab_length, "L_lab")

    exp_l1 = np.exp(-L1 / lab_length)
    if np.isinf(L2):
        probability = exp_l1
    else:
        interval_width = L2 - L1
        probability = exp_l1 * (-np.expm1(-interval_width / lab_length))

    return _return_scalar_if_scalar(L1, L_lab, probability)


def decay_pdf(L: FloatLike, L_lab: FloatLike) -> FloatLike:
    """Return the spatial decay density ``f(L) = exp(-L/L_lab) / L_lab``."""

    distance = _as_array(L)
    lab_length = _as_array(L_lab)
    _validate_non_negative(distance, "L")
    _validate_positive(lab_length, "L_lab")
    pdf = np.exp(-distance / lab_length) / lab_length
    return _return_scalar_if_scalar(L, L_lab, pdf)


def _as_array(value: FloatLike) -> FloatArray:
    return np.asarray(value, dtype=float)


def _return_scalar_if_scalar(
    first_original: object,
    second_original: object,
    value: FloatArray,
) -> FloatLike:
    scalar_input = np.isscalar(first_original) and np.isscalar(second_original)
    return float(value) if scalar_input else value


def _validate_non_negative(value: FloatArray, name: str) -> None:
    _validate_finite(value, name)
    if np.any(value < 0.0):
        raise ValueError(f"{name} must be non-negative.")


def _validate_positive(value: FloatArray, name: str) -> None:
    _validate_finite(value, name)
    if np.any(value <= 0.0):
        raise ValueError(f"{name} must be strictly positive.")


def _validate_interval(L1: float, L2: float) -> None:
    if not np.isfinite(L1):
        raise ValueError("L1 must be finite.")
    if L1 < 0.0:
        raise ValueError("L1 must be non-negative.")
    if not (np.isfinite(L2) or np.isposinf(L2)):
        raise ValueError("L2 must be finite or equal to positive infinity.")
    if not (L2 > L1 or np.isposinf(L2)):
        raise ValueError(
            "L2 must be greater than L1, or equal to positive infinity."
        )


def _validate_finite(value: FloatArray, name: str) -> None:
    if np.any(~np.isfinite(value)):
        raise ValueError(f"{name} must be finite.")
