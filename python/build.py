from ezFreeCAD import *

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
