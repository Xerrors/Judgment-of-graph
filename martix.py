# -*- coding: UTF-8 -*-
import random

class Martix():
    """表示矩阵的类"""

    def __init__(self,n):
        """初始化一个随机二维矩阵"""
        self.size = n
        self.M = [[0]*n for i in range(n)]

    def addEdge(self,v,w):
        """在节点 v、w 间添加一条边 v -> w """
        self.M[v][w] = 1

    def inDegree(self):
        """计算矩阵的入度"""
        inDegree = [0]*self.size
        for i in range(self.size):
            inDegree[i] =sum(self.M[i])
        return inDegree

    def outDegree(self):
        """计算矩阵的出度"""
        outDegree = [0]*self.size
        for j in range(self.size):
            for i in range(self.size):
                outDegree[j] += self.M[i][j]
        return outDegree

    def reachableMartix(self):
        """Warshall计算可达矩阵的算法"""
        A = self.M
        for i in range(self.size):
            for j in range (self.size):
                if(A[j][i]):
                    for k in range(self.size):
                        A[j][k] |= A[i][k]
        self.MRplus = A

