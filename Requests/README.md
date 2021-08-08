# README

本文件夹主要记录了python爬虫学习过程中使用requests式爬虫的一些笔记和项目，下面分别来做一些简要的介绍。

**First Crawler：**是我写的第一个基于requests的爬虫，主要要注意的地方就是request结束了之后我们需要resp.encoding="utf-8"，否则会显示乱码出来，另外如果要进行文件操作，也要记得open后面要加上encoding的相关信息否则存进去的中文也是会出现乱码的。

就如下：

![1](\img\1.png)

![2](\img\2.png)该代码的文件操作可以见上面被注释掉的部分。

**Xpath basic以及Xpath basic2**：这两篇代码主要讲述了lxml库的etree模块的使用方法，用它来寻找html结构中的信息，学习了首先使用etree.XML或etree.HTML或etree.parse（读入一个文件）来构造一个对象的etree，这里2份Xpath代码中使用的模块主要都是etree.XML而项目文件加Grade Crawler中的同名py文件使用的是parse读入的，可以结合代码理解一下其中的一些小细节问题。

**VegetablePrice**这里是一个小的项目，主要实现了抓取北京新发地的菜价，这里有一个小技巧，就是如何通过改变传参的参数值，来获得不同的页码的不同蔬菜信息。代码值得小小研究一下，其实主要看所传参数是通过浏览器自带的F12开发者工具。

**XLSX write**：这份代码主要是做了一个测试的作用，顺便学习了一下如何用python代码写Excel文件，代码中有非常详细的注释，这里就不在做过多的解释了。

最后就是**Grade Crawler**项目文件夹了，该项目进行的非常的成功，并且也让我对requests爬虫的理解与应用更加的熟练了，其中RawSource是一个年级的没有学号只有班号的花名册，然后Test.py是用来根据这个RawSource来暴力枚举每个人的学号的然后将最后学号与姓名对应起来将数据填入花名册.xlsx文件中，然后Grade Crawler就是根据花名册中的数据来查询对应的网站，然后获得相应的成绩最后填入成绩表中。其中有大量Xpath的应用，可以好好理解一下Xpath的正确使用方法。

