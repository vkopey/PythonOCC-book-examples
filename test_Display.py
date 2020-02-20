# encoding: utf-8
# Засоби для створення простого GUI
from OCC.Display.SimpleGui import *
# Функції для перегляду моделей
from OCC.Display.OCCViewer import Viewer3d

def HLR(event=None): # відповідає меню HLR
    display.View_Iso() # ізометрія
    display.SetModeHLR() # режим приховування невидимих ліній

def Shaded(event=None): # відповідає меню Shaded
    s=display.GetSelectedShape() # вибрана мишею форма
    if s: print s # надрукувати
    display.View_Front() # вид спереду
    display.SetModeShaded() # режим затінення

def WireFrame(event=None): # відповідає меню WireFrame
    display.DisableAntiAliasing() # відключити згладжування
    display.SetModeWireFrame() # режим перегляду каркасу

# об'єкти і функції для роботи з GUI          
display, start_display, add_menu, add_function_to_menu = init_display()
# display - обєкт класу OCC.Display.OCCViewer.Viewer3d
display.set_bg_gradient_color(255,255,255,255,255,255) # колір фону
#display.SetSelectionModeVertex() # вибір мишею тільки вершин
add_menu('View') # створити меню
add_function_to_menu('View',HLR) # створити підменю
add_function_to_menu('View',Shaded) # створити підменю
add_function_to_menu('View',WireFrame) # створити підменю

from OCC.BRepPrimAPI import BRepPrimAPI_MakeBox
s = BRepPrimAPI_MakeBox(10, 20, 30).Shape() # сторити форму
display.DisplayShape(s,color="black") # нарисувати форму
from OCC.gp import gp_Pnt
display.DisplayShape(gp_Pnt(),color="black") # нарисувати точку
# нарисувати текст в заданій позиції
display.DisplayMessage(gp_Pnt(-1,-1,-1),"0",message_color=(0,0,0))
display.FitAll()
start_display() # розпочати цикл обробки повідомлень