# -*- coding: UTF-8 -*-

class Line():
    """表示直线的类"""

    def __init__(self):
        self.color = '#5ED5D1'
        self.startX = -1
        self.startY = -1
        self.endX = 0
        self.endY = 0
        self.startIndex = -1
        self.endIndex = -1
        self.width = 3
        self.yesno = 0
        self.lastArrow = 0
        self.lastLine = 0

    def startDraw(self, x, y, start):
        self.yesno = 1
        self.startX = x
        self.startY = y
        self.startIndex = start

    def endDraw(self, x, y, end):
        self.yesno = 0
        self.endX = x
        self.endY = y
        self.endIndex = end
