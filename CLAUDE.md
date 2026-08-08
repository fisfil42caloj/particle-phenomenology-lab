# CLAUDE.md

Guidance for AI assistants working in this repository.

## What this repository is

`particle-phenomenology-lab` is an **academic portfolio** of small, self-contained
particle-phenomenology projects written in Python. It is not a framework and not a
monorepo of interdependent libraries: each subdirectory is one standalone project with
its own packaging, tests and documentation.

Currently there is exactly one project:

- `llp-acceptance-lab/` — toy acceptance calculations for long-lived particles (LLPs):
  relativistic kinematics, one-dimensional exponential decay probabilities, idealized
  1D detector regions, plotting helpers, notebooks and a LaTeX report scaffold.

The root `README.md` is the index of projects. When a new project is added, it gets its
own top-level directory *and* an entry in that index.

## The scope rule (read this before writing physics)

This is the single most important convention in the repository, and it is stated in both
READMEs:

> These projects are educational phenomenology tools. They do not use real experimental
> efficiencies, do not quote exclusions, and do not claim to simulate ATLAS, CMS, FASER,
> or any other detector.

Consequences for any change you make:

- Do not introduce real detector geometries, real efficiencies, published limits, or
  numbers presented as experimental results.
- Toy quantities are named as such. The existing regions are `inner_tracker_toy`,
  `calorimeter_toy`, `muon_system_toy`, `far_detector_toy` — keep the `_toy` suffix for
  any new region.
- Keep the "Limitations" section of `llp-acceptance-lab/README.md` truthful. If a change
  removes a limitation, remove the bullet; if it adds one, add a bullet.
- Physics that is deliberately not implemented yet (production models, branching ratios,
  detector response, boost distributions) should stay unimplemented rather than be
  faked.

## Layout

```text
particle-phenomenology-lab/
  README.md                      index of projects
  llp-acceptance-lab/
    README.md                    physics, install, usage, limitations
    pyproject.toml               setuptools; src layout; pytest config
    requirements.txt             numpy, matplotlib, pytest
    src/llp_acceptance/
      __init__.py                re-exports the kinematics API only
      constants.py               c and hbar*c
      kinematics.py              gamma, p, beta, beta*gamma, L_lab
      decay.py                   survival, decay-before/between, spatial PDF
      geometry.py                Region1D dataclass + toy region constants
      plotting.py                matplotlib helpers, optional file output
      distributions.py           placeholder (docstring only)
    tests/                       pytest, one module per source module
    notebooks/                   01 is a real study; 02-04 are placeholders
    examples/quickstart.py       smallest end-to-end example
    reports/                     LaTeX report scaffold + references.bib
    figures/                     generated output (.gitkeep only)
```

## Development workflow

All commands are run from inside `llp-acceptance-lab/`, not from the repository root.

```bash
cd llp-acceptance-lab
python -m pip install -e .
python -m pip install -r requirements.txt

python -m pytest                  # 23 tests, runs in well under a second
python -m pytest tests/test_decay.py -q
python examples/quickstart.py     # end-to-end smoke check
```

`pyproject.toml` sets `testpaths = ["tests"]` and `pythonpath = ["src"]`, so pytest finds
the package without an editable install; the editable install is still the recommended
way to work in notebooks.

There is no linter, formatter, type-checker or CI configured. The `.gitignore` reserves
cache directories for `mypy` and `ruff`, but neither is set up — do not assume a
formatter will clean up after you, and do not add tooling config unless asked.

## Code conventions

These are consistent across every module; follow them rather than your own defaults.

**Units.** Masses and energies in GeV, distances in meters, `ctau` passed directly in
meters (never seconds — no conversion happens anywhere in the code). State the units in
the docstring of any new public function.

**Scalar-in / scalar-out.** Public functions accept a float or a NumPy array and return
the same kind. The pattern is: convert with a private `_as_array`, compute on arrays,
then return through a private `_return_scalar_if_scalar` helper that checks
`np.isscalar` on the original input(s). Each module defines its own copy of these
private helpers and of the `FloatArray` / `FloatLike` type aliases — that duplication is
intentional and keeps the modules independent; do not refactor it into a shared utility
module without being asked.

**Validation up front, with physical error messages.** Every public function validates
its inputs before computing and raises `ValueError` with a message that explains the
physics, not just the constraint. The canonical example is in `kinematics.py`:

```text
Total energy E must satisfy E >= m in natural units;
a particle cannot have total energy below its rest mass.
```

Validation lives in private `_validate_*` helpers at the bottom of the module.

**Numerical care.** Use `expm1` / `log1p` where catastrophic cancellation is possible.
`decay_probability_between` already does this so that very narrow intervals stay
accurate; there is a regression test for it
(`test_close_interval_is_numerically_stable`). Preserve this when touching decay math.

**Style.** `from __future__ import annotations` at the top of every module, full type
hints on public functions, NumPy-style docstrings on the public API, `@dataclass(frozen=True)`
for value objects with validation in `__post_init__`. Module docstrings say what the
module is *and* restate the toy/idealized nature where relevant.

**`__init__.py`** currently re-exports only the kinematics API, with an explicit
`__all__`. Decay, geometry and plotting are imported from their submodules. Keep
`__all__` in sync if you add to the re-exported set.

**Plotting.** Helpers in `plotting.py` accept an optional `ax` and an optional
`output_path`, always return `(figure, axis)`, and create parent directories before
saving. Figures go to `figures/`, which is tracked but empty.

## Testing conventions

- One test module per source module, named `test_<module>.py`.
- Test names are full sentences describing the physics claim, not the function called:
  `test_ultrarelativistic_beta_approaches_one`,
  `test_probabilities_partition_unity`,
  `test_far_region_is_suppressed_for_short_lab_decay_length`.
- Tests assert **physical properties** — limits, normalization, partitions of unity,
  suppression in the expected regime — rather than hard-coded numbers copied from a run.
- `pytest.approx` for float comparison; `@pytest.mark.parametrize` for the invalid-input
  cases; `pytest.raises(ValueError, match=...)` where the message itself matters.
- Every public function should have both a valid-input test and an invalid-input test.

## Notebooks

- `01_decay_probability_1d.ipynb` is the only real one: it derives the 1D exponential
  decay law and plots `P(ctau)`, survival probabilities, decay PDFs and toy-region
  comparisons.
- `02`, `03` and `04` are single-markdown-cell placeholders. Filling one in is a real
  task, not a formality.
- Notebooks are committed **without outputs**. Clear outputs before committing;
  `.ipynb_checkpoints/` is gitignored.
- Notebooks import from the installed package; they do not redefine physics inline.

## Documentation

`llp-acceptance-lab/README.md` documents the implemented physics with plain-text
formulas (not LaTeX) in fenced `text` blocks, followed by a repository layout, a notebook
index and a "Limitations" list. Any change to the physics API means updating: the
README's physics section, the notebook index if a notebook changed status, and the
limitations list.

`reports/informe_llp_acceptance_lab.tex` is a LaTeX report scaffold with
`references.bib`. There is no build script; it is compiled manually.

## Commit conventions

Short imperative subject lines, no scope prefixes, no body, one logical change per
commit — matching the existing history:

```text
Add toy 1D detector regions
Test toy 1D detector regions
Document toy detector regions and notebook
Turn notebook 01 into a toy LLP acceptance study
```

Code, its tests and its documentation are frequently separate commits.
