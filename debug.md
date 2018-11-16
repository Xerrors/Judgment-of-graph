
# Debug 的过程
1. 过了这么久才发现我对连通图的判断是错误的，看来是需要改一下判定的原理了。
目前对连通图的判定方法是：
```python 
if (self.martix.size == 12):
            return "No_Graph_Here"
        for i in range(self.martix.size):
            for j in range(self.martix.size):
                if (self.martix.M[i][j] + self.martix.M[j][i] == 0):
                    return "Weakly_Connected_Graph"
                if (self.martix.M[i][j] + self.martix.M[j][i] == 1):
                    return "Unilaterally_Connected _Graph"
        return "Strongly_Connected_Graph"
```
即只能是这三种图的一种，但是众所周知，不是所有牛奶都叫特仑苏，也不是所有图都是连通图，所以需要更改一下判定。

第一个想法是在判断是否是强、弱、单向之前先判断是否是连通的。判断方法是判断时候有节点的入度和出度之和是 0 的。

Emmm, 大概反应30秒之后，我意识到这个算法不对，，所以，再改！

其实我是有个大概思路的，就是把邻接矩阵对称一下，然后判断可达矩阵，这个时候就能判断时候是弱连通了。

2. 对数组的复制操作

![image-20181115232622217](assets/image-20181115232622217-2295582.png)

由于在Python中，如果是对数组 A 和数组 B 进行如下操作的话，`A = B` 并不会复制一份数组，而是将 B 数组的地址赋给了 A， 对 A 进行操作修改的同时，B 的值也在发生改变。所以需要用到循环来进行赋值，如图绿色区域。