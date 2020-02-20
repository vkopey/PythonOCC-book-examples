# encoding: utf-8
"Ортогональна проекція точки на криву"
from myBaseGeom import *

from OCC.Geom2dAPI import Geom2dAPI_ProjectPointOnCurve
cir=GCE2d_MakeCircle(gp_Pnt2d(0,0), 5).Value() # коло
ptn=gp_Pnt2d(6,4) # точка
proj = Geom2dAPI_ProjectPointOnCurve(ptn,cir) # ортогональна проекція точки на криву
n=proj.NbPoints() # кількість проекції
for i in range(1,n+1): # для кожної проекції
    p=proj.Point(i) # точка проекції
    display.DisplayShape(p,color='black') # показати точку проекції
    dist = proj.Distance(i) # відстань від ptn до p
    display.DisplayMessage(p,"Distance: %f"%dist,message_color=(0,0,0))
print proj.NearestPoint() # найближча точка проекції
print proj.LowerDistance() # найменша відстань до проекції
display.View_Top() # вид зверху
display.DisplayShape(ptn,color='black')
display.DisplayShape(cir,color='black',update=True)

start_display()