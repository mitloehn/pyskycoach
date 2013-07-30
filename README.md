Welcome to the PySkyCoach!

This application shows a view of the sky with the objective of 
locating deep space objects, as you would with a non-magnifying 
finder. Stars up to visual magnitude 5 are plotted, 
roughly corresponding to what you can see with the naked eye 
from a moderately dark site.


INSTALLATION:

Download the ZIP archive and extract to a directory of your 
choice. Alternatively, you can use git to obtain the files.
To run the program you need the Python environment, which you 
can download from www.python.org if necessary. Depending on your
operating system you may have to install the package python-tk
as well.
With Python installed you can start the program by 
double clicking on the file pyskycoach.py in your file manager, 
or by typing "python pyskycoach.py" on the command line.


USAGE:

Your task is to click on the location of the DSO named in the 
bottom bar. The correct location will be shown, with a line 
displaying the difference from your estimate. The program
will present a maximum of 5 challenges per round, depending on
the region of sky and the set of DSO selected. At the end of
the round a score will be shown. The score is simply the
sum of the errors in the x and y axis relative to the window
dimensions.

You can use the RA and DE buttons and the View menu to change 
the view of the sky before starting a new round. 
Right ascension and declination are simply drawn on 
rectangular x/y coordinates within the window. This works 
reasonably well up to about 70 degrees but results in severe 
distortion towards the celestial poles. Depending on the view 
a change in window shape will result in less distortion.


CONFIGURATION:

Use the File menu to change the set of DSO: 

- easymes.csv: easy Messier objects
- messier.csv: complete Messier list
- urban.csv:   AAAA urban club list 
- rascngc.csv: RASC's Finest N.G.C.

The file format is name, right ascension, declination, all 
separated by comas. You can put your own files in the
same directory with the program and add them in the FILES 
list at the top of the code.
Note that Messier objects referenced by NGC numbers will be 
translated to Messier numbers. 


Clear Skies!

Johann Mitloehner, Vienna, Austria, July 2013
mitloehn@wu.ac.at


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

The Royal Astronomical Society of Canada Finest N.G.C. Objects List 
compiled by Alan Dyer

BSC5P - Bright Star Catalog, available at
http://heasarc.gsfc.nasa.gov/W3Browse/star-catalog/bsc5p.html

