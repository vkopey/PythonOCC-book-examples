# encoding: utf-8
# імпорт і експорт геометрії (STEP, STL)
from myBaseGeom import *

from OCC.BRepPrimAPI import BRepPrimAPI_MakeBox
solid = BRepPrimAPI_MakeBox(1, 1, 1).Shape() # призма (TopoDS_Shape)
display.DisplayShape(solid,update=True) # показати
start_display()

from OCC.STEPControl import STEPControl_Writer, STEPControl_AsIs, STEPControl_Reader
from OCC.Interface import Interface_Static_SetCVal
# ініціалізувати експортер STEP
step_writer = STEPControl_Writer() 
# AP203: проектування механізмів і загальний 3D CAD
Interface_Static_SetCVal("write.step.schema", "AP203")
step_writer.Transfer(solid, STEPControl_AsIs) # перевести форму у формат STEP
status = step_writer.Write("my.stp") # зберегти у форматі STEP

step_reader = STEPControl_Reader()
status = step_reader.ReadFile("my.stp") # прочитати з STEP
print step_reader.TransferRoot(1)
print step_reader.NbShapes()
solid = step_reader.Shape(1) 

from OCC.StlAPI import StlAPI_Writer, StlAPI_Reader
StlAPI_Writer().Write(solid, "my.stl") # зберегти в STL

from OCC.TopoDS import TopoDS_Shape
solid = TopoDS_Shape()
StlAPI_Reader().Read(solid, "my.stl") # прочитати з STL 