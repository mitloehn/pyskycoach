Welcome to the PySkyCoach!

This application shows a view of the sky and tests your memory of the
location of deep sky objects. In addition to the Messier catalog
several other object lists are provided with the package, and 
additional lists can be prepared in CSV format.


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

In the default mode stars up to visual magnitude 5 are plotted, 
roughly corresponding to what can be seen with the naked eye from a 
moderately dark site. You can move the current view by dragging the
mouse up and down for right ascension, and left and right for declination.
You can also use the mouse wheel to zoom in and out.

Once you decide on a section of sky you can press the Challenge
button. Change of view is now disabled, and your task is to click on 
the location of the DSO named in the bottom 
bar. The correct location will be shown, with a line displaying the 
difference from your estimate. The program will present a maximum of 
5 challenges per round, depending on the region of sky and the set of 
DSO selected. At the end of the round a score will be shown, and
change of view is once more enabled. The 
score is simply the sum of the errors in the x and y axis relative to 
the window dimensions.

Optionally a 6.5 magnitude star catalog can be loaded via the File
menu for more detailed star charts. This is useful when viewing 
very small regions of sky.

There are several methods of projection: 

- The orthographic projection is the default. If you zoom out and set
  the declination and right ascension corresponding to your observing 
  time and location you get a 180 degree view of the whole visible
  night sky, similar to a planishere.
- In the 100 deg view the right ascension and declination are directly 
  used as cartesian coordinates. This simple method has the advantage
  that the grid is rectangular. Towards the celestial poles the
  distortion becomes very high.
- The whole celestial globe can be drawn with this method as well,
  resulting in an overview chart resembling a cylinder projection.
- Two separate views with azimuthal projection are available for the 
  northern and southern celestial poles.  

Use the DSO menu to change the set of deep sky objects: 

- messier:  complete Messier list (default)
- rascngc:  RASC's Finest N.G.C.
- urban:    AAAA urban club list 
- southbin: AL southern binocular list
- easymes:  AL easy binocular Messier objects

The file format is name, right ascension, and declination, separated 
by comas. You can put your own files in the same directory with the 
program and add them in the FILES list at the top of the code. Note 
that Messier objects referenced by NGC numbers will be translated to 
Messier numbers.


TODO:

The current version serves as a very basic training program for 
locating deep sky objects; that much works as intended. However, many 
improvements come to mind, and may be implemented sooner or later:

- The 'Show All' option should indicate the object type in the display, 
  and the labels should not overlap. This would mean additional file 
  data for object types, and some algorithm for better label 
  positioning.

- On a more ambitious scale, different types of quizzes would probably 
  be more motivating, e.g., give the name and type of a displayed 
  object; point out all open clusters in the area; etc. This would mean 
  a major redesign of the interface, so this is more of a long term 
  goal.


ACKNOWLEDGEMENTS:

This work would not have been possible without the efforts of many 
contributors to amateur astronomy resources and professional data 
made available on the Internet. Many thanks go to everyone involved!

- The complete list of Messier objects
  from http://messier.seds.org

- The Royal Astronomical Society of Canada Finest N.G.C. Objects List 
  compiled by Alan Dyer

- The AAAA Urban Astronomy Club List of Objects
  compiled by John Wagoner (stargate at gte.net)

- The Astronomical League's Southern binocular objects list;
  easy binocular Messier object list

- BSC5P Bright Star Catalog, available at
  http://heasarc.gsfc.nasa.gov/W3Browse/star-catalog/bsc5p.html

A good starting point for similar resources is 
http://messier.seds.org/xtra/similar/similar.html


Clear Skies!

Johann Mitloehner, Vienna, Austria, August 2013

mitloehn@wu.ac.at

