"""Plotting utilities for LLP acceptance studies."""

from __future__ import annotations

from collections.abc import Sequence
from pathlib import Path
from typing import TypeAlias

import matplotlib.pyplot as plt
import numpy as np
import numpy.typing as npt

from .decay import decay_pdf, survival_probability
from .geometry import Region1D, probability_in_region
from .kinematics import lab_decay_length

FloatArray: TypeAlias = npt.NDArray[np.float64]


def plot_probability_vs_ctau(
    regions: Sequence[Region1D],
    ctau_values: npt.ArrayLike,
    betagamma: float,
    output_path: str | Path | None = None,
    ax: object | None = None,
) -> tuple[object, object]:
    """Plot ``P_region(ctau)`` for several toy detector regions.

    ``ctau_values`` are proper decay lengths in meters. The boost
    ``beta*gamma`` is held fixed, so each point uses
    ``L_lab = beta*gamma*ctau``. The resulting curves show the basic LLP
    phenomenology: each region is most sensitive when the boosted decay length
    is comparable to its distance scale.
    """

    ctau = _positive_array(ctau_values, "ctau_values")
    _validate_positive_scalar(betagamma, "betagamma")
    if not regions:
        raise ValueError("At least one region is required.")

    axis = ax if ax is not None else plt.subplots()[1]
    figure = axis.figure

    L_lab = lab_decay_length(ctau, betagamma)
    for region in regions:
        probability = probability_in_region(region, L_lab)
        axis.plot(ctau, probability, label=region.name)

    axis.set_xscale("log")
    axis.set_xlabel("ctau [m]")
    axis.set_ylabel("probability")
    axis.set_ylim(0.0, 1.0)
    axis.set_title(f"Toy LLP decay probability, beta gamma = {betagamma:g}")
    axis.grid(True, which="both", alpha=0.3)
    axis.legend()

    _save_if_requested(figure, output_path)
    return figure, axis


def plot_survival_probability(
    L_values: npt.ArrayLike,
    L_lab: float,
    output_path: str | Path | None = None,
    ax: object | None = None,
) -> tuple[object, object]:
    """Plot the survival probability ``S(L) = exp(-L/L_lab)``."""

    L = _non_negative_array(L_values, "L_values")
    _validate_positive_scalar(L_lab, "L_lab")
    axis = ax if ax is not None else plt.subplots()[1]
    figure = axis.figure

    axis.plot(L, survival_probability(L, L_lab))
    axis.set_xlabel("L [m]")
    axis.set_ylabel("survival probability")
    axis.set_title(f"Survival probability, L_lab = {L_lab:g} m")
    axis.grid(True, alpha=0.3)

    _save_if_requested(figure, output_path)
    return figure, axis


def plot_decay_pdf(
    L_values: npt.ArrayLike,
    L_lab: float,
    output_path: str | Path | None = None,
    ax: object | None = None,
) -> tuple[object, object]:
    """Plot the spatial decay density ``f(L) = exp(-L/L_lab)/L_lab``."""

    L = _non_negative_array(L_values, "L_values")
    _validate_positive_scalar(L_lab, "L_lab")
    axis = ax if ax is not None else plt.subplots()[1]
    figure = axis.figure

    axis.plot(L, decay_pdf(L, L_lab))
    axis.set_xlabel("L [m]")
    axis.set_ylabel("decay PDF [1/m]")
    axis.set_title(f"Spatial decay PDF, L_lab = {L_lab:g} m")
    axis.grid(True, alpha=0.3)

    _save_if_requested(figure, output_path)
    return figure, axis


def _save_if_requested(figure: object, output_path: str | Path | None) -> None:
    if output_path is None:
        return
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    figure.savefig(path, bbox_inches="tight", dpi=150)


def _positive_array(values: npt.ArrayLike, name: str) -> FloatArray:
    array = np.asarray(values, dtype=float)
    if np.any(~np.isfinite(array)) or np.any(array <= 0.0):
        raise ValueError(f"{name} must contain only positive finite values.")
    return array


def _non_negative_array(values: npt.ArrayLike, name: str) -> FloatArray:
    array = np.asarray(values, dtype=float)
    if np.any(~np.isfinite(array)) or np.any(array < 0.0):
        raise ValueError(f"{name} must contain only non-negative finite values.")
    return array


def _validate_positive_scalar(value: float, name: str) -> None:
    if not np.isfinite(value) or value <= 0.0:
        raise ValueError(f"{name} must be positive and finite.")
