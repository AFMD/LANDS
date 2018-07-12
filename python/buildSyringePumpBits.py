#!/usr/bin/env python2
from __future__ import division
import sys
sys.path.append('/usr/lib/freecad/lib') # path to your FreeCAD.so or FreeCAD.dll file
import FreeCAD

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
basePlateThickness = 16 # mm
thrustBearingRecess = 5
basePlate = extrude(pump2D["basePlate"],0,0,basePlateThickness)

rodHoles = [Part.Face(Part.Wire(edge)) for edge in pump2D["slideRods"]] # facify the edges from the DXF
rodHoles = extrude(rodHoles,0,0,standoffHeight)

thrustGuide = [Part.Face(Part.Wire(edge)) for edge in pump2D["thrustGuide"]] # facify the edges from the DXF
thrustGuide = extrude(thrustGuide,0,0,thrustBearingRecess)

bearingSeat = [Part.Face(Part.Wire(edge)) for edge in pump2D["bearingSeat"]] # facify the edges from the DXF
bearingSeat = extrude(bearingSeat,0,0,standoffHeight)

basePlate = difference(basePlate, nema23Holes + rodHoles + thrustGuide + bearingSeat)
basePlate = translate(basePlate, 0, 0, -basePlateThickness)
solid2STEP(basePlate, "../output/pumpBasePlate.step")
solid2STL(basePlate, "../output/pumpBasePlate.stl")

# build syringe rod guide piece, this goes on the end of the motor and holds the rods
rodGuideThickness = 10
rodGuidePosition = standoffHeight + 40  #mm kind of arbitrary, just makes the full model look not smashed
rodGuide = extrude(pump2D["rodGuide"],0,0,rodGuideThickness)
rodGuide = difference(rodGuide, nema23Holes + rodHoles)

rodGuide = translate(rodGuide, 0, 0, rodGuidePosition)
solid2STEP(rodGuide, "../output/rodGuide.step")
solid2STL(rodGuide, "../output/rodGuide.stl")

# build moving plate
movingPlateThickness = 24
movingPlatePosition = -basePlateThickness - movingPlateThickness - 100
movingPlate = extrude(pump2D["movingPlate"],0,0,movingPlateThickness)

nutMounts = [Part.Face(Part.Wire(edge)) for edge in pump2D["nutMounts"]] # facify the edges from the DXF
nutMounts = extrude(nutMounts,0,0,standoffHeight)

leadscrewHole = [Part.Face(Part.Wire(edge)) for edge in pump2D["leadscrewHole"]] # facify the edges from the DXF
leadscrewHole = extrude(leadscrewHole,0,0,standoffHeight)

slideBearings = [Part.Face(Part.Wire(edge)) for edge in pump2D["slideBearings"]] # facify the edges from the DXF
slideBearings = extrude(slideBearings,0,0,standoffHeight)

movingPlate = difference(movingPlate, nutMounts + leadscrewHole + slideBearings)

movingPlate = translate(movingPlate, 0, 0, movingPlatePosition)
solid2STEP(movingPlate, "../output/movingPlate.step")
solid2STL(movingPlate, "../output/movingPlate.stl")