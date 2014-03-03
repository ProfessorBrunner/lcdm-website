Title: Cosmological Systematic Effect Visualization and Mining
Slug: sysview
Date: 2014-03-02
Modified: 
Authors: Robert J. Brunner
Save_as: xprojects/sysview.html
Tags: Data Mining, Machine Learning, Classification, Image Classification, Crowdsourcing, Mobile Application 
Type: xproject
Comments: True
Construction: True
Summary: Develop a new approach to visualizing and mining cosmological systematic effects.

## Project Synopsis

Develop a Python or Java (preferred) based implementation to
rapidly quantify and mitigate systematic effects in cosmological
measurements from large sky surveys.

## Project Description

Large sky surveys obtain a tremendous volume of new data, but
this data is sometimes affected by observational limitations, like
atmospheric blurring, sky brightness variations, and interstellar dust.
To properly analyze the data, the effect of these systematics must be
quantified and heavily affected data must be removed from the analysis.

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

## Programming Notes

TBD

## Starting Conditions

This project is currently in the design stage. The HEALPix standard has multiple language
bindings, and the MOC is an International Virtual Observatory standard
with existing codes to serve as a guide for writing, reading, and
performing logical combinations of MOCs.

## Expected Outcome

The student will be expected to develop software to
encode a systematic in a HEALPix map, to extract a MOC from a HEALPIx
encoded systematic map, and to perform logical operations on multiple
input MOCs. Finally, the student will provide a software tool to allow a
scientist to take a final, combined MOC and generate a HEALPIx encoded
window function for a particular survey data set.

## Personnel

The lead mentor for this project is Professor Brunner.

## References

- [HEALPix](http://healpix.jpl.nasa.gov)
- [MOC](http://www.ivoa.net/documents/MOC/)
- [Aladin Light](http://aladin.u-strasbg.fr/AladinLite/)

