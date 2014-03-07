Title: Machine Learning Based Source Classification
Slug: mlsc
Date: 2014-03-03
Modified: 
Authors: Robert J. Brunner
Save_as: xprojects/mlsc.html
Tags: Data Mining, Machine Learning, Classification, Python, Source Classification
Type: xproject
Comments: True
Summary: Develop Python based implementation of popular machine learning classifications

## Project Synopsis

Develop Python based versions of several popular classification
algorithms including SVM and random forests that can scale to billions
of source.

## Project Description

With the growth of large surveys in astronomy, we need rapid
implementations to reliably classify sources detected in PB-scale
imaging surveys as star, galaxy, artifact, or unknown, see
Figure 1 for an example of the problem from the SDSS survey.

<img src="{filename}/static/images/SGmag.png"
alt="Galaxy shown in different filters"
width="400px" height="auto" align="right"
display="block" style="margin: 20px;" />. 

This project will require a student to develop machine learning
implementations of popular algorithms in the Python and Java programming
languages for the source classification problem. Particular algorithms
of interest include a Support Vector Machine (SVM) and a Random Forest.
Other algorithms are possible, so don't hesitate to make suggestions.


## Programming Notes

Ideally, initial development will occur in Python. As necessary, we may
move to Java to take advantage of Hadoop and the Mahout library. 

## Starting Conditions

Existing work on both of these approaches (and
several others) already exists. But the implementations are written in
other languages. The student will take these existing implementations
and existing machine learning libraries like scikit-learn or Mahout and
leverage existing codes to make more precise classifications.

## Expected Outcome

The student will develop classification
implementations in Python by using scikit-learn or in Java by using
Apache Mahout for the SVM and Random Forest algorithms. A secondary goal
will be to compare the performance and efficacy of these different language
implementations on real survey data.

A target output would be a consistent packaging of several machine
learning algorithms for the source classification problem to simplify
their use on other data sets and in comparison with other techniques.

## Personnel

The lead mentor for this project is Edward Kim, with assistance from Professor Brunner.

## References

- The [Sloan Digital Sky Survey](http://www.sdss3.org)
- The [Dark Energy Survey](http://www.darkenergysurvey.org)

- [Machine Learning for Photometric Redshifts](/static/code/MLZ/MLZ-1.0.tar.gz)

- [Astronomical Python](http://www.astropy.org) libraries

- [Python machine learning](http://scikit-learn.org) libraries

- [Header Information](/static/data/classify/SG_small.header) for sample training data

- [SDSS Small Train](/static/data/classify/SG_small.train.zip) data file (3.3 MB)

- [SDSS Small Test](/static/data/classify/SG_small.test.zip) data file (33 MB)