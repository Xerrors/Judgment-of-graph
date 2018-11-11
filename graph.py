# -*- coding: UTF-8 -*-
from martix import Martix


class Graph():
    """表示图的类"""
    def __init__(self, n):
        self.martix = Martix(n)

    def conetType(self):
        self.printMRplus()
        if (self.martix.size == 12):
            return "No_Graph_Here"
        for i in range(self.martix.size):
            for j in range(self.martix.size):
                if (self.martix.M[i][j] + self.martix.M[j][i] == 0):
                    return "Weakly_Connected_Graph"
                if (self.martix.M[i][j] + self.martix.M[j][i] == 1):
                    return "Unilaterally_Connected _Graph"
        return "Strongly_Connected_Graph"

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
