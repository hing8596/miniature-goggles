# miniature-goggles
记账还是excel最好了。但是没有满意的可以导出为相关格式的移动端程序。
目前使用iOS的Workflow记录消费添加到Evernote的笔记。(https://workflow.is/workflows/33bb0de23cbc464abe4ccd6ae1ba445e)
          格式是"[时间(ISO 860)],[名称],¥[金额]"（例“2017年4月2日 10:33,亚马逊余额充值,¥50”）
一共分了5类，就是一个笔记本下的5篇笔记。

此程序目的是将这5篇笔记的记录存入一个xlsx文件，5张表分别对应5类。

这也算是我学习python API的习作了。

使用的傻瓜和便利程度显然是和作者的水平负相关的，所以用起来还是相当的繁琐并且需要一定python基础。针对个人的分类等等习惯，自己编可能比改我的简单很多。

不过之前没有搜到关于导出Evernote笔记的文章，所以我还是发出来给需要的参考。

使用准备：
  Evernote中建好笔记本和笔记。生成自己开发者token。
  Workflow配置好，同时添加几条记录作为测试记录。
  Python配置好，包括安装好Evernote SDK.其他我用到的库包括 re和xlsxwriter
  获取要用到的笔记本guid——参见getallguids.py 
    请将源码中加上自己的token和作为账本的笔记本名称。
    运行，它会生成你所有笔记本的guid和指定笔记本下所有笔记的guid,分别保存为txt文件
    随后可以将savexlsx.py源码里的笔记本名称和guid词典手动编辑好。（因为只要做一次数量少，就不编进程序了。）
 
使用步骤
  每次需要xlsx版本的账目的时候：
  运行savexlsx.py

没了。
