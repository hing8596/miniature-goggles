# EvernoteNotes2expensebook.xlsx

思路和目的
记账还是excel最好了。但是没有满意的可以导出为相关格式的移动端程序。
目前使用iOS的Workflow记录消费添加到Evernote的笔记。(https://workflow.is/workflows/33bb0de23cbc464abe4ccd6ae1ba445e)
          格式是"[时间(yyyy/MM/dd)],[名称],¥[金额]"（例“20170530,亚马逊余额充值,¥50”）

**我的保存结构是，每一类开销是一本笔记（Notes)，所有类别保存在同一个笔记本（Notebook）下，且该笔记本无其他不相干笔记**

这是也是我学习Evernote API和打包的习作。
目前最大的遗憾是并不清楚如何适应不同的环境，我自己的系统是64位的win8.1 其他版本可能会无法运行。

开发者token每次都输入其实并不方便。guid也没有必要每次都获取一遍。
但是存入txt又会增加一个“保存txt文件”的麻烦。考虑我设计也是一个月甚至几个月才需要运行一次，所以保留了每次都输入的设计。

使用：
下载exe，点击运行。
按提示输入自己的开发者token;用作账本的笔记本名称；保存的xlsx的名称。
如果workflow照搬的话，不需要其他设置。但是如果workflow中保存的格式不同，请修改源码里配套的正则。
杀毒软件可能会报警，但是你可以在这里看见源码。

各文件
ENnotes2expensexlsx_.exe是可供下载使用的可执行文件。#此步考虑放弃

ENnotes2expensexlsx_.py是其源码

getallguids2txt.py是提取全部笔记本guid和某指定笔记本内所有笔记的guid并均保存为txt文件的程序。需要自己将源码内各个参数信息填入，并且安装相关包
savexlsx.py是已知笔记本guid和笔记guid后，将笔记本内的记录提取出来保存入xlsx的。
将这两者合并，将一些参数由内置改为输入，改善对中文的支持，就是ENnotes2expensexlsx_.py了。

