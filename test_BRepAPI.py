# encoding: utf-8
# Топологічний API - створення стандартних топологічних обєктів, примітивів, булеві операції, скруглення

import math
from myBaseGeom import *

# Класи для моделювання і побудови чисто типологічних структур даних
from OCC.TopoDS import *   

# Пакет BRep описує топологічні структури даних BRep
# (Boundary Representation Data Structure) успадкованих від абстрактної
# топології, яка визначена в пакеті TopoDS
# Ці більш складні структури об'єнують топологічні описи з додатковою геометричною інформацією
# і включають правила оцінки еквівалентності різних можливих образів одних і тих самих об'єктів, наприклад, точок.
# from OCC.BRep import *

# Забезпечує API до топологічних структур даних BRep.
# Високорівневі і прості виклики для найбільш типових операцій - створення
# вершин, ребер, граней, тіл; операції витягування, булеві операції, розрахунок глобальних властивостей
from OCC.BRepBuilderAPI import *

p1=gp_Pnt(1, 0, 0) # точка
p2=gp_Pnt(1, 2, 0) # точка
p3=gp_Pnt(2, 1, 0) # точка

mvert1=BRepBuilderAPI_MakeVertex(p1) # створює вершину (BRepBuilderAPI_MakeVertex)
vert1=mvert1.Vertex() # вершина (TopoDS_Vertex)
# але mvert1.Shape() # форма взагалі (TopoDS_Shape)
vert2=BRepBuilderAPI_MakeVertex(p2).Vertex() # вершина (TopoDS_Vertex)

edge1=BRepBuilderAPI_MakeEdge(vert1,vert2).Edge() # ребро (TopoDS_Edge)
# BRepBuilderAPI_MakeEdge(p1,p2).Edge() # або так
arc=GC_MakeArcOfCircle(p1,p3,p2).Value() # дуга
medge2=BRepBuilderAPI_MakeEdge(arc) # створює ребро з дуги
# Більшість алгоритмів підтримують обробку помилок. Наприклад:
if medge2.IsDone(): # якщо побудова успішна
    edge2=medge2.Edge() # ребро
else: # якщо помилка
    print medge2.Error() # вивести номер помилки
    # наприклад, якщо параметри функції BRepBuilderAPI_MakeEdge будуть такі:
    # gp_Lin(),gp_Pnt(),gp_Pnt()
    # то буде істинним вираз:
    # medge2.Error()==BRepBuilderAPI_LineThroughIdenticPoints

# для розрахунку екстремумів (відстаней від форми до форми)
from OCC.BRepExtrema import BRepExtrema_ExtPC
vx=BRepBuilderAPI_MakeVertex(gp_Pnt(-2.5, 1, 0)).Vertex() # вершина
extr=BRepExtrema_ExtPC(vx,edge1) # знаходить відстані від вершини до ребра
if extr.IsDone(): # якщо екстремуми знайдені
    print "NbExt=",extr.NbExt() # кількість екстремумів
    print extr.SquareDistance(1) # квадрат відстані до першого екстремуму
    print extr.IsMin(1) # чи це мінімальна відстань?
    print extr.Parameter(1) # параметри кривої
    print extr.Point(1) # точка на кривій
    
mw=BRepBuilderAPI_MakeWire() # створює контур (BRepBuilderAPI_MakeWire)
mw.Add(edge1) # додати ребро
mw.Add(edge2) # додати ребро
wire=mw.Wire() # контур (TopoDS_Wire)

# Інструменти для структур даних BRep
from OCC.BRepTools import *
wexp=BRepTools_WireExplorer(wire) # перглядач структур TopoDS_Wire
while wexp.More(): # поки є елементи
    print wexp.Current() # поточне ребро (TopoDS_Edge)
    print wexp.CurrentVertex() # поточна вершина (TopoDS_Vertex)
    wexp.Next() # наступний елемент

# забезпечує API для створення примітивів (призм, тіл обертання, витягувань, сфер, циліндрів ...)
from OCC.BRepPrimAPI import *

face=BRepBuilderAPI_MakeFace(wire).Face() # грань (TopoDS_Face)

# дозволяє визначити положення точки відносно форми
# в даному випадку точка може бути "на границі" (в грані) і "за формою"
from OCC.BRepClass3d import BRepClass3d_SolidClassifier
sc=BRepClass3d_SolidClassifier(face,gp_Pnt(1, 1, 1),1e-6)
print "State=", sc.State() # див. OCC.TopAbs

vector=gp_Vec(p1, gp_Pnt(1, 0, 1)) # вектор
solid1 = BRepPrimAPI_MakePrism(face, vector).Shape() # призма (TopoDS_Shape)

# Ідентифікувати позицію точки відносно грані (на грані, поза гранею, на границі)
from OCC.BRepTopAdaptor import BRepTopAdaptor_FClass2d
print BRepTopAdaptor_FClass2d(face,1e-6).Perform(gp_Pnt2d(1,1)) # позиція точки (TopAbs_State)

axis=gp_Ax1(gp_Pnt(),gp_Dir(0,1,0)) # вісь Y
solid2 = BRepPrimAPI_MakeRevol(face, axis, math.pi).Shape() # тіло обертання (TopoDS_Shape)

solid3 = BRepPrimAPI_MakeBox(1, 1, 1).Shape() # призма (TopoDS_Shape)
# Див. також: 
# BRepPrimAPI_MakeCone # конус
# BRepPrimAPI_MakeCylinder # циліндр
# BRepPrimAPI_MakeSphere # сфера
# BRepPrimAPI_MakeTorus # тор
# BRepPrimAPI_MakeWedge # клиноподібне тіло

solid4=BRepBuilderAPI_Copy(solid3).Shape() # копія тіла (TopoDS_Shape)

trsf=gp_Trsf() # трансформація
trsf.SetTranslation(gp_Pnt(),gp_Pnt(0.5,0.5,0)) # переміщення
# Див. також:
# trsf.SetMirror() # дзеркальна трансформація
# trsf.SetScale() # масштабування
# trsf.SetRotation() # поворот
solid5=BRepBuilderAPI_Transform(solid4, trsf).Shape() # переміщена призма (TopoDS_Shape)

# забезпечує новий API для булевих операцій з формами (об'єднань, вирізів, перетинів)
from OCC.BRepAlgoAPI import *

solid6=BRepAlgoAPI_Fuse(solid1, solid2).Shape() # тіло після об'єднання (TopoDS_Shape)
# Див. також:
# BRepAlgoAPI_Common # спільне тіло
# BRepAlgoAPI_Cut # виріз тілом
# BRepAlgoAPI_Section # перетин

# Базові інструменти для дослідження топологічних структур даних. Наприклад, дозволяє знайти усі грані тіла
from OCC.TopExp import *

# Ресурси для топологічно орієнтованих застосувань
from OCC.TopAbs import *

# API для створення скруглень і фасок 
from OCC.BRepFilletAPI import *

# BRep_Tool забезпечує методи для доступу до геометрії BRep форм
# Наприклад, BRep_Tool_Pnt дозволяє отримати точку з вершини
from OCC.BRep import BRep_Tool_Pnt

# наступний приклад показує як зробити скруглення ребра, якщо відомі точки його вершин
pt1=gp_Pnt(1,0,0) # перша точка ребра зі скругленням
pt2=gp_Pnt(1,1,0) # друга точка ребра зі скругленням
ex = TopExp_Explorer(solid4, TopAbs_EDGE) # переглядач усіх ребер тіла
mfil=BRepFilletAPI_MakeFillet(solid4) # будівельник скруглень
while ex.More(): # поки є ще ребро
    e = topods_Edge(ex.Current()) # поточне ребро
    if e.Orientation()==0: # тілки 12 ребер куба будуть переглядатись
        # ще 12 мають зворотну орієнтацію
        fv=topexp_FirstVertex(e) # перша вершина ребра
        vp1=BRep_Tool_Pnt(fv) # точка за вершиною
        lv=topexp_LastVertex(e) # остання вершина ребра
        vp2=BRep_Tool_Pnt(lv) # точка за вершиною
        if vp1.IsEqual(pt1,1e-6) and vp2.IsEqual(pt2,1e-6): # якщо точки рівні
            mfil.Add(0.2, e) # додати скруглення до цього ребра
    ex.Next() # перейти до наступного ребра
solid7=mfil.Shape() # тіло зі скругленням (OCC.TopoDS.TopoDS_Shape)

mch=BRepFilletAPI_MakeChamfer(solid4)
ex = TopExp_Explorer(solid4, TopAbs_FACE) # переглядач усіх граней тіла
f = topods_Face(ex.Current()) # поточна грань
ex = TopExp_Explorer(solid4, TopAbs_EDGE) # переглядач усіх ребер грані
e = topods_Edge(ex.Current()) # поточне ребро
mch.Add(0.2,0.3,e,f) # додати фаску
solid8=mch.Shape() # тіло з фаскою

# API для побудови форм шляхом зміщення
from OCC.BRepOffsetAPI import *

edge3=BRepBuilderAPI_MakeEdge(gp_Pnt(),gp_Pnt(0,1,1)).Edge()
spine=BRepBuilderAPI_MakeWire(edge3).Wire()
edge4=BRepBuilderAPI_MakeEdge(gp_Circ(gp_Ax2(),0.5)).Edge()
wire2=BRepBuilderAPI_MakeWire(edge4).Wire()
profile=BRepBuilderAPI_MakeFace(wire2).Shape()
solid9=BRepOffsetAPI_MakePipe(spine,profile).Shape() # витягнути профіль вздовж траєкторії
# Див. також:
# BRepOffsetAPI_MakeThickSolid - створює тіло шляхом надання товщини поверхням
# BRepOffsetAPI_DraftAngle - уклон плоских, циліндричних і конічних граней
# BRepOffsetAPI_MakeOffset - зміщення
# BRepOffsetAPI_MakeEvolved - витягування профілю вздовж траєкторії
# BRepOffsetAPI_ThruSections - створює тіло, яке проходить через множину січень

# Алгоритми для розрахунку таких глобальних властивостей як
# довжина, площа, центр мас, об'єм, момент інерції відносно заданої осі
from OCC.GProp import GProp_GProps
# Функції для розрахунку глобальних властивостей ліній, поверхонь і тіл
from OCC.BRepGProp import brepgprop_VolumeProperties 
gpro = GProp_GProps()
brepgprop_VolumeProperties(solid9, gpro) # отримати властивості тіла
com = gpro.CentreOfMass() # центр мас
print com.X(), com.Y(), com.Z()
print gpro.Mass() # об'єм

# закоментуйте/розкоментуйте потрібні команди, щоб побачити потрібну форму
#display.DisplayShape(solid6)
#display.DisplayShape(solid7)
#display.DisplayShape(solid8)
display.DisplayShape(solid9)

display.FitAll()                            
start_display()