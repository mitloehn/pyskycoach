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
from math import sin, cos, pi

# add your own CSV files here!
FILES = ("easymes.csv", "messier.csv", "urban.csv", "rascngc.csv", "southbin.csv")

def clicked(event):
  global cur, mp, score, cnt, done, curi, lcur, fg
  if done: return 0
  (na, r, d) = dso[cur[curi]]
  drawob(na, r, d)
  (x, y, chk) = rd2xy(r, d)
  mp.create_line(x, y, event.x, event.y, fill="red")
  score += abs(x-event.x)/float(mp.winfo_width()) + abs(y-event.y)/float(mp.winfo_height()) 
  curi += 1
  if curi >= len(cur): 
    done = True
    getscore()
  else:
    lcur.config(text="Find: " + cur[curi])

def getscore():
  global score, lcur
  if score < 0.1: msg = "Excellent!"
  elif score < 0.5: msg = "Good."
  elif score < 1.0: msg = "Not too bad."
  elif score < 2.0: msg = "Quite bad."
  else: msg = "Dreadful!"
  lcur.config(text=" *** Score: " + ("%.1f" % score) + "  " + msg + " ***  ")

def drawob(na, r, d):
  global mp, fg
  (x, y, chk) = rd2xy(r, d)
  dia=8
  mp.create_oval(x-dia/2, y-dia/2, x+dia/2, y+dia/2, outline=fg)
  mp.create_text(x+10, y+1, anchor=W, text=na, font=("Helvetica", 8), fill=fg)

def resize(event):
  drawstars()

def drawstars():
  global w, h, lra, lde, r1, r2, d1, d2, sa, mp, fg, pv, pvde
  mp.delete("all")
  if pv == 1:
    lra.config(text="")
    lde.config(text="DE +"+str(pvde)+" to +90")
  elif pv == -1:
    lra.config(text="")
    lde.config(text="DE -"+str(pvde)+" to -90")
  else:
    lra.config(text="RA "+str(r1)+" to "+str(r2))
    lde.config(text="DE "+str(d1)+" to "+str(d2))
  w = mp.winfo_width()
  h = mp.winfo_height()
  for s in stars.keys():
    (r,d,m) = stars[s]
    (x, y, chk) = rd2xy(r, d)
    if not chk: continue
    # dia = int((7.5-m)*1.0)
    if fg == "black":
      if m > 4.5: dia = 2
      elif m > 3.8: dia = 3
      elif m > 2.8: dia = 4
      elif m > 1.5: dia = 6
      else: dia = 8
    else:
      if m > 4.5: dia = 2
      elif m > 3.8: dia = 2
      elif m > 2.8: dia = 3
      elif m > 1.5: dia = 4
      else: dia = 7
    mp.create_oval(x, y, x+dia, y+dia, fill=fg, outline=oppcol(fg))
    # mp.create_text(x+10, y+1, text=str(m), anchor=W, font=("Helvetica", 8), fill="white")
  if sa.get() == 1: drawdso()
  mp.pack()

def drawdso():
  global fg, pv, pvde
  for k in dso.keys():
    (na, r, d) = dso[k]
    (x, y, chk) = rd2xy(r, d)
    if not chk: continue
    dia=6
    mp.create_oval(x-dia/2, y-dia/2, x+dia/2, y+dia/2, outline=fg)
    mp.create_text(x+10, y+1, anchor=W, text=na, font=("Helvetica", 7), fill=fg)

def rd2xy(r, d):
  global pv # d1, d2, w, h
  if pv != 0:
    (x, y) = rd2xypv(r, d)
    chk = x >= 0 and x <= w and y >= 0 and y <= h
    return (x, y, chk)
  else:
    chk = inr(r) and d >= d1 and d <= d2
    if not chk: return (0, 0, chk)
    else: return (r2x(r), d2y(d), chk)
  # ra = 2 * pi * (24-r)/24.0
  # de = 2 * pi * (90-d)/90.0
  # ll = de
  # ww =ra
  # x = (cos(ll) * sin(ww)) / (1 + cos(ll) * cos(ww))
  # y = (sin(ll)) / (1 + cos(ll) * cos(ww))
  # f = (90 - d) / 40.0
  # x = w/2 + f * x * w/2
  # y = h/2 + f * y * h/2
  # return (x, y)

def rd2xypv(r, d):
  global pvde, pv
  rad = abs(90-d*pv)/(90-pvde)
  phi = 2 * pi * r / 24.0
  x = w/2 + rad * cos(phi) * w/2
  y = h/2 + rad * sin(phi) * h/2
  return (x, y)

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
  global dso
  f = open(fn, "r")
  for line in f:
    (na, r, d) = line.split(",")
    (ra, de) = rade(r, d)
    if nm.has_key(na): na = nm[na]
    if na.startswith("NGC "): na = na[4:]
    dso[na] = (na, ra, de)
  f.close()

def readnm():
  global nm
  f = open("nm.csv", "r")
  for line in f:
    (n, m) = line.strip().split(",")
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
  global d1, d2, pv
  if d2 >= 75: return
  d1 += 5
  d2 += 5
  drawstars()

def deminus():
  global d1, d2, pv
  if d1 <= -75: return
  d1 -= 5
  d2 -= 5
  drawstars()

def bnew():
  global cur, lcur, done, curi, score
  cur = newdso()
  if len(cur) > 0: lcur.config(text="Find: " + cur[0])
  else: lcur.config(text="No DSO")
  curi = 0
  score = 0.0
  drawstars()
  done = False

def min(x, y):
  if x < y: return x
  else: return y

def newdso():
  global pv, pvde, w, h
  lst = {}
  for o in dso.keys():
    (na, r, d) = dso[o]
    (x, y, chk) = rd2xy(r, d)
    if chk: lst[na] = 1
  return random.sample(lst.keys(), min(len(lst), 5))

def reloaddso():
  global dso
  dso = {}
  for k in dsofiles.keys():
    # print k, dsofiles[k].get()
    if dsofiles[k].get() == 1: readdso(k + ".csv")

def callback(name, index, mode):
  reloaddso()
  drawstars()

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
  global r1, r2, d1, d2, pv
  # print "changeview", deg, deg == 360
  pv = False
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
  elif deg == 1 or deg == -1:
    pv = deg
  bnew()

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

def oppcol(col):
  if col == "white": return "black"
  if col == "black": return "white"

def setfg(col):
  global mp, fg
  mp.delete("all")
  fg = col
  mp.config(bg=oppcol(fg))
  drawstars()

def main():
  global w, h, mp, r1, r2, d1, d2, lcur, cur, lra, lde, viewvar, done
  global stars, dso, dsofiles, FILES, nm, sa, fg, pv, pvde
  root = Tk()
  root.title("PySkyCoach 0.1")
  stars = {}
  dso = {}
  nm = {}
  dsofiles = {}
  for f in FILES:
    (pre,post) = f.split(".")
    dsofiles[pre] = IntVar()
  sa = IntVar()
  fg = "white"
  pv = 0
  pvde = 50.0
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
  lra = Label(root)
  lra.pack(side=LEFT)
  lde = Label(root)
  lde.pack(side=LEFT)
  Button(root, text="RA+", command=raplus).pack(side=LEFT)
  Button(root, text="RA-", command=raminus).pack(side=LEFT)
  Button(root, text="DE+", command=deplus).pack(side=LEFT)
  Button(root, text="DE-", command=deminus).pack(side=LEFT)
  # Button(pan, text="Zoom out", command=zoomout).pack(side=LEFT)
  # Button(pan, text="Zoom in", command=zoomin).pack(side=LEFT)
  mb = Menu(root)
  fm = Menu(mb, tearoff=0)
  fm.add_command(label="Quit", command=root.quit)
  dm = Menu(mb, tearoff=0)
  for k in dsofiles.keys():
    traceName = dsofiles[k].trace_variable("w", callback)
    dm.add_checkbutton(label=k, onvalue=1, offvalue=0, variable=dsofiles[k])
  sa.trace_variable("w", callback)
  dm.add_checkbutton(label="Show All", onvalue=1, offvalue=0, variable=sa)
  vm = Menu(mb, tearoff=0)
  # vm.add_command(label="25 deg", command=lambda: changeview(25))
  # vm.add_command(label="50 deg", command=lambda: changeview(50))
  vm.add_command(label="100 deg", command=lambda: changeview(100))
  vm.add_command(label="Whole Sky", command=lambda: changeview(360))
  vm.add_command(label="N Pole", command=lambda: changeview(1))
  vm.add_command(label="S Pole", command=lambda: changeview(-1))
  vm.add_command(label="White on Black", command=lambda: setfg("white"))
  vm.add_command(label="Black on White",command=lambda: setfg("black"))
  hm = Menu(mb, tearoff=0)
  hm.add_command(label="Instructions", command=helptxt)
  hm.add_command(label="License", command=license)
  hm.add_command(label="About", command=about)
  mb.add_cascade(label="File", menu=fm)
  mb.add_cascade(label="DSO", menu=dm)
  mb.add_cascade(label="View", menu=vm)
  mb.add_cascade(label="Help", menu=hm)
  root.config(menu=mb)
  w = mp.winfo_width()
  h = mp.winfo_height()
  cur = newdso()
  Button(root, text="Start Over", command=bnew).pack(side=RIGHT)
  lcur = Label(root, text="..")
  bnew()
  lcur.pack(side=RIGHT)
  root.mainloop()

if __name__ == '__main__': main()
