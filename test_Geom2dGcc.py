# encoding: utf-8
"""Геометричні обмеження об'єктів OCC.Geom2dGcc"""
from myBaseGeom import *

from OCC.GccEnt import * # об'єкти з кваліфікаторами для створення об'єктів з геометричними обмеженнями  
from OCC.Geom2dGcc import * # алгоритми для створення об'єктів з геометричними обмеженнями для об'єктів Geom2d
from OCC.Geom2dAdaptor import * # адаптори для об'єктів Geom2d
from OCC.Precision import precision_Angular # рекомендована точність для перевірки ріності двох кутів (1e-12)

cir=gp_Circ2d(gp_Ax22d(),5) # коло радіусом 5 (OCC.gp.gp_Circ2d)
circ=GCE2d_MakeCircle(cir).Value() # коло (OCC.Geom2d.Handle_Geom2d_Circle)
ptn=gp_Pnt2d(6,4) # точка
# адаптує криву Geom2d для її використання в алгоритмах
adap=Geom2dAdaptor_Curve(circ) # адаптор кривої (OCC.Geom2dAdaptor.Geom2dAdaptor_Curve)

# Спробуйте різні кваліфікатори, щоб побачити різні результати:
# 0 - Unqualified
# 1 - Enclosing
# 2 - Enclosed
# 3 - Outside
cire=Geom2dGcc_QualifiedCurve(adap,0) # коло з кваліфікатором 0 (OCC.Geom2dGcc.Geom2dGcc_QualifiedCurve)
sol=Geom2dGcc_Lin2d2Tan(cire,ptn,precision_Angular()) # алгоритм побудови лінії через точку і яка дотична до кола
print sol.NbSolutions() # кількість розв'язків
ln=sol.ThisSolution(1) # перший розв'язок - лінія (OCC.gp.gp_Lin2d)

display.View_Top() # вид зверху
# Нарисувати фігури
for s in [circ,ptn,Geom2d_Line(ln)]:
    display.DisplayShape(s,update=True,color="black")

start_display()