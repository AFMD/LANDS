#!/usr/bin/env python2
from __future__ import division

import sys
sys.path.append('/usr/lib/freecad') # path to your FreeCAD.so or FreeCAD.dll file
import FreeCAD

from ezFreeCAD import *

# all distances in mm
majorWidth = 390
footHeight = 60
littleFootWidth = 40
littleFootHeight = 20
roundsR = 10 # radius used for most rounds
plateThickness = 10.4

def makeScrewUnion(holeLength=10.4,tHeight=10.4,tDepth=12.2,holeD=4.2,nutD=7,nutL=3.1,extraScrew=4):
    screwGrove = translate(cube(holeD,tDepth,tHeight),-holeD/2,0,0)
    nutPocket = translate(cube(nutD,nutL,tHeight),-nutD/2,extraScrew,0)
    tee = translate(union(screwGrove,nutPocket),0,-tDepth,0)
    screwUnion = union(translate(rotate(cylinder(holeD/2, holeLength),-90,0,0),0,0,tHeight/2),tee)
    return screwUnion

foot = extrude(roundedRectangle(majorWidth, footHeight,r=[0,0,roundsR,roundsR]),0,0,plateThickness)
footGap = translate(extrude(roundedRectangle(majorWidth-littleFootWidth*2, littleFootHeight,r=roundsR,ear=True),0,0,plateThickness),littleFootWidth,0,0)
foot = difference(foot,footGap)

solid2STEP(foot, "foot.step")
save2DXF(foot,"foot.dxf")
