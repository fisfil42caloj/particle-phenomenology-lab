# LLP Acceptance Lab

Small scientific Python project for studying toy acceptances of long-lived
particles (LLPs). The first implementation covers relativistic kinematics and
the probability for an LLP to decay between two distances along its trajectory.

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

## Limitations

- Detector regions are not yet implemented in this phase.
- No real detector dimensions or experimental efficiencies are used.
- No production model, branching ratio, or detector response is included.
- The current model studies only exponential decay along an idealized path.
