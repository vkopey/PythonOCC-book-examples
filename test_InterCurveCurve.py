# encoding: utf-8
from myBaseGeom import *

from OCC.Geom2dAPI import Geom2dAPI_InterCurveCurve
ln=GCE2d_MakeLine(gp_Pnt2d(0,0),gp_Pnt2d(1,1)).Value() # лінія
cir=GCE2d_MakeCircle(gp_Pnt2d(0,0), 5).Value() # коло
inter=Geom2dAPI_InterCurveCurve(ln, cir) # алгоритм перетину двох кривих
n=inter.NbPoints() # кількість перетинів
m=inter.NbSegments() # кількість тангенційних перетинів
for i in range(1,n+1): # для кожного перетину
    p=inter.Point(i) # точка перетину
    display.DisplayShape(p,color='black') # показати точку перетину
display.View_Top() # вид зверху
display.DisplayShape(cir,color='black')
display.DisplayShape(ln,color='black')

start_display()