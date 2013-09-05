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
import string
from math import sin, cos, pi

# add your own CSV files here!
FILES = ("messier", "rascngc", "urban", "southbin", "karkoschka")
STARFILE = "bscmag5"

def clicked(event):
  global cur, mp, score, cnt, done, curi, lcur, fg
  if done: return
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
  elif pv == -2:
    lra.config(text="RA "+str(r0))
    lde.config(text="DE "+str(d0))
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
      if STARFILE == "bscmag5":
        if   m > 4.5: dia = 2
        elif m > 3.8: dia = 2
        elif m > 2.8: dia = 3
        elif m > 1.5: dia = 5
        else:         dia = 7
      else:
        if   m > 5.5: dia = 2
        elif m > 4.5: dia = 3
        elif m > 3.8: dia = 4
        elif m > 2.8: dia = 5
        elif m > 1.5: dia = 6
        else:         dia = 8
    mp.create_oval(x, y, x+dia, y+dia, fill=fg, outline=oppcol(fg))
    # mp.create_text(x+10, y+1, text=str(m), anchor=W, font=("Helvetica", 8), fill="white")
  if sa.get() == 1: drawdso()
  if grid and pv == 0: drawgrid()
  mp.pack()

def drawdso():
  global fg, pv, pvde, INFO
  for k in dso.keys():
    (na, r, d, ty, vm, sz) = dso[k]
    (x, y, chk) = rd2xy(r, d)
    if not chk: continue
    # dia=16
    # mp.create_oval(x-dia/2, y-dia/2, x+dia/2, y+dia/2, outline=fg, dash=(2,2))
    mp.create_line(x-2, y-2, x+3, y+3, fill=fg)
    mp.create_line(x-2, y+2, x+3, y-3, fill=fg)
    mp.create_text(x+10, y+1, anchor=W, text=na, font=("Helvetica", 7), fill=fg)
    if ty != '' and INFO.get() == 1:
      mp.create_text(x+10, y+17, anchor=W, text=ty+' '+str(vm)+' '+str(sz)+"'", font=("Helvetica", 7), fill=fg)

def rd2xy(r, d):
  global pv # d1, d2, w, h
  if pv != 0:
    (x, y, chk) = rd2xypv(r, d)
    return (x, y, chk)
  else:
    chk = inr(r) and d >= d1 and d <= d2
    if not chk: return (0, 0, chk)
    else: return (r2x(r), d2y(d), chk)

def rd2xypv(r, d):
  if pv == -2:
    (lam0, phi0) = (2 * pi * r0/24.0, pi * d0/180.0)
    (lam, phi) = (2 * pi * r/24.0, pi * d/180.0)
    x = -1 * dpp * (cos(phi) * sin(lam - lam0))
    y = -1 * dpp * (cos(phi0) * sin(phi) - sin(phi0) * cos(phi) * cos(lam - lam0))
    # if angle != 0.0:
    #   x = x * cos(angle) - y * sin(angle)
    #   y = x * sin(angle) + y * cos(angle)
    x += w/2
    y += h/2
    cosc = sin(phi0) * sin(phi) + cos(phi0) * cos(phi) * cos(lam - lam0)
    chk = cosc >= 0 and x > 0 and x < w and y > 0 and y < h
  else:
    (lam, phi) = rd2rad(r, d)
    x = w/2 * (1 + lam * cos(phi))
    y = h/2 * (1 + lam * sin(phi))
    chk = x >= 0 and x <= w and y >= 0 and y <= h
  return (x, y, chk)

def rd2rad(r, d):
  rad = abs(90-d*pv)/(90.0-pvde)
  phi = 2 * pi * r / 24.0
  return (rad, phi)

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

def drawgrid():
  for i in range(r1,r1+24):
    h = (r1+i) % 24
    (x1, y1, chk) = rd2xy(h, d1)
    (x2, y2, chk) = rd2xy(h, d2)
    mp.create_line(x1, y1, x2, y2, fill=fg, dash=(1, 5))
    mp.create_text(x1, y1, anchor=S, text=str(h)+"h", font=("Helvetica", 8), fill=fg)
  for i in range(d1,d2,10):
    (x1, y1, chk) = rd2xy(r1+0.001, i+0.001)
    (x2, y2, chk) = rd2xy(r2-0.001, i+0.001)
    mp.create_line(x1, y1, x2, y2, fill=fg, dash=(1, 5))
    mp.create_text(x2, y2, anchor=W, text=str(i)+"d", font=("Helvetica", 8), fill=fg)

def readstars():
  global stars
  stars = {}
  f = open(STARFILE+".csv", "r")
  for line in f:
    if line.startswith("#"): continue
    try:
      (hr,na,ra,de,mg) = line.split(",")
      (r,d) = rade(ra,de)
      stars[hr] = (r,d,float(mg))
    except:
      # entries without visual magnitude, like novae etc
      continue
  f.close()

def readdso(fn):
  global dso
  f = open(fn, "r")
  for line in f:
    lst = line.split(",")
    if len(lst) == 3:
      (na, r, d) = lst
      (ty, vm, sz) = ('', '0', '0')
    if len(lst) == 6:
      (na, r, d, ty, vm, sz) = lst
    (ra, de) = rade(r, d)
    if nm.has_key(na): na = nm[na]
    if na.startswith("NGC "): na = na[4:]
    dso[na] = (na, ra, de, ty, vm, sz)
  f.close()

def readnm():
  global nm
  f = open("nm.csv", "r")
  for line in f:
    (n, m) = line.strip().split(",")
    nm[n] = m
  f.close()

def rade(ra,de):
  if -1 == string.find(ra, ":"):
    return (float(ra), float(de))
  (rh,rm) = ra.split(":")
  r = float(rh) + float(rm)/60
  (dh,dm) = de.split(":")
  d = float(dh) + float(dm)/60
  return (r,d)

def raplus():
  global r1, r2, r0
  r1 = (r1 + 1) % 24
  r2 = (r2 + 1) % 24
  r0 = (r0 + 1) % 24
  drawstars()

def raminus():
  global r1, r2, r0
  r1 = (r1 - 1) % 24
  r2 = (r2 - 1) % 24
  r0 = (r0 - 1) % 24
  drawstars()

def deplus():
  global d1, d2, d0
  if pv == -2:
    d0 += 5
    drawstars()
    return
  if d2 >= 90: return
  d1 += 5
  d2 += 5
  drawstars()

def deminus():
  global d1, d2, d0
  if pv == -2:
    d0 -= 5
    drawstars()
    return
  if d1 <= -90: return
  d1 -= 5
  d2 -= 5
  drawstars()

def challenge():
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
    (na, r, d, ty, vm, sz) = dso[o]
    (x, y, chk) = rd2xy(r, d)
    if chk and x > 50 and x < w-50 and y > 50 and y < h-50: lst[na] = 1
  return random.sample(lst.keys(), min(len(lst), 5))

def reloaddso():
  global dso
  dso = {}
  for k in dsofiles.keys():
    if dsofiles[k].get() == 1: readdso(k + ".csv")

def callback(name, index, mode):
  reloaddso()
  drawstars()

def zoomout():
  global r1, r2, d1, d2, dpp
  if pv == -2:
    dpp /= 1.2
    drawstars()
    return
  if rdif(r2, r1) >= 12: return 0
  r1 = (r1 - 1) % 24
  r2 = (r2 + 1) % 24
  d1 -= 10
  d2 += 10
  drawstars()

def zoomoutw(ev):
  zoomout()

def zoomin():
  global r1, r2, d1, d2, dpp
  if pv == -2:
    dpp *= 1.2
    drawstars()
    return
  if rdif(r2, r1) <= 6: return 0
  r1 = (r1 + 1) % 24
  r2 = (r2 - 1) % 24
  d1 += 10
  d2 -= 10
  drawstars()

def zoominw(ev):
  zoomin()

def rotatp():
  global angle
  angle += pi / 16
  drawstars()

def rotatm():
  global angle
  angle -= pi / 16
  drawstars()

def motion(ev):
  global lastx, lasty, r0, d0, done
  if not done: return
  if lastx != -1 and lasty != -1:
    r0 += -0.01 * (lastx - ev.x)
    d0 += -0.1 * (lasty - ev.y)
    drawstars() 
  lastx, lasty = (ev.x, ev.y)

def release(ev):
  global lastx, lasty, done
  if not done: 
    return
  lastx, lasty = (-1, -1)

def changeview(deg):
  global r1, r2, d1, d2, pv, r0, d0, dpp
  pv = False
  if deg == 50:
    r2 = (r1 + 4) % 24
    (d1, d2) = (0, 50)
  elif deg == 100:
    r2 = (r1 + 12) % 24
    (d1, d2) = (-50, 50)
  elif deg == 360:
    r1 = 0
    r2 = 24
    d1 = -90
    d2 = 90
  elif deg == 1 or deg == -1 or deg == -2:
    pv = deg
    if deg == -2: # ortho
      r0 = 19.0
      d0 = 50.0
      dpp = 500.0
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

def oppcol(col):
  if col == "white": return "black"
  if col == "black": return "white"

def setfg(col):
  global mp, fg
  mp.delete("all")
  fg = col
  mp.config(bg=oppcol(fg))
  drawstars()

def switchgrid():
  global grid
  grid = not grid
  drawstars()

def bscmag5():
  global STARFILE
  STARFILE = "bscmag5"
  readstars()
  drawstars()

def bscmag65():
  global STARFILE
  STARFILE = "bscmag65"
  readstars()
  drawstars()

def main():
  global w, h, mp, r1, r2, d1, d2, r0, d0, lcur, cur, lra, lde, viewvar, done
  global stars, dso, dsofiles, FILES, nm, sa, fg, pv, pvde, angle, grid, dpp
  global lastx, lasty, INFO
  root = Tk()
  root.title("PySkyCoach 0.1")
  stars = {}
  dso = {}
  nm = {}
  dsofiles = {}
  for f in FILES:
    dsofiles[f] = IntVar()
  sa = IntVar()
  fg = "white"
  pv = -2
  dpp = 500.0
  pvde = 50.0
  angle = 0.0
  grid = False
  lastx, lasty = (-1, -1)
  readstars()
  readnm()
  dsofiles["messier"].set(1)
  reloaddso()
  done = True
  r1, r2, d1, d2, r0, d0 = (10, 22, -50, 50, 20.0, 40.0)
  mp = Canvas(root, width=800, height=600, bg="black")
  mp.bind("<Configure>", resize)
  mp.bind("<Button-1>", clicked)
  mp.bind("<Button-4>", zoominw)
  mp.bind("<Button-5>", zoomoutw)
  mp.bind("<B1-Motion>", motion)
  mp.bind("<ButtonRelease-1>", release)
  mp.pack(fill=BOTH, expand=YES)
  lra = Label(root)
  lra.pack(side=LEFT)
  lde = Label(root)
  lde.pack(side=LEFT)
  Button(root, text="RA+", command=raplus).pack(side=LEFT)
  Button(root, text="RA-", command=raminus).pack(side=LEFT)
  Button(root, text="DE+", command=deplus).pack(side=LEFT)
  Button(root, text="DE-", command=deminus).pack(side=LEFT)
  Button(root, text="IN", command=zoomin).pack(side=LEFT)
  Button(root, text="OUT", command=zoomout).pack(side=LEFT)
  #Button(root, text="ROT+", command=rotatp).pack(side=LEFT)
  #Button(root, text="ROT-", command=rotatm).pack(side=LEFT)
  INFO = IntVar()
  mb = Menu(root)
  fm = Menu(mb, tearoff=0)
  fm.add_command(label="BSC to mag 5", command=bscmag5)
  fm.add_command(label="BSC to mag 6.5", command=bscmag65)
  fm.add_command(label="Quit", command=root.quit)
  dm = Menu(mb, tearoff=0)
  for f in FILES:
    traceName = dsofiles[f].trace_variable("w", callback)
    dm.add_checkbutton(label=f, onvalue=1, offvalue=0, variable=dsofiles[f])
  sa.trace_variable("w", callback)
  dm.add_checkbutton(label="Show DSO", onvalue=1, offvalue=0, variable=sa)
  dm.add_checkbutton(label="more info", onvalue=1, offvalue=0, variable=INFO)
  INFO.trace_variable("w", callback)
  vm = Menu(mb, tearoff=0)
  vm.add_command(label="Orthographic", command=lambda: changeview(-2))
  vm.add_command(label="100 deg/12 h", command=lambda: changeview(100))
  vm.add_command(label="360 deg/24 h", command=lambda: changeview(360))
  vm.add_command(label="N Pole", command=lambda: changeview(1))
  vm.add_command(label="S Pole", command=lambda: changeview(-1))
  vm.add_command(label="White on Black", command=lambda: setfg("white"))
  vm.add_command(label="Black on White",command=lambda: setfg("black"))
  vm.add_command(label="Grid",command=switchgrid)
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
  Button(root, text="Challenge", command=challenge).pack(side=RIGHT)
  lcur = Label(root, text="")
  lcur.pack(side=RIGHT)
  root.mainloop()

if __name__ == '__main__': main()
