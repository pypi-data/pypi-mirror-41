:math:`\chi^1\chi^2` program
============================

The aim of the program is to calculate linear (refractive indices) and nonlinear (:math:`\chi^2`
for second harmonic generation) optical properties of organic crystals.


.. contents::

Installation
------------

Make sure you have installed:
 - gfortran
 - python 3.6
 - open babel

Installation:
 - pip install chi1chi2
 - for the fortran programs a Makefile is provided with the repository:
   *make* command builds the programs in the build/ directory

Description
-----------

The whole program constitutes a set of scripts that need to be executed in order.

There are four main steps:

    1. Input preparation (optionally - geometry optimization)
    2. Optical properties of molecular sub-units calculations
    3. Calculations of bulk properties
    4. Analysis of the results

The purpose of this file is to lead the user through all these steps.


Step *1* - Input preparation
----------------------------

A) from Cif (easy path)

    use *chi.from_cif* to get geometry for further optimization with *e.g.* crystal09/14/..

B) from fractional coordinates

    use *chi.from_fra* script (see: examples/mna_cif.fra, examples/mna_cif2.fra to see the convention)
      (remember to adjust the

C) manually

    see examples for the convention


Step *1a* after geometry optimization
-------------------------------------

D) use *chi.from_crystal* script to adjust the coordinates and charges after *crystal* geometry optimization

E) run *chi.input_preparator* script to get input files for:

    - *charge_generator* program (example usage: *charge_generator < chg1.inp*)

    - Lorentz tensor with *lorentz* program (example usage: *lorentz < lorentz.inp > L.dat*)


Step *2* - property calculation
-------------------------------

Use sets of charges, geometries and follow your favorite property calculation procedure.
Additional shell scripts could be provided in later releases.

Step *3* - core calculations
----------------------------

Use script *chi.main* to get the :math:`\chi^1` and :math:`\chi^2` tensor components in the so called ab'c* reference frame.

v 0.1.1: Q-LFT calculations enabled!

Step *4* - result analysis
--------------------------

This step will be provided in future releases.

- Refractive indices and optical indicatrix analysis (0.2.0)
- Magnitude of the :math:`\chi^2` tensor components in the direction of the optical indicatrix (0.2.0)
- Phase matching diagrams (in future plans)

Examples
--------

See the examples/examples.pdf to follow the steps used in the integration tests.
The files used for the tests are located in the tests/integration directory:

    - *input* as a starting point
    - *expected* as a reference
