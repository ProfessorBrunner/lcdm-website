Title: Crowdsourcing Web Application
Slug: cswebapp
Date: 2014-03-02
Modified: 
Authors: Robert J. Brunner
Save_as: xprojects/cswebapp.html
Tags: Data Mining, Machine Learning, Classification, Image Classification, Crowdsourcing, Web Application 
Type: xproject-hot
Comments: True
Summary: We want to develop a new web application to facilitate more advanced crowdsourcing classification projects.

## Project Synopsis

Traditional crowdsourcing, like the
[ZooUniverse](https://www.zooniverse.org) project, typically focus on
the identification and classification of a single type of object. For
example, the [GalaxyZoo](http://www.galaxyzoo.org) project has a user
classify the single object contained within an image. 

Many classification problems are not amenable to this approach. For
example, anomaly detection in images can have zero or more anomalies.
Thus a user viewing these images might find zero or many objects of
interest. This not only complicates the challenge of quantifying the
reliability of a classification, but also the ability of the classifier
to find **all** anomalies.

## Project Description

The change we propose to enable more general crowdsourcing experiments
in the future requires a fundamental change in how the data are both
presented and the classifications are gathered. As a result, in this
project, we propose to develop an entirely new user interface to enable
a human user to easily view, identify, and tag _features_ within an
image (see, e.g., Figure 1). The user will be able to select
pre-assigned labels, as well as enter free-form text to describe unusual
or interesting classes.

<img src="{filename}/static/images/sdss-bad.jpg"
alt="Bad Image from SDSS"
width="auto" height="auto" align="center"
display="block" />


The web application will communicate with a back-end database to obtain
the target image and to store the user classifications and other associated metadata.

## Programming Notes

- The User Interface will be primarily written in JavaScript. The
[astrojs](http://www.astrojs.org) library will prove useful.

- Security verification will need to be included for non-public data
crowdsourcing projects.

- The database backend will be SQL-92 complaint. The student will not be
required to implement this, but doing so is an option if it simplifies
the development of the overall application.

- The image server will respond to URL requests. The student can safely
assume this exists, although this also can be developed as part of a
project if doing so simplifies the development  of he application.

## Starting Conditions

This project is currently in the design stage.

## Expected Outcome

Ideally a new web application will be designed, prototyped, and deployed
on real, Dark Energy Survey data. 

## Personnel

The lead mentor for this project is Xianming Liu, with assistance from Professor Brunner.

## References

- The [Sloan Digital Sky Survey](http://cas.sdss.org) database

- The [Sloan Digital Sky Survey](http://www.sdss3.org)

- The [Dark Energy Survey](http://www.darkenergysurvey.org)

- [Galaxy Zoo](http://www.galaxyzoo.org) project 

- [Dark Energy Survey](http://eyeball.erinsheldon.net/index.html) exposure checker, with
[source code](https://github.com/pmelchior/des-exp-checker) repository.

Note the DES project data is currently restricted access. Students
working on this project will be given proper security credentials.

