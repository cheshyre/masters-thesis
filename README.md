# Matthias Heinz's Master's thesis: Analysis of three-body effects in the in-medium similarity renormalization group

This repository contains my Master's proposal and thesis and the slides for both defenses.

## Abstract

The in-medium similarity renormalization group (IMSRG)
is an *ab initio* many-body method used to great success
to solve the time-independent Schrödinger equation in medium-mass nuclear systems.
Its computational cost scales polynomially in the size of the truncated model space,
and its formalism is highly flexible,
leading to multiple variants that have been developed to extend its original closed-shell
formulation to open-shell systems.

The current state-of-the-art implementations truncate the IMSRG equations
at the normal-ordered two-body level,
the first non-trivial order in the expansion.
In this work, we seek to systematically study the effects
of extending this truncation to the normal-ordered three-body level,
the so-called IMSRG(3) approximation.
Exploitation of symmetries is essential to making IMSRG(3) calculations tractable.
We present the reduced `J`-scheme IMSRG(3) working equations,
which we arrive at by applying angular-momentum reduction to the IMSRG(3) for spherical systems.

We use our implementation of the `J`-scheme IMSRG(3)
to investigate three-body contributions
that first appear in the IMSRG(3)
in light and medium-mass nuclei.
We introduce approximate IMSRG(3) truncations
that leave out the most expensive parts of the IMSRG(3).
We find that in helium-4
and oxygen-16
in a restricted `emax=2` model space,
these approximate IMSRG(3) truncation schemes
deliver small, sub-percent corrections to the ground-state energies
and larger corrections to radii.
Further, by investigating the behavior
under the removal or inclusion of certain terms,
we see that the organization by computational cost
used to set up our approximate truncation schemes
is poorly motivated
and some computationally more expensive terms
provide larger corrections to ground-state energies
than the cheaper terms in the truncation.
This work is a key step towards
high-precision many-body calculations of medium-mass nuclei
in the IMSRG.

## Build requirements

The build system uses a Makefile.
This does two things:

1. It (re)generates figures when the underlying data or scripts are changed or the PDFs are absent.
2. It (re)builds the output PDFs based on changes in the chapters or the figures.

All (non-external) figures are generated via `matplotlib`.
The Makefile uses [poetry](https://python-poetry.org/) to manage the virtual environment,
which contains `numpy`, `scipy`, and `matplotlib` to generate the plots.
For this to work on your computer, you must install poetry.
I recommend following the instructions on the [project website](https://python-poetry.org/),
but a simple install can be achieved via:
```
python3 -m pip install --user poetry
```
After this, set up the virtual environment via
```
poetry install
```
in the root directory.

The LaTeX build is handled by [latexrun](https://github.com/aclements/latexrun),
which is provided in the code here for convenience.

## Versioning system

I am testing out a private/public 2 repository system,
which will allow me to develop quickly on the private repository,
keeping the full commit history for obvious reasons,
while updating a public repository with large-scale changes.
I will attempt to use [a variant of semantic versioning for documents](https://semverdoc.org/)
(see also the original [semantic versioning](https://semver.org/))
to keep track of versions for the documents.
Each document in the repository will be given a version number with 3 integers, MAJOR.MINOR.PATCH.
Before submission of the defense version the documents,
the version number changes should be interpreted as follows:

1. The MAJOR version number will be incremented when
   the document has reached defense version.
2. The MINOR version number will be incremented when
   the structure of the content has been changed
   (addition or removal of sections or subsections).
3. The PATCH version number will be incremented when
   fleshing out content in sections or fixing typos.

After the defense, the version number changes should be interpreted as follows:

1. The MAJOR version number will be incremented when
   a major claim made in the document has been shown to be incorrect.
   It is unlikely that the documents will be rewritten,
   but in the (hopefully unlikely) case that this happens
   I will include warnings at the beginning of incorrect sections and on the affected slides.
2. The MINOR version number will be incremented when
   the content of the documents has changed in some way that
   is not a simple typo but also does not invalidate the main claims of the thesis.
3. The PATCH version number will be incremented when
   typos are fixed.
   In most cases typos in equations will fall under this versioning classification when fixed.
   The exception to this will be formulas that are central to the document
   and are not generally available for cross-referencing in other literature.

**Summary**: This means each document will reach version 1.0.0 at the time of the defense.
Version numbers beyond that mean that I was made aware of typos or errors in my work.
A version number `>=2.0.0` indicates that something was significantly wrong,
most likely making the documents not worth reading.

