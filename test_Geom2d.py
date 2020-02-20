# encoding: utf-8
from myBaseGeom import *

p1=gp_Pnt2d(0,0)
p2=gp_Pnt2d(1,0)
p3=gp_Pnt2d(1,-1)
vec1=gp_Vec2d(p3,p1)
ln1=GCE2d_MakeSegment(p3,p1).Value() # відрізок (OCC.Geom2d.Handle_Geom2d_TrimmedCurve)
# перетворення об'єктів gp в об'єкти Geom2d:
ln2=Geom2d_Line(gp_Lin2d()) # лінія (OCC.Geom2d.Geom2d_Line)
arc2=GCE2d_MakeArcOfCircle(p1,vec1,p2).Value() # дуга через дві точки та дотична до vec1 в точці p1 (OCC.Geom2d.Handle_Geom2d_TrimmedCurve) 
offs1 = Geom2d_OffsetCurve(arc2, -0.1) # крива отримана шляхом зміщення OCC.Geom2d.Geom2d_OffsetCurve

display.View_Top() # вид зверху
# Нарисувати фігури
for s in [p1,p2,p3,ln1,ln2,arc2,offs1]:
    display.DisplayShape(s,color="black")
    
from OCC.GeomAPI import geomapi
arc3=geomapi.To3d(arc2 ,gp_Pln()) # перетворити 2D в 3D (OCC.Geom.Handle_Geom_Curve)
arc4=geomapi.To2d(arc3 ,gp_Pln()) # перетворити 3D в 2D (OCC.Geom2d.Handle_Geom2d_Curve)

display.FitAll()
start_display()