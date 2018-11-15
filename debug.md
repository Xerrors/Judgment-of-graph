
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

