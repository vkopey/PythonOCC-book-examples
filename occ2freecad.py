# encoding: utf-8
# взаємодія FreeCAD - PythonOCC, читатння і запис файлів BRep

import sys
# додати шлях до модулів PythonOCC
sys.path.append(r"C:\Python27\Lib\site-packages")

from OCC.BRepPrimAPI import BRepPrimAPI_MakeBox
box = BRepPrimAPI_MakeBox(10., 20., 30.).Shape() # створити призму 

import Part # модуль Part FreeCAD
# передати форму в FreeCAD
# Part.__fromPythonOCC__(box) # працює не в усіх версіях PythonOCC (несумістність SWIG)

from OCC.BRepTools import breptools_Write # функція PythonOCC для запису BRep
breptools_Write(box,"box.brep") # зберегти в PythonOCC у форматі BRep
p = Part.read("box.brep") # прочитати в FreeCAD у форматі BRep
Part.show(p) # показати тіло

p.exportBrep("box.brep") # зберегти в FreeCAD у форматі BRep

from OCC.TopoDS import TopoDS_Shape
from OCC.BRep import BRep_Builder 
from OCC.BRepTools import breptools_Read # функція PythonOCC для читання BRep
base_shape = TopoDS_Shape()
builder = BRep_Builder() 
breptools_Read(base_shape, "box.brep", builder) # прочитати в PythonOCC у форматі BRep