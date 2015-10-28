# 0wex1 Diary

## 思路
第0周参考了太多的指南和教程，没有自己的思路，反而多走了很多弯路，这一次决定先有自己的想法，碰壁后再去寻求解决的方法。



### 根据任务概述：
* 完成一个极简交互式日记系统,需求如下:
  * 一次接收输入一行日记保存为本地文件
  * 再次运行系统时,能打印出过往的所有日记


### 目标：
1. 输入一行日记后，自动输入时间+日记（日记最重要的就是时间哪~）
2. 第一次运行创建txt文件
3. 以后每次运行，添加一条时间+日记，保存
4. 再次运行时，显示所有日记


## 写代码：
* 靠学过的[Learn Python the Hard Way Exercise 16](http://learnpythonthehardway.org/book/ex16.html)中的知识点就能解决大多数问题，还算顺利的完成了基本的框架，在Windows系统中还待解决读取txt文档显示的问题，不懂的情况下乱试了encoding/decoding，果然是没有效的...回家看看任务概述后的提示卡片，拿Mac再实验下。
* 被a+，r+，w+能否创建新的txt文件所困扰，很不优雅的解决了问题，可以在Mac上成功运行Diary.py。

### 效果：
1. 第一次运行在Diary.py所在文件夹创建diary.txt文件
2. 在“How are you?"提问后，输入日记内容
3. 以后每次运行，添加一条日记所记录时间+日记，保存
4. 再次运行时，显示所有日记，并可以再次添加日记

## 待改进：
* 去看了昨晚已经提交作业的Zoe的[小小日记](https://github.com/OpenMindClub/OMOOC2py/issues/26)
   * 自己从来没有考虑到可以用if...else或者其他逻辑设计日记的可能性哪
   * README.md是隐藏问题= =

## 改进：
在Mac中成功运行[Diary-Mac.py](https://github.com/Iris-Di/OMOOC2py/blob/master/_src/om2py0w/0wex1/Diary-Mac.py)

在Windows中成功运行[Diary-Win.py](https://github.com/Iris-Di/OMOOC2py/blob/master/_src/om2py0w/0wex1/Diary-Win.py)

## 演示1w任务
技术点：
* raw_input()
* while + break #保持输入
* os.path.exists *（没有用到）*
* open() 里的参数
* for in #回读时的循环*(不会在没有范围的情况下使用)*


看了一些教程，实在无法将W1编好的程序安放在图形界面中，只能从头开始看指南[An Introduction To Tkinter](http://effbot.org/tkinterbook/tkinter-index.htm)了。
















