# Github添加Disqus评论插件

## 背景

## 安装
1. 打开[Disqus](https://disqus.com/)，注册账号，登陆
2. 点击Settings中的Add Disqus To Site
3. 点击Start Using Engage,填写Site profile

## 配置
1. 打开Gitbook网络页面，打开需要添加插件的书的编辑页面
2. 点击settings旁边的下拉菜单，在Plugins中点击Find Plugins，找到并打开[Disqus
](https://plugins.gitbook.com/plugin/disqus)
3. 由于安装Disqus时没有安装Node，尝试直接将book.json中的内容替换成：
    
        {
           "plugins": ["disqus"],
           "pluginsConfig": {
                "disqus": {
                    "ShortName": "XXXXXXX"
                }
            } 
        }
ShortName为Site profile中所填Site Name
4. 点击Plugins,其中出现Disqus,评论插件安装成功

## 使用

## 体验


