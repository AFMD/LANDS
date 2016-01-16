#!/usr/bin/env python2
FREECADPATH = '/usr/lib/freecad' # path to your FreeCAD.so or FreeCAD.dll file
import sys
sys.path.append(FREECADPATH)
import FreeCAD
import Part
import importDXF
mydoc = FreeCAD.newDocument("mydoc")

def rectangle(xDim,yDim):
    return Part.makePlane(xDim,yDim)

def circle(radius):
    circEdge = Part.makeCircle(radius)
    circWire = Part.Wire(circEdge)
    circFace = Part.Face(circWire)
    return circFace

def union(thingA,thingB):
    if (thingA.ShapeType == 'Face') and (thingB.ShapeType == 'Face'):
        u = thingA.oldFuse(thingB).Faces[0]
    elif (thingA.ShapeType == 'Solid') and (thingB.ShapeType == 'Solid'):
        u = thingA.oldFuse(thingB).Solids[0]
    else:
        u = []
    return u

def difference(thingA,thingB):
    if (thingA.ShapeType == 'Face') and (thingB.ShapeType == 'Face'):
        d = thingA.cut(thingB).Faces[0]
    elif (thingA.ShapeType == 'Solid') and (thingB.ShapeType == 'Solid'):
        d = thingA.cut(thingB).Solids[0]
    else:
        d = []
    return d

def save2DXF (thing,outputFilename):
    tmpPart = mydoc.addObject("Part::Feature")
    tmpPart.Shape = thing
    importDXF.export([tmpPart], outputFilename)
    mydoc.removeObject(tmpPart.Name)
    return

def solid2STEP (solid,outputFilename):
    solid.exportStep(outputFilename)
    return

def extrude (face,direction):
    return face.extrude(FreeCAD.Vector(direction))

def translate (obj,direction):
    obj.translate(FreeCAD.Vector(direction))
    return obj

def section (solid,height="halfWay"):
    bb = solid.BoundBox
    if height == "halfWay":
        zPos = bb.ZLength/2
    else:
        zPos = height
    slicePlane = rectangle(bb.XLength, bb.YLength)
    slicePlane.translate(FreeCAD.Vector(bb.XMin,bb.YMin,zPos))
    sectionShape = solid.section(slicePlane)
    return sectionShape

myrect = rectangle(4,3)
myrect = translate(myrect,(0,2,0))
myrect2 = rectangle(1,10)
circ=circle(4)
circ2=circle(2)

aShape = union(myrect,myrect2)
banjoOuter2D = union(aShape,circ)
banjo2D = difference(banjoOuter2D, circ2)

thickness = 1;
banjo3D = extrude(banjo2D, (0,0,thickness))
banjoSection = section(banjo3D)

save2DXF(banjoSection,"banjo.dxf")
solid2STEP(banjo3D, "banjo.step")