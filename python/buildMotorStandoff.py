#!/usr/bin/env python2
from __future__ import division
from ezFreeCAD import *

standoffHeight=55

pump2D = loadDXF("syringePump.dxf")
standoff = extrude(pump2D["nema23Spacer"],0,0,standoffHeight)
holes = [Part.Face(Part.Wire(edge)) for edge in pump2D["nema23Holes"]] # facify the edges from the DXF
holes = extrude(holes,0,0,standoffHeight)
standoff = difference(standoff, holes)

# make a space for the thrust bearing holder
thrustPlateL = 33.1
thrustPlateT = 5
thrustCut = rectangle (thrustPlateL, thrustPlateL)
thrustCut = extrude(thrustCut,0,0,thrustPlateT)
bb = standoff.BoundBox
thrustCut = translate(thrustCut, -thrustPlateL/2+bb.Center[0], -thrustPlateL/2+bb.Center[1], 0)
standoff = difference(standoff, thrustCut)

solid2STEP(standoff, "../output/nema23Standoff.step")
solid2STL(standoff, "../output/nema23Standoff.stl")

