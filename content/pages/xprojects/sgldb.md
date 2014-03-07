Title: Identifying Strong Gravitational Lenses in Astrophysical Databases
Slug: sgldb
Date: 2014-03-03
Modified: 
Authors: Robert J. Brunner
Save_as: xprojects/sgldb.html
Tags: Data Mining, Machine Learning, Classification, Databases, Strong Gravitational Lens 
Type: xproject
Comments: True
Summary: Develop new technique to optimally identify strong gravitational lenses in astronomical databases

## Project Synopsis
Identify strong gravitational lenses in astronomical databases.

## Project Description
Strong Gravitational Lenses are amazing creations, where a distant
background galaxy or quasar is lensed by a foreground galaxy or galaxy
group. As a result, a distant source that might have been too faint to
detect on Earth is visible for detailed study. In addition, the lensed
source sometimes appears as either a distorted arc or as a multiply
imaged copy of the original (for example, see Figure 1). Despite their
odd appearance, finding strong lens systems remains very difficult for
machines, and the largest sample of lenses generally involved
crowdsourcing.

![g-band image of SDSS gravitational lens]({filename}/static/images/l1g.png)
![r-band image of SDSS gravitational lens]({filename}/static/images/l1r.png)
![i-band image of SDSS gravitational lens]({filename}/static/images/l1i.png)
![Color composite image of SDSS gravitational lens]({filename}/static/images/l1c.png)

In this project, we expect a student to instead develop new, custom SQL
queries along with specialized Python codes to first intelligently
select possible lens candidates directly from the survey archive and to
subsequently cull this list of false positives by using custom Python
code to quantify the likelihood of the source being a lens.

## Programming Notes

The primary means of searching astronomy databases is via SQL.
Additional post-processing that might be required will be done by using
Python.

## Starting Conditions
The basic concepts of this project are laid out,
including a draft SQL query, and the mathematical framework to cull the
false positives.

## Expected Outcome
The student will be expected to complete the SQL
query, which involves multiply nested joins. Second the student will
write post-processing code in Python to cull this list by comparing the
observed location of candidate lenses with the theoretical expectations.
As time permits, the student may explore additional deep learning
techniques to enable strong lens detection as an image anomaly.

## Personnel

The lead mentor for this project is Professor Brunner.

## References

- The [Sloan Digital Sky Survey](http://cas.sdss.org) database

- The [Sloan Digital Sky Survey](http://www.sdss3.org)

- The [Dark Energy Survey](http://www.darkenergysurvey.org)

- Dr Phil Marshall [demonstrates](http://www.youtube.com/watch?v=PviYbX7cUUg) Gravitational Lensing

- Introductory [review article]
(http://www.annualreviews.org/doi/full/10.1146/annurev-astro-081309-130924) on strong gravitation lensing

- The [CASTLES Survey](http://www.cfa.harvard.edu/castles/) Lens database

- The [Cassowary Lens](http://www.ast.cam.ac.uk/ioa/research/cassowary/) gravitational lens search

- [SpaceWarps](http://spacewarps.org) crowdsourcing lens search

