Title: Fast Two-point Correlation Code
Slug: tpacf-code
Date: 2007-09-11
Modified: 2013-12-16
Authors: Robert J. Brunner
Save_as: code/tpacf.html
TAGS: TPACF, correlation function, cosmology, hpc, mpi, openmp
Construction: False
Summary: We have released our fast two-point correlation function estimation code.

## Introduction

We have implemented a dual kd-tree implementation of the two-point
correlation (both spatial and angular) function code. The implementation
was first described in [Dolence & Brunner
2009](http://www.linuxclustersinstitute.org/conferences/archive/2008/PDF/Dolence_98279.pdf) 
and was used and further described in [Wang, Brunner, & Dolence
2013](http://adsabs.harvard.edu/cgi-bin/bib_query?arXiv:1303.2432).

## Public Archive

The code base is currently maintained at [github](https://github.com/ProfessorBrunner/tpacf).

Note: The current version of the code merely computes binned pair
counts. To construct a correlation function estimator (e.g.,
Landy-Szalay), you must combine binned pair counts appropriately.

## Original Archive

The originally published [correlation function
code](/static/tpacf/CorrCode.tar.gz) is permanently archived at the LCDM site.

For completeness, you can directly view the original [README](/static/tpacf/README-TPACF) file.

## Contact:

If you have any questions about these codes, please contact Robert
Brunner at: bigdog AT illinois.edu
