# -*- coding: UTF-8 -*-
import tkinter as tk
import random
import math

from graph import Graph
from line import Line

# 创建窗口数
window = tk.Tk()
window.title('离散数学-我的最爱')
window.geometry('800x900')
window.resizable(width=False, height=False)
window.iconbitmap("./icon.ico")

# 图像的设置
img = 0
cvImage = 0

# 画布的边长
canvasSide = 800

# 画出来的线的一些设置
line = Line()

# 圆圈的设置
n = 12  # 圆圈数
r = 40  # 圆圈的半径
CircleIndex = -1  # 圆圈的索引
ovalColor = '#1F6FB5'  # 圆圈的颜色
oval = [[0] * 2 for i in range(n)]  # 圆圈的数组

# 创建一个图的实例
G = Graph(n)

# 画个圆圈
def paintCircle():
    global n
    global oval
    global G
    n = int(sb.get())
    G = Graph(n)
    R = canvasSide*0.3
    oval = [[0]*2 for i in range(n)]
    deleteAll()
    for i in range(n): 
        angl = i * 2 * math.pi / n + math.pi / 2
        Ox = R * math.cos(angl) + canvasSide * 0.5
        Oy = canvasSide * 0.5 - R * math.sin(angl)

        oval[i] = [Ox,Oy]

        canvas.create_oval(
            (Ox - r, Oy - r, Ox + r, Oy + r), fill=ovalColor, width=0, tag='oval')

# 删除圆圈直线和箭头
def deleteAll():
    canvas.delete(cvImage)
    for item in canvas.find_withtag("oval"):
        canvas.delete(item)
    for item in canvas.find_withtag("line"):
        canvas.delete(item)
    for item in canvas.find_withtag("arrow"):
        canvas.delete(item)

# 画个小星星
def polygon_star(event):

    # p = 20
    # t = 5
    # x = random.randint(0+p,canvasSide-p)
    # y = random.randint(0+p,canvasSide-p)

    # points = []
    # fill='#e03636'
    # for i in (1,-1):
    #     points.extend((x,       y + i*p))
    #     points.extend((x + i*t, y + i*t))
    #     points.extend((x + i*p, y))
    #     points.extend((x + i*t, y - i * t))

    # # canvas.create_polygon(points, fill=fill, width=0)

    x = random.randint(100,canvasSide-100)
    y = random.randint(100,canvasSide-100)

    canvas.create_text(x,y,text="离散")

# 画个箭头
def drawArrow(line, eventX, eventY):
    k = 0
    p = 5
    t = 15
    x0 = (2 * eventX + line.startX) / 3
    y0 = (2 * eventY + line.startY) / 3

    points = []
    
    if (eventX == line.startX):
        points.extend((x0, y0 + t))
        points.extend((x0 - p, y0))
        points.extend((x0 + p, y0))
        line.lastArrow = canvas.create_polygon(
            points, fill=line.color, width=line.width, tag="arrow")
    else:
        diraX = (1 if eventX > line.startX else - 1)
        diraY = (1 if eventY > line.startY else - 1)

        k = math.fabs((eventY - line.startY) / (eventX - line.startX))
        m = t / (1 + k * k) ** 0.5
        n = p / (1 + k * k) ** 0.5
        points.extend((x0 + m * diraX, y0 + k * m * diraY))
        points.extend((x0 - k * n * diraX, y0 + n * diraY))
        points.extend((x0 + k * n * diraX, y0 - n * diraY))      
        line.lastArrow = canvas.create_polygon(
            points, fill=line.color, width=line.width, tag="arrow")
    
def drawLine(line, x, y):
    line.lastLine = canvas.create_line(
        line.startX, line.startY, x, y,
        fill=line.color,
        width=line.width,
        tag="line")

# 检测所点击的点所在的圆圈的索引，如果不在就返回 -1 
def checkPoint(x, y):
    global oval
    for i in range(n):
        if ((x - oval[i][0])** 2 + (y - oval[i][1])** 2 <= r**2):
            return i
    return -1

# 鼠标左键单击，允许画图
def onLeftButtonDown(event):
    global CircleIndex
    CircleIndex = checkPoint(event.x,event.y)
    if(CircleIndex >= 0):
        global line
        line.startDraw(event.x, event.y, CircleIndex)      

# 画个直线
def drawaline(event):
    # 绘制直线，先删除刚刚画过的直线，再画一条新的直线
    global line
    if(line.yesno == 1):
        if(line.lastLine): 
            canvas.delete(line.lastLine)
            canvas.delete(line.lastArrow)

            drawArrow(line,event.x,event.y)
            drawLine(line, event.x, event.y)
        else:
            drawArrow(line,event.x,event.y)
            drawLine(line, event.x, event.y)

# 鼠标左键抬起，不允许画图
def onLeftButtonUp(event):
    global CircleIndex
    global line

    CircleIndex = checkPoint(event.x, event.y)
    if (CircleIndex >= 0 ):
        # 删除之前所创建的直线和箭头
        canvas.delete(line.lastLine)
        canvas.delete(line.lastArrow)

        drawLine(line, event.x, event.y)
        line.endDraw(event.x, event.y, CircleIndex)

        drawArrow(line,event.x,event.y)
        G.martix.addEdge(line.startIndex, line.endIndex)
        line.startIndex = -1
        line.endIndex = -1
        
        G.printMartix()
    else:
        canvas.delete(line.lastLine)
        canvas.delete(line.lastArrow)
    line.yesno = 0
    line.lastLine = 0
    line.lastArrow = 0

# 判断图的类型
def judgeConet():
    global img
    global cvImage
    global n

    position = (canvasSide * 0.5, canvasSide * 0.5)

    Type = G.conetType()
    deleteAll()

    if (Type == "Strong"):
        img = tk.PhotoImage(
            file="images/s" + str(random.randint(0, 13)) + ".gif")
    elif (Type == "Unidirect"):
        img = tk.PhotoImage(
            file="images/u" + str(random.randint(0, 12)) + ".gif")
    elif (Type == "Weak"):
        img = tk.PhotoImage(
            file="images/w" + str(random.randint(0, 13)) + ".gif")
    else:
        img = tk.PhotoImage(
            file="images/q" + str(random.randint(0, 14)) + ".gif")
    
    cvImage = canvas.create_image(position, anchor='center', image=img)

# 创建 canvas 区域
canvas = tk.Canvas(window, bd=0, bg='white', relief='groove',
                   height=canvasSide+100, width=canvasSide)

canvas.bind('<Button-1>' , onLeftButtonDown)
canvas.bind('<B1-Motion>', drawaline)
canvas.bind("<Button-2>" , polygon_star)
canvas.bind('<ButtonRelease-1>', onLeftButtonUp)

# 创建 spanbox
sb = tk.Spinbox(canvas, from_=2, to=10, increment=1,
                justify="center", command=paintCircle)
# 创建按钮
bt = tk.Button(canvas, text='画完了', command=judgeConet)

canvas.create_window((canvasSide*0.5, 30), window=sb, anchor="center")
canvas.create_window((canvasSide*0.5, canvasSide-30), window=bt, anchor="center")

canvas.pack()
window.mainloop()
