# encoding: utf-8
"""Геометричні обмеження об'єктів OCC.GccAna"""
from myBaseGeom import *

from OCC.GccEnt import gccent # об'єкти з кваліфікаторами для створення об'єктів з геометричними обмеженнями  
from OCC.GccAna import * # аналітичні алгоритми для створення об'єктів з геометричними обмеженнями для об'єктів gp

ax=gp_Ax22d() # система координат OXY
cir=gp_Circ2d(ax,5) # коло радіусом 5 (OCC.gp.gp_Circ2d)
ptn=gp_Pnt2d(7,7) # точка

cire=gccent.Outside(cir) # коло з кваліфікатором (GccEnt_QualifiedCirc)
# Спробуйте різні кваліфікатори, щоб побачити різні результати:
# Enclosing - розв'язок (лінія) повинен обводити аргумент (коло)
# Enclosed - розв'язок повинен бути обведений аргументом
# Outside - розв'язок і аргумент повинні бути назовні один до одного
# Unqualified - позиція невизначена
# Примітка: в даному випадку кваліфікатор Enclosed не допустимий
# а кваліфікатор Unqualified дає два розв'язки

sol=GccAna_Lin2d2Tan(cire, ptn, 1e-6) # алгоритм побудови лінії через точку і яка дотична до кола
print sol.NbSolutions() # кількість розв'язків
ln=sol.ThisSolution(1) # перший розв'язок - лінія (OCC.gp.gp_Lin2d)

display.View_Top() # вид зверху
# Нарисувати фігури
for s in [Geom2d_Line(ln),ptn,Geom2d_Circle(cir)]:
    display.DisplayShape(s,update=True,color="black")

start_display()