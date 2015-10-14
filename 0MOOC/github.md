# Github与Gitbook的联动

## 背景

## 安装

1.创建新书


      如需在Gitbook中创建新书并与Github中的Respository关联

          在Gitbook中create a new book

      如需通过Gitbook中Fork已存在Respository创建新书

          点击create a new book后，在GITHUB而不是BASIC中输入Title，并选择需要对应的GithubID/Repo

2.点击书名进入新书，在settings的Github中，根据[the GitHub integration](https://help.gitbook.com/github/index.html)及操作提示完成对Github Repository的设置后保存。

3.在Integration中Add webhook后保存。

4.点击Export to Github，Check需要在Github中import的Gitbook的URL，创建新的GitbubID/Repo,并将其设为Public。

      如关联不成功，在Gitbook-settings-Gitbub中，可以检查Github账号是否允许与私人
      或公共账号关联，webhook是否能够把Gitbook的变动push到关联的Repo，更改错误。

## 配置

## 使用

## 体验
用半小时完成了安装，用半天写完了教程。在写教程的过程中无数次对自己的智商和记忆产生怀疑，把安装时没碰到的歪路都走了一遍，最终以创建test.git实验一个repo通过2个webhook push 2本book才清楚了之前没踩坑的原因，写教案是个苦差事，小白还在继续探索中。
