#!/usr/bin/env python2
from __future__ import division
from ezFreeCAD import *

pump2D = loadDXF("../dxf/syringePump.dxf")

standoffHeight=55
standoff = extrude(pump2D["nema23Spacer"],0,0,standoffHeight)

nema23Holes = [Part.Face(Part.Wire(edge)) for edge in pump2D["nema23Holes"]] # facify the edges from the DXF
nema23Holes = extrude(nema23Holes,0,0,standoffHeight)

standoff = difference(standoff, nema23Holes)

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

# build syringe base plate
basePlateThickness = 8 # mm for now, TODO: update this to 10 and make standoff 2mm less when they get merged
thrustBearingRecess = 5
basePlate = extrude(pump2D["basePlate"],0,0,basePlateThickness)

rodHoles = [Part.Face(Part.Wire(edge)) for edge in pump2D["slideRods"]] # facify the edges from the DXF
rodHoles = extrude(rodHoles,0,0,standoffHeight)

thrustGuide = [Part.Face(Part.Wire(edge)) for edge in pump2D["thrustGuide"]] # facify the edges from the DXF
thrustGuide = extrude(thrustGuide,0,0,thrustBearingRecess)

bearingSeat = [Part.Face(Part.Wire(edge)) for edge in pump2D["bearingSeat"]] # facify the edges from the DXF
bearingSeat = extrude(bearingSeat,0,0,standoffHeight)

basePlate = difference(basePlate, nema23Holes + rodHoles + thrustGuide + bearingSeat)
solid2STEP(basePlate, "../output/pumpBasePlate.step")
solid2STL(basePlate, "../output/pumpBasePlate.stl")

# build syringe rod guide piece
rodGuideThickness = 10
rodGuide = extrude(pump2D["rodGuide"],0,0,rodGuideThickness)

rodGuide = difference(rodGuide, nema23Holes + rodHoles)
solid2STEP(rodGuide, "../output/rodGuide.step")
solid2STL(rodGuide, "../output/rodGuide.stl")