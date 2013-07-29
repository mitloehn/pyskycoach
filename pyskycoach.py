#!/usr/bin/python
# Copyright 2013 Johann Mitloehner
# Distributed under the terms of the GNU General Public License
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details, in file LICENSE

from Tkinter import *
import random

# add your own CSV files here!
FILES = ("easymes.csv", "messier.csv", "urban.csv", "rascngc.csv")

def clicked(event):
  global cur, mp, score, cnt, done, curi, lcur
  if done: return 0
  (na, r, d) = dso[cur[curi]]
  drawob(na, r, d)
  (x, y) = (r2x(r), d2y(d))
  mp.create_line(x, y, event.x, event.y, fill="red")
  score += abs(x-event.x)/float(mp.winfo_width()) + abs(y-event.y)/float(mp.winfo_height()) 
  curi += 1
  if curi >= len(cur): 
    done = True
    getscore()
  else:
    lcur.config(text="Find: " + cur[curi])

def getscore():
  global score, curi, clicks, lcur
  if score < 0.1: msg = "Excellent!"
  elif score < 0.5: msg = "Good."
  elif score < 1.0: msg = "Not too bad."
  elif score < 2.0: msg = "Quite bad."
  else: msg = "Dreadful!"
  lcur.config(text=" *** Score: " + ("%.1f" % score) + "  " + msg + " ***  ")

def drawob(na, r, d):
  global mp
  x = r2x(r)
  y = d2y(d)
  dia=8
  mp.create_oval(x-dia/2, y-dia/2, x+dia/2, y+dia/2, outline="white")
  mp.create_text(x+10, y+1, anchor=W, text=na, font=("Helvetica", 8), fill="white")

def resize(event):
  drawstars()

def drawstars():
  global w, h, lra, lde, r1, r2
  mp.delete("all")
  lra.config(text="RA "+str(r1)+" to "+str(r2))
  lde.config(text="DE "+str(d1)+" to "+str(d2))
  w = mp.winfo_width()
  h = mp.winfo_height()
  cnt = 0
  for s in stars.keys():
    (r,d,m) = stars[s]
    if (not inr(r)) or d < d1 or d > d2: continue
    x = r2x(r) 
    y = d2y(d) 
    # dia = int((7.5-m)*1.0)
    if m > 4.5: dia = 2
    elif m > 3.8: dia = 2
    elif m > 2.8: dia = 3
    elif m > 1.5: dia = 4
    else: dia = 6
    mp.create_oval(x, y, x+dia, y+dia, fill="white")
    # mp.create_text(x+10, y+1, text=str(m), anchor=W, font=("Helvetica", 8), fill="white")
    cnt += 1
  # print "drawn", cnt, "stars"
  mp.pack()

def drawdso():
  for k in dso.keys():
    (na, r, d) = dso[k]
    x = r2x(r)
    y = d2y(d)
    dia=6
    mp.create_oval(x-dia/2, y-dia/2, x+dia/2, y+dia/2, outline="green")
    mp.create_text(x+10, y+1, anchor=W, text=na, font=("Helvetica", 8), fill="green")

def r2x(r):
  return (1 - float(rdif(r, r1))/(rdif(r2, r1))) * w

def d2y(d):
  return (1 - float(d - d1)/(d2 - d1)) * h

def rdif(x, y):
  if x > y: return x - y
  else: return x + 24 - y

def inr(r):
  if r2 > r1:
    return r >= r1 and r <= r2
  else:
    return r >= r1 or  r <= r2 

def readstars():
  f = open("bscmag5.csv", "r")
  for line in f:
    if line.startswith("#"): continue
    (hr,na,ra,de,mg) = line.split(",")
    (r,d) = rade(ra,de)
    stars[hr] = (r,d,float(mg))
  f.close()

def readdso(fn):
  f = open(fn, "r")
  for line in f:
    (na, r, d) = line.split(",")
    (ra, de) = rade(r, d)
    if nm.has_key(na): na = nm[na]
    if na.startswith("NGC "): na = na[4:]
    dso[na] = (na, ra, de)

def readnm():
  f = open("nm.csv", "r")
  for line in f:
    (n, m) = line.split(",")
    nm[n] = m
  f.close()

def rade(ra,de):
  (rh,rm) = ra.split(":")
  r = float(rh) + float(rm)/60
  (dh,dm) = de.split(":")
  d = float(dh) + float(dm)/60
  return (r,d)

def raplus():
  global r1, r2
  r1 = (r1 + 1) % 24
  r2 = (r2 + 1) % 24
  drawstars()

def raminus():
  global r1, r2
  r1 = (r1 - 1) % 24
  r2 = (r2 - 1) % 24
  drawstars()

def deplus():
  global d1, d2
  if d2 >= 90: return 0
  d1 += 5
  d2 += 5
  drawstars()

def deminus():
  global d1, d2
  if d1 <= -90: return 0
  d1 -= 5
  d2 -= 5
  drawstars()

def bnew():
  global cur, lcur, done, curi, score
  cur = newdso()
  lcur.config(text="Find: " + cur[0])
  curi = 0
  score = 0.0
  drawstars()
  done = False

def min(x, y):
  if x < y: return x
  else: return y

def newdso():
  lst = {}
  for o in dso.keys():
    (na, r, d) = dso[o]
    if (inr(r) and d >= d1 and d <= d2): lst[na] = 1
  return random.sample(lst.keys(), min(len(lst), 5))

def reloaddso():
  global dso
  dso = {}
  for k in dsofiles.keys():
    # print k, dsofiles[k].get()
    if dsofiles[k].get() == 1: readdso(k + ".csv")

def callback(name, index, mode):
  reloaddso()

def zoomout():
  global r1, r2, d1, d2
  if rdif(r2, r1) >= 10: return 0
  r1 = (r1 - 1) % 24
  r2 = (r2 + 1) % 24
  d1 -= 10
  d2 += 10
  drawstars()

def zoomin():
  global r1, r2, d1, d2
  if rdif(r2, r1) <= 2 or d2-d1 <= 20: return 0
  r1 = (r1 + 1) % 24
  r2 = (r2 - 1) % 24
  d1 += 10
  d2 -= 10
  drawstars()

def changeview(deg):
  global r1, r2, d1, d2
  # print "changeview", deg, deg == 360
  if deg == 25:
    r2 = (r1 + 2) % 24
    d2 = d1 + 25
  elif deg == 50:
    r2 = (r1 + 4) % 24
    (d1, d2) = (0, 50)
  elif deg == 100:
    r2 = (r1 + 8) % 24
    (d1, d2) = (-50, 50)
  elif deg == 360:
    r1 = 0
    r2 = 24
    d1 = -90
    d2 = 90
  drawstars()

def helptxt():
  showfile("README.md", "PySkyCoach Readme")

def license():
  showfile("LICENSE", "License")

def about():
  showfile("about.txt", "About")

def showfile(fn, tit):
  h = Tk()
  h.title(tit)
  s = Scrollbar(h)
  t = Text(h, height=40, width=79)
  s.pack(side=RIGHT, fill=Y)
  t.pack(side=LEFT, fill=Y)
  s.config(command=t.yview)
  t.config(yscrollcommand=s.set)
  hf = open(fn, "r")
  t.insert(END, "\n")
  for l in hf: t.insert(END, " "+l)

def main():
  global mp, r1, r2, d1, d2, lcur, cur, lra, lde, viewvar, done
  global stars, dso, dsofiles, FILES, nm
  root = Tk()
  root.title("PySkyCoach 0.1")
  stars = {}
  dso = {}
  nm = {}
  dsofiles = {}
  for f in FILES:
    (pre,post) = f.split(".")
    dsofiles[pre] = IntVar()
  readstars()
  readnm()
  dsofiles["easymes"].set(1)
  reloaddso()
  done = False
  r1, r2, d1, d2 = (14, 22, -50, 50)
  mp = Canvas(root, width=800, height=600, bg="black")
  mp.bind("<Button-1>", clicked)
  mp.bind("<Configure>", resize)
  mp.pack(fill=BOTH, expand=YES)
  pan = Frame(root)
  lra = Label(pan)
  lra.pack(side=LEFT)
  lde = Label(pan)
  lde.pack(side=LEFT)
  Button(pan, text="RA+", command=raplus).pack(side=LEFT)
  Button(pan, text="RA-", command=raminus).pack(side=LEFT)
  Button(pan, text="DE+", command=deplus).pack(side=LEFT)
  Button(pan, text="DE-", command=deminus).pack(side=LEFT)
  # Button(pan, text="Zoom out", command=zoomout).pack(side=LEFT)
  # Button(pan, text="Zoom in", command=zoomin).pack(side=LEFT)
  mb = Menu(root)
  fm = Menu(mb, tearoff=0)
  fm.add_command(label="Quit", command=root.quit)
  dm = Menu(mb, tearoff=0)
  for k in dsofiles.keys():
    traceName = dsofiles[k].trace_variable("w", callback)
    dm.add_checkbutton(label=k, onvalue=1, offvalue=0, variable=dsofiles[k])
  vm = Menu(mb, tearoff=0)
  vm.add_command(label="25 deg", command=lambda: changeview(25))
  vm.add_command(label="50 deg", command=lambda: changeview(50))
  vm.add_command(label="100 deg", command=lambda: changeview(100))
  vm.add_command(label="360 deg", command=lambda: changeview(360))
  hm = Menu(mb, tearoff=0)
  hm.add_command(label="Instructions", command=helptxt)
  hm.add_command(label="License", command=license)
  hm.add_command(label="About", command=about)
  mb.add_cascade(label="File", menu=fm)
  mb.add_cascade(label="DSO", menu=dm)
  mb.add_cascade(label="View", menu=vm)
  mb.add_cascade(label="Help", menu=hm)
  root.config(menu=mb)
  cur = newdso()
  Button(pan, text="Start Over", command=bnew).pack(side=RIGHT)
  lcur = Label(pan, text="..")
  bnew()
  lcur.pack(side=RIGHT)
  pan.pack(fill=BOTH, expand=YES)
  root.mainloop()

if __name__ == '__main__': main()
