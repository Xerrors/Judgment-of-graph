# Judge-TKinter

## 0. 运行方法
```
python3 main.py
```

前言：前前后后、断断续续写了大约两个星期由于某些原因不想使用 QT 做界面编程，索性就使用 Python 写一个界面看一下，思来想去，选了个最古老的 Tkinter 模块；

```enviroment
编程语言 : Python 3.7.1
操作环境 : macOS High Sierra(10.13.4)
引用模块 : 
	- tkinter
	- random
	- math
```

## 1. 参考资料

- Blogs by Baidu or Google。

  ​	网络上有很多前辈已经为我们踩过了很多坑，所以我们可以站在前人的肩膀上来学习。网上大牛们写的脚本基本上比较简单，适合初学者入门。比如 CSDN 里面有一个博主，用了 几十个 例子来阐述 Canvas 的一些基本应用，只要照着做就能学到很多东西。

- [NEW MEXICO TECH](http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/index.html)

  ​	很好用的一个网站，当然了，要是先看这个再去写脚本的话，那么你放弃编程的可能性有 99.99%，内容比较古老，界面还比较丑，所以，不推荐用这个入门。这个的特点就是全，可以后期需要的时候当作字典来查。

## 2. 项目需求

​	来源自离散数学课程的期末作业，要求从选题中选取一个并实现，可以采用界面编程，有加分哦！所以我就选择了我比较喜欢的 图论 的题目。虽然难度系数是中等，并不能加很多分，但，就是喜欢，没办法！

## 3. 编程思路

- 用户界面
- 用户输入
- 判断逻辑
- 程序输出

#### 3.1 用户界面

由于是需要图形化界面，采用的是较为古老的TKinter模块。

1. 首先想到的是古老的界面以及古老的控件，所以我的设计的第一个限制就是尽量减少控件的使用。
2. 由于Tkinter的打包放置方式都不是很友好，所以我才用了在 前端开发中比较流行的 Canvas，TKinter 虽然比较古老，但是，有了 Canvas 之后，就可以通过自己的设计使界面变的相对美观一点。所以，几乎所有的图形都是通过 Canvas 进行排版和设计的。
3. 虽说是减少控件的使用，但是有些控件是不得不使用的，比如，输入框和按钮。那就只能使用这两个了，其他的就不使用了。
4. 对于需要输入邻接矩阵，我觉得如果在图形化界面里面让用户一个个的去输入邻接矩阵的话，简直就是个智障设计，所以我决定采用对用户更加友好的连线的方式来绘制图形。
5. 那么现在整体的思路就有了，在整个 TKinter 里面创建一个与窗体等大的 Canvas 。（注意：窗体的大小需要设置为不可更改，因为Canvas的组件的放置是根据坐标来的，一旦窗体设计为默认的可更改，会出现一些不可描述的Bug，所以在这个程序中设置的窗体是不可更改长宽比的。）然后在中间的区域是绘制图形的区域，会根据用户输入的节点数在一个圆圈上等间距的出现相应数量的节点，用户可以通过连线的方式构造图的边。在最下端，会出现一个按钮“画完了”当用户画完图之后，对图的类型进行判断并输出。

#### 3.2 用户输入

由于题目要求是提供一个邻接矩阵，但是我觉得让用户输入一个邻接矩阵的话也太不人性化了，所以我才用的是可视化的圆圈连线的方式来进行生成矩阵的操作。

1. 首先用户可以通过顶部的控件来修改图中节点的数量，绘制区根据节点数生成不同的数量的节点（ drawCircle() ）；
2. 然后用户可以在一个节点区域内点击并拖拽出一条直线（ drawLine() ），如果直线的末端落在另外一个节点的范围内的话，就相当于在两个节点之间添加了一个边（ addEdge() ）。同时在界面中生成所绘制的直线。这里的技术难点就在于生成的直线应该是一个有方向的箭头，而 Tkinter 中内置的箭头是在末端的，当直线绘制完毕时生成的箭头藏在节点中，并不是很容易的能够看清有向边的方向，所以在实现的时候，就在绘制直线时同时在直线的三分之二处绘制一个与直线方向相同的小箭头（ drawArrow() ）。（具体参考 line.py）
3. 经过上述操作就应该能够获得用户的输入的图的邻接矩阵了。

#### 3.3 判断逻辑

1. 首先生成改矩阵的可达矩阵，根据可达矩阵来判断图的类型。（ martix.reachableMartix() ）
2. 如果生成的可达矩阵中存在两个节点的正反两个方向均不连通则该图是弱连通图或者非连通图
   - 如果把有向边换成无向边的话，生成的可带矩阵是全部是 1 ，则该图是弱连通图
   - 否则就是 非连通图
3. 如果生成的可达矩阵中不存在两个方向均不连通的节点，而存在单向连通的节点的话，就说明这个图是单向连通图
4. 如果可达矩阵的每个值都是 1 ，则这个图是强连通图

#### 3.4 程序输出

由于是图形化界面，要是输出一个文字“强连通图”，岂不是很不好看，所以我就用了表情包的形式来输出结果，表情包共用四种类型，分别对应四种不同的图的类型，每个类型的表情包里面都有 14 个不同的表情包，当结果生成时随机显示其中的一个。另外为了照顾到不同平台的兼容性，当打开照片文件失败时，依然会输出文本提示信息。



## 4. 基本功能

1. 可以选择 2 - 10 个节点的图进行绘制
2. 绘制完成后点按按钮判断 图的类型 并输出。
    - 强连通图
    - 弱连通图
    - 单向连通图
    - 非连通图

## 5. 彩蛋（eggs）

自己找吧。。。

