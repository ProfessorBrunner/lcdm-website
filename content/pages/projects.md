Title: Undergraduate Research Projects
Slug: gsoc
Date: 2014-02-13
Modified: 
Authors: Robert J. Brunner
Save_as: ugprojects.html
Tags: Image Processing, Hyperspectral, Source Detection, Photometry, Machine Learning Classification, Cosmology, Correlation Function, Power Spectrum
Construction: True
Summary: Currently Available Undergraduate Research Projects

## Undergraduate Research Projects

The following list of projects are currently open for undergraduate
researchers, including Google Sumer of Code particpants. If you have an
interest in a related concept, feel free to propose something new,
especially if it lies in the fields of computer vision, machine
learning, or cloud computing (or all three!). If you are interested in
any of these projects, please contact Professor Brunner directly.

### Bayesian Source Classification

*Summary*: Develop a Python-based implementation of a Bayesian source
classification algorithm that can scale to billions of sources. 

*Details*: Astronomers have entered the era of survey astronomy, for
example we have the recently completed [Sloan Digital Sky
Survey](http://www.sdss.org) (SDSS) and the recently started [Dark
Energy Survey](https://www.darkenergysurvey.org) (DES). These surveys
generate TBs and now PBs of imaging data that can be used to annswer
fundamental questions about our Cosmos. But before the processed image
data can be used scientifically, we must first separate out the stars in
our Mikly Way galaxy from the galaxies that make up the cosmic web.

One new approach to classifying sources in a an astronomical survey was
recently developed by Henrion et al. (2010). This approach computes the
Bayesian Evidence from the input photometric measurements and makes a
probabilistic classification. Their implementation is written in he R
programming language and was applied to a small data set from the UKIDDS
survey (an infrared sky survey). To make this approach more effective
and to enable future enhancements to the method, we are looking for a
student to convert this R implementation into Python.

*Starting Conditions*: The R implementation is available on github and
provides an implementation of the algorithm. 

*Expected Outcomes*: We have test data on which to compare the new
Python version to the original R version. At a minimum we expect the
student to complet the Python version and verify its accuracy against
the R version. A second gola would be to apply this data to a large,
deep survey data to test scaling performance and identify bottlenecks.
The final goal will be to implement performance improvements to
accelerate this new implementation to scale to billions of sources.

### Machine Learning Based Source Classification

*Summary*: Develop Python based versions of several popular classification
algorithms including SVM and random forests that can scale to billions
of source.

*Details*: With the growth of large surveys in astronomy, we need rapid
implementations to reliably classify sources detected in PB-scale
imaging surveys as star, galaxy, artifact, or unknown. This project will
require a student to develop machine learning implementations of popular
algorithms in the Python and Java programming languages for the source
classification problem. Particular algorithms of interest include a
Support Vector Machine (SVM) and a Random Forest.

*Starting Conditions*: Existing work on both of these approaches (and
several others) already exists. But the implementations are written in
other languages. The student will take these existing implementations
and existing machine learning libraries like scikit-learn or Mahout and
leverage existing codes to make more precise classifications.

*Expected Outcomes*: The student will develop classification
implementations in Python by using scikit-learn and in Java by using
Apache Mahout for the SVM and Random Forest algorithms. A secondary goal
will be to compare the performance and efficacy of these different language
implementations on real survey data.

### Quantification and Mitigation of Systematic Effects in Cosmological Measurements.

*Summary*: Develop a Python or Java (preferred) based implementation to
rapidly quantify and mitigate systematic efects in cosmological
measurements from large sky surfveys.

*Details*: Large sky surveys obtain a tremendous volume of new data, but
this data is sometimes affected by observational limitations, like
atmospheric blurring, sky brightness variations, and interstellar dust.
To properly analyze the data, the effect of these systmatics must be
quantified and hevily affected data must be removed from the analysis.

In this project, the student will leverage the HEALPix sky tessellation
scheme to pixelate the imprint of the various systematic effects on the
sky. The pixel values will encode the value of the specific systematic
effect, and different pixel maps will be constructed for different types
of systematics. A method for transforming a HEALPix encoded systematic
into a linear multi-order coverage map (MOC) will be developed, along
with methods for performing logical operations on these MOCs in order to
generate a window function fo a particular sky survey. The window
function will specify where we expect to find clean, unaffected data and
where data are potentially affected to a degree that they must be
excluded from a cosmological analysis.

*Starting Conditions*: The HEALPix standard has multiple language
bindings, and the MOC is an International Virtual Observatory standad
with existing codes to serve as a guide for writing, reading, and
performing logical combinations of MOCs.

*Expected Outcomes*: The student will be expected to develop software to
encode a systematic in a HEALPix map, to extract a MOC fomr a HEALPIx
encoded systematic map, and to perform logical operations on multiple
input MOCs. Finally, the student will provide a software tool to allow a
scientist to take a final, combined MOC and generate a HEALPIx encoded
window function for a particular survey data set.

### Identifying Strong Gravitational Lenses in Astrophysical Databases

*Summary*: Identify strong gravitational lenses in astronomical databases.

*Details*: Strong Gravitational Lenses are amazing creations, where a
distant background galaxy or quasar is lensed by a foreground galaxy or
galaxy group. As a result, a distant source that might have been too
faint to detect on Earthis visible for detailed study. In addition, the
lensed source sometimes appears as either a distorted arc or as a
multiply imaged copy of the original. Despite their odd appearance,
finding srong lens systems remians very difficult for machines, and the
largest sample of lenses generally involved crowdsourcing.

In this project, we expect a student to instead develop new, custom SQL
queries along with specialized Python codes to first intelligently
select possible lens candidaes directly from the survey archive and to
subsequently cull this list of false positives by using custom Python
code to quantify the likelihood of the source being a lens.

*Starting Conditions*: The basic concepts of this project are laid out,
including a draft SQL query, and the mathematical framework to cull the
false positives.

*Expected Outcomes*: The student will be expected to complete the SQL
query, which involves multiply nested joins. Second the student will
write post-processing code in Python to cull this list by coparing the
observed location of candidate lenses with the theoretical expectations.
As time permits, the student may explore additional deep learning
techniques to enable strong lens detection as an image anomaly.

### Cloud-based Cosmological Measurements

*Summary*: Develop a cloud-computing based implementation of the standard
two-point correlation function.

*Details*: A correlation function measures the likelihood that one
source (like a galaxy) will be within a given distance from another
source (like another galaxy). Correlation functions are often done in
angular coordinates, so the distance is a one-dimensional angle. In this
project, the student will develop a two-dimensional correlation
function. This approach will uniquely be able to measure if any	
systematic effects due solely to the observational strategy are present.

*Starting Conditions*: An existing implementation of a single angle
two-point correltationfunction exists. 

*Expected Outcomes*: The student will convert this to Java to run on
Hadoop, and second, extend this new implementation to measure the
correltation function in terms of two angles. Finally, the student will
test this new implementation to verify its accuracy.

### Probabilistic Cosmological Measurements

*Summary*: Develop a probabilistic two-point correlation code.

*Details*: The two-point correlation function (TPCF) is a very important
measure of the distribution of a set of points, particularly in
Cosmology, where it is used to measure the clustering of galaxies in the
Universe. TPCF measurements can be compared to theoretical predictions
in order to constrain the allowed values of cosmological quantities like
the amount of dark matter or dark energy in the Universe. Most current
TPACF implementations, however, always assume a source measured in a sky
survey is unambigously a galaxy and that it has a known distance from
Earth.

This project is desinged to remove these limitations. By including a
probabilistic classification for whether a source is a galaxy or not and
a probability density function for the distnace a source is located from
Earth, we can use significantly more data to make more precise
cosmological measurements with exact same input data.

*Starting Conditions*: A fast, dual-tree implementation of the TPACF
algorithm has been developed an dpublished by our group. This code is
written in C and forms the basis for the new code implementation. An
optional project is to also develop a probabilsitic power spectrum
esimtator, for which we also have an existing implementation written in
C. Both of these codes are run on supercomputers to make their computations.

*Expected Outcomes*: The student will first modify the existing TPACF
code to read probabilities for each source (along with their positions
on the sky) from an input file. Second, the student will modify the
TPACF computation to include these probabilities in the calculation of
the correlation function (the probabilities will effectively act like a
weight for each source in the measurement). Finally, the student will
test the accuracy and performance of the new code on existing data. An
optional second algorithm is the Angular Power Spectrum, for which a similar
modification can be made.