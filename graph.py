# -*- coding: UTF-8 -*-
from martix import Martix


class Graph():
    """表示图的类"""
    def __init__(self, n):
        self.martix = Martix(n)

    def conetType(self):
        """判断图的类型"""
        # 判断用户是否绘制 图
        if (self.martix.size == 12):
            return "No_Graph_Here"
        self.printMRplus()
        self.printMartix()
        result = "Strongly_Connected_Graph"
        for i in range(self.martix.size):
            for j in range(self.martix.size):
                if (self.martix.MRplus[i][j] + self.martix.MRplus[j][i] == 0 and i != j):
                    if (self.martix.judgeWCG()):
                        result = "Weakly_Connected_Graph"
                    else:
                        result = "Not_Connected_Graph"
                if (self.martix.MRplus[i][j] + self.martix.MRplus[j][i] == 1):
                    result = "Unilaterally_Connected _Graph"
        return result
    def printMartix(self):
        """按照行输出矩阵"""
        print("\nHere is your Martix ~, enjoy it ~")
        for row in self.martix.M:
            print(row)

    def printMRplus(self):
        """按照行输出可达矩阵"""
        self.martix.reachableMartix()
        print("\nHere is your reachable Martix ~, enjoy it ~")
        for row in self.martix.MRplus:
            print(row)
