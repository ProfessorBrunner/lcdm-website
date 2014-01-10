Title: SOMZ: Maps for Photo-Z
Slug: somz-paper
Date: 2013-12-15
Modified: 2014-01-08
Authors: Matias Carrasco-Kind, Robert J. Brunner
Save_as: papers/somz.html
Tags: Data Mining, Machine Learning, Photometric Redshift, Python, Self Organizing Maps, Random Atlas, Matias Carrasco Kind, Robert J. Brunner
Type: paper
Parent: photoz
Construction: True
Latex: True
sDate: 2012-11-15
aDate: 2013-03-28
pDate: 
pURL: 
Summary: We have developed a new random atlas estimation technique for photometric redshift PDF estimation.

### SOMz: photometric redshift PDFs with self organizing maps and random atlas

**Authors**: Matias Carrasco Kind and Robert J. Brunner  
**Published**:   TBD  
**DOI**: N/A

### Access:
[MNRAS Journal Article]()  
[NASA ADS Record](http://adsabs.harvard.edu/cgi-bin/bib_query?arXiv:1312.5753)  
[arXiv Posting](http://arxiv.org/abs/1312.5753)  
[LCDM Repository](/static/papers/somz.pdf)

### Abstract:
In this paper we explore the applicability of the unsupervised machine
learning technique of Self Organizing Maps (SOM) to estimate galaxy
photometric redshift probability density functions (PDFs). This
technique takes a spectroscopic training set, and maps the photometric
attributes, but not the redshifts, to a two dimensional surface by using
a process of competitive learning where neurons compete to more closely
resemble the training data multidimensional space. The key feature of a
SOM is that it retains the topology of the input set, revealing
correlations between the attributes that are not easily identified. We
test three different 2D topological mapping: rectangular, hexagonal, and
spherical, by using data from the DEEP2 survey. We also explore
different implementations and boundary conditions on the map and also
introduce the idea of a random atlas where a large number of different
maps are created and their individual predictions are aggregated to
produce a more robust photometric redshift PDF. We also introduced a new
metric, the $I$-score, which efficiently incorporates different metrics,
making it easier to compare different results (from different parameters
or different photometric redshift codes). We find that by using a
spherical topology mapping we obtain a better representation of the
underlying multidimensional topology, which provides more accurate
results that are comparable to other, state-of-the-art machine learning
algorithms. Our results illustrate that unsupervised approaches have
great potential for many astronomical problems, and in particular for
the computation of photometric redshifts.

### Implementation

The most recent implementation of the SOMZ algorithm is now included in
the Machine Learning for Photometric Redshift (MLZ) code. Both the [MLZ
code](/static/code/MLZ/MLZ-1.0.tar.gz) and the [MLZ
Manual](/static/code/MLZ/doc/html/index.html) are freely available.

### Contact:

If you have any questions about the method or the code, please contact
the authors.
