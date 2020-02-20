# encoding: utf-8
from myBaseGeom import *

p1=gp_Pnt(0,0,0) # 3D точка в декартовій системі координат
p2=gp_Pnt(1,1,0)
p3=gp_Pnt(1,0,0)
ln1=GC_MakeLine(p1,p2).Value() # лінія (OCC.Geom.Handle_Geom_Line)
ln2=GC_MakeSegment(p1,p2).Value() # відрізок (OCC.Geom.Handle_Geom_TrimmedCurve)
ln3=GC_MakeSegment(gp_Lin(),gp_Pnt(),gp_Pnt(0,0,1)).Value() # відрізок за точками на лінії
ln3=GC_MakeSegment(gp_Lin(),0,1).Value() # відрізок за двома значеннями параметра лінії
cir1=GC_MakeCircle(p1,p2,p3).Value() # коло (OCC.Geom.Handle_Geom_Circle)
cir2=Geom_Circle(gp_XOY(),1).GetHandle() # коло (OCC.Geom.Handle_Geom_Circle)
arc1=GC_MakeArcOfCircle(p1,p2,p3).Value() # дуга (OCC.Geom.Handle_Geom_TrimmedCurve)
tra1=GC_MakeTranslation(p1,p2).Value() # переміщення (OCC.Geom.Handle_Geom_Transformation)

display.View_Top() # вид зверху
# Нарисувати фігури
for s in [p1,p2,p3,ln2,cir2,arc1]:
    display.DisplayShape(s,update=True,color="black")

# перевірка успішності побудови
cir1=GC_MakeCircle(p1,p2,p3)
if cir1.IsDone(): # якщо побудова успішна
    cir1=cir1.Value() # коло
else:
    print cir1.Status() # статус помилки

start_display()