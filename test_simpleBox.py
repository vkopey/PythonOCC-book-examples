# encoding: utf-8
# Найпростіший приклад
# Імпортувати функцію для створеня простого GUI
from OCC.Display.SimpleGui import init_display
display, start_display, add_menu, add_function_to_menu = init_display()

# Імпортувати функцію для створеня призми
from OCC.BRepPrimAPI import BRepPrimAPI_MakeBox
my_box = BRepPrimAPI_MakeBox(10., 20., 30.).Shape() # створити призму
display.DisplayShape(my_box,update=True) # показати призму
start_display() # цикл обробки повідомлень. Цей виклик повинен бути останнім.