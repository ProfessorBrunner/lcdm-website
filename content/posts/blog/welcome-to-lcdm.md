Title: An Introduction to the LCDM Website
Slug: welcome
Date: 2014-01-06
Authors: Robert J. Brunner
Tags: Pelican, LCDM, Python
Comments: True

<!-- PELICAN_BEGIN_SUMMARY -->
The LCDM website has been under development for nearly seven years,
although our [first website](http://www.sdss.jhu.edu/~rbrunner/) dates
from 1995. During this time, the website has been developed by writing
hand coded HTML, by using a wiki (multiple ones in fact), and by trying
Wordpress. In the end, however, progress has been hampered by either the
difficulty in creating content (via hand crafted HTML) or in maintaining
a secure site (when using duynamic solutions like a wiki or a bloging
tool). Coupled with a painful disk crash where much of the previous
content was lost, and the LCDM website was basically on life-support.

<!-- PELICAN_END_SUMMARY -->

Several recent changes, however, have driven the need for a reinvestment
of time and resources into the LCDM website. First, a recent NSF CDSE
award requires, in part, the LCDM website to be functioning to
communicate the work we do to the broader community and the general
public. Second, the LCDM group has recently grown and this website will
provide a mechanism to both record our progress as well as educate new
members on the various research projects that are underway. Finally, the
growth of static content generators appears to solve the two problems
holding back previous versions of the LCDM website. In this
approach, content is written in a special markup format and translated
into a set of static content files that are served by the LCDM webserver.

## Building the website

As briefly discussed on the [LCDM About webpage](/about.html), this
website is built using the
[Pelican](https://github.com/getpelican/pelican), a static site
generator written in [Python](http://python.org). Content can be written
in [Markdown](http://daringfireball.net/projects/markdown/) or
[ReStructured
Text](http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html
) markup formats. Pelican converts these documents into static content
that can be dropped into an existing website. Pelican uses the
[Jinja2](http://jinja.pocoo.org/) template engine, written in Python, to
support custom processing of all or some of the input content.
Furthermore, Pelican organiazes the conversion process from input
content to static site content in themes, which simplifies the process
of changing the look-n-feel of a particular website as well as the
organization of the website content.

But Pelican isn't perfect, or at least not perfectly suited,
out-of-the-box, for building the LCDM website. First, Pelican was
primarily developed to build a blogging website. In Pelican parlance, a
blog is dynamic with posts being added over time. Pelican also supports
a limited number of pages, which are static, and correspond to more
traditional web pages. While the concept of adding a blog (which you are
now reading!) has been a long-time goal, the LCDM website is primarily
built around pages that describe our on-going research projects. Second,
Pelican doesn't easily support multiple directories (which are generally
used to organize webpages) for pages. Furthermore, since the directory
and filename are standard metadata for writing the static page content,
matching the new LCDM wesbtie to the old LCDM website proved difficult. 

In the end, the solution was to develop a custom Pelican theme that
added custom metadata tags to all pages and posts in order to properly
build the static site. For example, to build project hierarchies, we add
the following tags to a page:

    Type: project
    Parent: dmml
    Construction: True
    Comments: True
    Save_as: research/dmml/photoz.html
    Template: lcdmprojects
    
The _Type_ tage specifies the type of the page being built and can be
either research, project, paper, poster, presentation, background, or
references. The _Parent_ tag links the current page to another page,
whcih enables compound pages to be built, for example, a list of related
projects.  While the _Construction_ and the _Comments_ tags indicate
whether the current page should be marked as *Under Construction* and
whether [Disqus](http://disqus.com) comments should be enabled for the
current page.

The next two tags are standard Pelican metadata tags. The  _Save\_as_
tag allows the developer to customize the output page layout. This was
important for the LCDM website since we had top level directories for
research, code, data, and teaching, with subdirectories for different
subprojects. Since Pelican requires all page content to be stored in the
pages directory, the default Pelican setup would place all output pages
in a single directory, or at most a two-level directory hierarchy by
using the _{category}/{slug}_ metadata. The _Template_ tag specifies the
custom LCDM Jinja2 template file that should be used to process the
current content file.

## Conclusion

The full details of the LCDM Website hierarchy and a discussion of the
diffecurrent LCDM Pelican theme and associated Jinja2 template files
will be presented in future posts. However, all static content for the
LCDM website is hosted on github, including the [LCDM Pelican
theme](https://github.com/ProfessorBrunner/lcdm-pelican) and the [LCDM
website content](https://github.com/ProfessorBrunner/lcdm-website). The
License for these materials is the University of Illinois/NCSA license,
which is fairly flexible. To use them, you basically need to maintain
the LCDM copyright notice. Of course, please let us know if you find the
LCDM site useful or interesting!
