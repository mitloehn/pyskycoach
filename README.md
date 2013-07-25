Welcome to the PySkyCoach!

This application shows a view of the sky with the objective of 
locating deep space objects, as you would with a non-magnifying 
finder. All 1630 stars up to visual magnitude 5 are plotted, 
roughly corresponding to what you can see with the naked eye 
from a moderately dark site.

INSTALLATION:

Download the ZIP archive and extract to a directory of your 
choice. Alternatively, you can use git to obtain the files.
To run the program you need the Python environment, which you 
can download from www.python.org if necessary. Depending on your
operating system you may have to install the package python-tk
as well.
With Python installed you can usually start the program by 
double clicking on the file pyskycoach.py in your file manager, 
or by typing "python pyskycoach.py" on the command line.

USAGE:

Your task is to click on the location of the DSO named in the 
bottom bar. The correct location will be shown, with a line 
displaying the difference from your own estimate. When done, 
click the New button for the next random DSO. At the end of
the round a score will be shown. The score is simply the
sum of the errors in the x and y axis relative to the window
dimensions.

Use the RA and DE buttons and the View menu to change the view 
of the sky. You can also zoom in and out.
Currently there is only one method of projection: RA and DE 
coordinates are simply drawn on a rectangular grid. This works 
reasonably well up to about 70 degrees but results in severe
distortion towards the celestial poles.

CONFIGURATION:

Use the File menu to change the set of DSO: 

- easymes.csv: easy Messier objects
- messier.csv: complete Messier list
- urban.csv:   DSO list for urban observers 

Use your favorite text editor to take a look at the CSV files 
if you want to modify them. The format is very simple: name,
right ascension, declination, all separated by comas. You can
add your own files in the FILES list at the top of the program.
Note that Messier objects referenced by NGC numbers will be 
translated to Messier numbers. The lists are not limited to
DSO, they can contain double stars, or any other object with
RA and DE coordinates.

TODO:

- better scoring system
- ask object type in addition to position
- show/hide all objects in current view
- different projection method towards poles

Clear Skies!

Johann Mitloehner, Vienna, Austria, July 2013

ACKNOWLEDGEMENTS:

This work would not have been possible without the efforts
of many contributors to amateur astronomy resources and
professional data made available on the Internet. Many thanks
go to everyone involved. A good starting point for similar
resources is http://messier.seds.org/xtra/similar/similar.html

The Astronomical League's Binocular Messier Club
List A 1 of 42 easy Messier objects

The complete list of Messier objects
from http://messier.seds.org

The AAAA Urban Astronomy Club List of Objects
compiled by John Wagoner (stargate at gte.net)

BSC5P - Bright Star Catalog, available at
http://heasarc.gsfc.nasa.gov/W3Browse/star-catalog/bsc5p.html

