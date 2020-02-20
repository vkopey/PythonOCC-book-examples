# -*- coding: utf-8 -*-
# Для виконання введіть в консолі:
# "c:\Program Files\FreeCAD 0.16\bin\python.exe" freecad_part.py
# Для виконання з довільного інтерпретатора Python введіть в консолі:
# c:\Python27\python.exe freecad_part.py

import sys
FREECADPATH = "c:\\Program Files\\FreeCAD 0.16\\bin"
sys.path.append(FREECADPATH) # шлях до бібліотек FreeCAD

import math
import FreeCAD # модуль для роботи з програмою
import FreeCADGui # модуль для роботи з GUI
App=FreeCAD
Gui=FreeCADGui
import Part # workbench-модуль для створення і керування BRep об'єктами

v1=App.Vector(0,0,0) # вектор (або точка)
v2=App.Vector(0,10,0)
v3=App.Vector(5,5,0)
l1=Part.Line(v1,v2) # лінія
a1=Part.Arc(v1,v3,v2) # дуга за трьома точками
e1=l1.toShape() # ребро
# або
#e1=Part.makeLine((0,0,0),(0,10,0)) # ребро
e2=a1.toShape() # ребро
# або
#e2=Part.makeCircle(5,App.Vector(0,5,0),App.Vector(0,0,1),-90,90)
bs=Part.BSplineCurve() # B-сплайн
bs.interpolate([(0,0,0),(0,1,1),(0,-1,2)]) # шляхом інтерполяції
# або
#bs.approximate([(0,0,0),(0,1,1),(0,-1,2)]) # шляхом апроксимації
#bs.buildFromPoles([(0,0,0),(0,1,1),(0,-1,2)]) # за списком полюсів
e3=bs.toShape() # ребро
w1=Part.Wire([e1,e2]) # цикл (сукупність ребер)
f1=Part.Face(w1) # грань
trsf=App.Matrix() # матриця трансформації
trsf.rotateZ(math.pi/4) # повернути навколо осі z
trsf.move(App.Vector(5,0,0)) # перемістити
f2=f1.copy() # копія форми
f2.transformShape(trsf) # виконати трансформацію
# або
# f2.rotate(App.Vector(0,0,0),App.Vector(0,0,1),180.0/4)
# f2.translate(App.Vector(5,0,0))
s1=f2.extrude(App.Vector(0,0,10)) # тіло шляхом видавлювання
s2=Part.Wire([e3]).makePipe(f1) # тіло шляхом видавлювання по траекторії
# або
#s2=Part.Wire([e3]).makePipeShell([w1],True,True)
s3=f1.revolve(v1,App.Vector(0,1,0),90) # тіло шляхом обертання
s2=s2.fuse(s3) # об'єднання тіл
# Див. також common, cut, oldFuse
s2=s2.removeSplitter() # видалити непотрібні ребра (refine shape)
# Див. також makeBox, makeCylinder, makeLoft, makeThickness, ...
s1=s1.makeFillet(1,[s1.Edges[1]]) # скруглення. Див. також makeChamfer

print s1.ShapeType # тип форми
print s1.Volume # об'єм. Див. також Length, Area, CenterOfMass 
print s1.distToShape(s2) # мінімальна відстань до іншої форми
print s1.Faces # список граней
print s1.Edges # список ребер
print type(s1.Edges[0].Curve) # тип кривої першого ребра
print s1.Vertexes[0].Point.x # координата x точки першої вершини

s1.exportBrep("my.brep") # експорт у форматі BREP
s1 = Part.Shape()
s1.read("my.brep") # імпорт у форматі BREP
# див. також exportStep, exportIges

##################################################################
# Наступні команди потрібні тільки для візуалізації створених форм
Gui.showMainWindow() # показати головне вікно
doc=App.newDocument() # створити новий документ
# показати форми
# doc.addObject("Part::Feature","Line").Shape=l1.toShape()
# або
Part.show(l1.toShape())
Part.show(a1.toShape())
Part.show(w1)
Part.show(f1)
Part.show(f2)
Part.show(s1)
Part.show(bs.toShape())
Part.show(s2)

doc.recompute() # перебудувати
Gui.exec_loop() # головний цикл програми