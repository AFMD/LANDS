#!/usr/bin/env python2
from __future__ import division

import sys
sys.path.append('/usr/lib/freecad') # path to your FreeCAD.so or FreeCAD.dll file
import FreeCAD

from ezFreeCAD import *

# all distances in mm

# ==== constants ====
# general
plateThickness = 10.4
majorWidth = 390
majorDepth = 440
roundsR = 10 # radius used for most rounds

# feet
footHeight = 60
littleFootWidth = 40
littleFootHeight = 20
connectorWidth = 20


def makeScrewUnion(holeLength=plateThickness,tHeight=plateThickness,tDepth=12.2,holeD=4.2,nutD=7,nutL=3.1,extraScrew=4):
    screwGrove = translate(cube(holeD,tDepth,tHeight),-holeD/2,0,0)
    nutPocket = translate(cube(nutD,nutL,tHeight),-nutD/2,extraScrew,0)
    tee = translate(union(screwGrove,nutPocket),0,-tDepth,0)
    screwUnion = union(translate(rotate(cylinder(holeD/2, holeLength),-90,0,0),0,0,tHeight/2),tee)
    return screwUnion

foot = extrude(roundedRectangle(majorWidth, footHeight,r=[0,0,roundsR,roundsR]),0,0,plateThickness)
footGap = translate(extrude(roundedRectangle(majorWidth-littleFootWidth*2, littleFootHeight,r=roundsR,ear=True),0,0,plateThickness),littleFootWidth,0,0)
foot = difference(foot,footGap)

footConnector = extrude(rectangle(connectorWidth, plateThickness), 0, 0, plateThickness)
footConnectorA = translate(footConnector, majorWidth*1/8-connectorWidth/2, footHeight, 0)
footConnectorB = translate(footConnector, majorWidth*3/8-connectorWidth/2, footHeight, 0)
footConnectorC = translate(footConnector, majorWidth*5/8-connectorWidth/2, footHeight, 0)
footConnectorD = translate(footConnector, majorWidth*7/8-connectorWidth/2, footHeight, 0)
foot = union(foot,[footConnectorA,footConnectorB,footConnectorC,footConnectorD])

screwUnion = makeScrewUnion()
screwUnionA = translate(screwUnion, majorWidth*1/4, footHeight, 0)
screwUnionB = translate(screwUnion, majorWidth*2/4, footHeight, 0)
screwUnionC = translate(screwUnion, majorWidth*3/4, footHeight, 0)

footUnit = [foot,screwUnionA,screwUnionB,screwUnionC]
solid2STEP(footUnit, "footUnit.step")
#save2DXF(difference(footUnit[0], [footUnit[1],footUnit[2],footUnit[3]]),"foot.dxf")


basePlate = extrude(roundedRectangle(majorWidth, majorDepth,r=roundsR),0,0,plateThickness)
