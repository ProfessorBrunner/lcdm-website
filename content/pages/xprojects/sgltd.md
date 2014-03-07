Title: Strong Gravitational Lens Time Delays
Slug: sgltd
Date: 2014-03-02
Modified: 2014-03-03
Authors: Robert J. Brunner
Save_as: xprojects/sgltd.html
Tags: Data Mining, Machine Learning, Classification, Image Classification, Crowdsourcing, Mobile Application 
Type: xproject-hot
Comments: True
Summary: Develop and apply new strong gravitational lensing time delays measurements.

## Project Synopsis

Accurately measuring time delays to strong gravitational lens systems is
a new technique to enable constraints on dark energy.

## Project Description

Few strongly lensed quasar systems are known, yet they are important
cosmological tools. A strongly lensed quasar appears multiple times in
an image due to the presence of a foreground lensing galaxy. Since the
light that forms the different quasar images takes different paths
through the Universe to reach us, the light will also take a different
amount of time to reach us. Since quasars are inherently variable in
their light output (see Figure 1 for a simulated example), and in fact
they can be modeled as stochastic processes, the quasar variability can
be used to measure the time delay between two or more quasar images.

<img src="{filename}/static/images/LightCurves.png"
alt="Galaxy shown in different filters"
width="400px" height="auto" align="right"
display="block" style="margin: 40px;" />

A number of techniques hav been developed and applied to this problem,
with the best techniques still having accuracies of around a few days
(given time delays of a year or more). To achieve precision cosmological
constraints, we need to reduce the error on this measurement. The
approach we propose to develop is based on the distance correlation
method.

To test this technique, we will resort to both known lens systems, for
example from the [CosmoGrail](http://cosmograil.epfl.ch) project. We also will develop a simulation
framework to model the quasar stochasticity, impose random time delays in
the resultant light curves, and impose arbitrary and seasonally observational
effects in order to truly characterize the efficacy of this algorithm.

Finally, we will apply this new technique to the LSST strong lensing
time delay challenge.

Future Target: Compute time delays directly from images.

## Programming Notes

- An implementation of the distance correlation method, to operate on
two lightcurves and returning the estimate time delay along with an
associated error. This can either be done in R or Python.

- An implementation of the lightcurve simulation framework, most likely
in Python.

## Starting Conditions

A prototype lightcurve simulator exists in Python. A prototype distance
correlation code exists in R. This code can either be left in R or rewritten in Python.

## Expected Outcome

The main outcome is the development of the new time delay estimation
code and its application to the LSST time delay challenge simulated
data, which is due by July 1, 2014.

## Personnel

The lead mentor for this project is Professor Feng Liang, with
assistance from Professor Brunner.

## References

- [Distance Correlation](http://en.wikipedia.org/wiki/Distance_correlation)

- [CosmoGrail](http://cosmograil.epfl.ch) project 

- Castles [multiple object lensing survey](http://www.cfa.harvard.edu/castles/)

- LSST [Time Delay Challenge](http://timedelaychallenge.org)

- [Stochastic Fluctuation](http://arxiv.org/abs/0903.5315) model for quasar variability.

- [Github](https://github.com/ProfessorBrunner/sgl-timedelay) Repository

