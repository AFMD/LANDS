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

# only tested/working with solid+solid and face+face
def union(thingA,thingB,tol=1e-5):
    if (thingA.ShapeType == 'Face') and (thingB.ShapeType == 'Face'):
        u = thingA.multiFuse([thingB],tol).removeSplitter().Faces[0]
    elif (thingA.ShapeType == 'Solid') and (thingB.ShapeType == 'Solid'):
        u = thingA.multiFuse([thingB],tol).removeSplitter().Solids[0]
    else:
        u = []
    return u

# TODO: this cut is leaving breaks in circles, try to upgrade it to fuzzy logic with tolerance
# also remove splitter does nothing here
def difference(thingA,thingB):
    if (thingA.ShapeType == 'Face') and (thingB.ShapeType == 'Face'):
        d = thingA.cut(thingB).removeSplitter().Faces[0]
    elif (thingA.ShapeType == 'Solid') and (thingB.ShapeType == 'Solid'):
        d = thingA.cut(thingB).removeSplitter().Solids[0]
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
    tobj = obj.copy()
    tobj.translate(FreeCAD.Vector(direction))
    return tobj

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

# 2d first, union then extrude to 3d --> 2d section:
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

# 2d first --> extrude to 3d then union --> 2d section:
# this gives better results. boolean operations work better on 3d things
myrect = extrude(rectangle(4,3), (0,0,thickness))
myrect = translate(myrect,(0,2,0))
myrect2 = extrude(rectangle(1,10), (0,0,thickness))
circ=extrude(circle(4), (0,0,thickness))
circ2=extrude(circle(2), (0,0,thickness))

aShape = union(myrect,myrect2)
banjoOuter2D = union(aShape,circ)
banjo3D = difference(banjoOuter2D, circ2)
banjoSection = section(banjo3D)

save2DXF(banjoSection,"banjo2.dxf")
solid2STEP(banjo3D, "banjo2.step")
