Welcome to the PySkyCoach!

This application shows a view of the sky with the objective of 
locating deep sky objects with a non-magnifying finder. Stars up to 
visual magnitude 5 are plotted, roughly corresponding to what you can 
see with the naked eye from a moderately dark site. Several deep sky 
object lists are provided with the package, and additional lists can 
be prepared using a simple CSV format.


INSTALLATION:

Download the ZIP archive and extract to a directory of your choice. 
Alternatively, you can use git to obtain the files. To run the 
program you need the Python environment, which you can download from 
www.python.org if necessary. Depending on your operating system you 
may have to install the package python-tk as well.

With Python installed you can start the program by typing "python 
pyskycoach.py" on the command line. Double-clicking on the file 
pyskycoach.py in your file manager should work as well, but depending 
on your system you may need to configure your file manager first to 
run Python on files with extension .py; this option is usually called 
'open with' or similar.


USAGE:

Your task is to click on the location of the DSO named in the bottom 
bar. The correct location will be shown, with a line displaying the 
difference from your estimate. The program will present a maximum of 
5 challenges per round, depending on the region of sky and the set of 
DSO selected. At the end of the round a score will be shown. The 
score is simply the sum of the errors in the x and y axis relative to 
the window dimensions.

You can use the RA and DE buttons and the View menu to change the 
view of the celestial sphere before starting a new round. For views 
within +/- 75 degrees the right ascension and declination are 
directly used as cartesian coordinates. This method is simple and 
fast, and it works reasonably well for most parts of the sky, but it 
would result in severe distortion towards the celestial poles. 
Therefore two separate views with azimuthal projection are available 
for the northern and southern celestial poles via the View menu. 

Use the DSO menu to change the set of deep sky objects: 

- easymes.csv: easy Messier objects
- messier.csv: complete Messier list
- urban.csv:   AAAA urban club list 
- rascngc.csv: RASC's Finest N.G.C.
- southbin.csv: AL southern binocular list

The file format is name, right ascension, declination, all separated 
by comas. You can put your own files in the same directory with the 
program and add them in the FILES list at the top of the code. Note 
that Messier objects referenced by NGC numbers will be translated to 
Messier numbers.

Clear Skies!

Johann Mitloehner, Vienna, Austria, July 2013
mitloehn@wu.ac.at

TODO:

The current version serves as a very basic training program for 
locating deep sky objects; that much works as intended. However, many 
improvements come to mind, and may be implemented sooner or later:

The charted sky section does not change with the size and shape of 
the window, so depending on the current view a change in window shape 
will result in more or less distortion. This is rather 
unsatisfactory, and should be taken care of automatically.

The 'Show All' option should indicate the object type in the display, 
and the labels should not overlap. This would mean additional file 
data for object types, and some algorithm for better label 
positioning.

On a more ambitious scale, different types of quizzes would probably 
be more motivating, e.g., give the name and type of a displayed 
object; point out all open clusters in the area; etc. This would mean 
a major redesign of the interface, so this is more of a long term 
goal.

ACKNOWLEDGEMENTS:

This work would not have been possible without the efforts of many 
contributors to amateur astronomy resources and professional data 
made available on the Internet. Many thanks go to everyone involved. 
A good starting point for similar resources is 
http://messier.seds.org/xtra/similar/similar.html

The Astronomical League's Binocular Messier Club
List A 1 of 42 easy Messier objects,
as well as the Southern binocular objects list

The complete list of Messier objects
from http://messier.seds.org

The AAAA Urban Astronomy Club List of Objects
compiled by John Wagoner (stargate at gte.net)

The Royal Astronomical Society of Canada Finest N.G.C. Objects List 
compiled by Alan Dyer

BSC5P Bright Star Catalog, available at
http://heasarc.gsfc.nasa.gov/W3Browse/star-catalog/bsc5p.html

