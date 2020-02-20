# encoding: utf-8
"Побудова сплайна"
from myBaseGeom import *

from OCC.Geom2dAPI import Geom2dAPI_PointsToBSpline
# можна також використати Geom2dAPI_Interpolate
from OCC.TColgp import TColgp_Array1OfPnt2d
array = TColgp_Array1OfPnt2d(1, 5) # масив точок розміром 5
for i,p in enumerate([(0, 1),(1, 2),(2, 3),(3, 3),(4, 4)]): # для кожної точки
    array.SetValue(i+1, gp_Pnt2d(*p)) # помістити точку в масив
bspl1 = Geom2dAPI_PointsToBSpline(array).Curve() # сплайн

display.View_Top() # вид зверху
display.DisplayShape(bspl1,update=True,color='black') # показати сплайн
for i in range(array.Lower(), array.Upper()+1): # для кожної точки
    display.DisplayShape(array.Value(i),color='black',update=False) # показати точку

start_display()