# LLP Acceptance Lab

Small scientific Python project for studying toy acceptances of long-lived
particles (LLPs). The current implementation covers relativistic kinematics,
the probability for an LLP to decay between two distances along its trajectory,
and toy one-dimensional detector regions.

This is a deliberately idealized phenomenology exercise. It is not a simulation
of ATLAS, CMS, FASER, or any real detector.

## Install

```bash
python -m pip install -e .
python -m pip install -r requirements.txt
```

## Minimal Example

```python
from llp_acceptance.decay import decay_probability_between
from llp_acceptance.kinematics import lab_decay_length

ctau = 1.0       # m
betagamma = 10.0
L_lab = lab_decay_length(ctau, betagamma)

P = decay_probability_between(1.0, 4.0, L_lab)
print(P)
```

Toy detector regions can be used directly:

```python
from llp_acceptance.geometry import CALORIMETER_TOY, probability_in_region
from llp_acceptance.kinematics import lab_decay_length

L_lab = lab_decay_length(ctau=1.0, betagamma=10.0)
P_calorimeter = probability_in_region(CALORIMETER_TOY, L_lab)
print(P_calorimeter)
```

## Physics Implemented So Far

For a particle with proper decay length `ctau` in meters and boost
`beta*gamma`, the mean decay length in the lab frame is

```text
L_lab = beta * gamma * ctau .
```

The probability to decay between two path lengths `L1` and `L2` is

```text
P(L1 < L < L2) = exp(-L1 / L_lab) - exp(-L2 / L_lab).
```

The code assumes natural units for masses and energies, with masses and
energies expressed in GeV. Distances are expressed in meters, and `ctau` is
entered directly in meters.

For an idealized 1D detector region,

```text
Region1D(name, L_min, L_max)
```

the region probability is computed from the same exponential law:

```text
P_region = exp(-L_min / L_lab) - exp(-L_max / L_lab).
```

## Repository Layout

```text
llp-acceptance-lab/
  README.md
  pyproject.toml
  requirements.txt
  src/llp_acceptance/
  notebooks/
  tests/
  reports/
  figures/
  examples/
```

## Notebooks

- `01_decay_probability_1d.ipynb`: derives the 1D exponential decay law and
  plots `P(ctau)`, survival probabilities, decay PDFs, and toy-region
  comparisons.
- `02_boost_distributions.ipynb`: placeholder for boost distributions.
- `03_toy_detector_geometry.ipynb`: placeholder for toy detector geometry.
- `04_alp_like_lifetime_toy.ipynb`: placeholder for an ALP-like lifetime toy
  model.

## Limitations

- Detector regions are idealized one-dimensional toy intervals.
- No real detector dimensions or experimental efficiencies are used.
- No production model, branching ratio, or detector response is included.
- The current model studies only exponential decay along an idealized path.
