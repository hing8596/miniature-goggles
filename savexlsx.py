# -*- coding: utf-8 -*-
#这是已经有笔记guid之后保存为xlsx的程序

import sys
reload(sys) 
sys.setdefaultencoding( "utf-8" ) 
from datetime import datetime
import time
import re #正则表达式用库
import xlsxwriter #保存xlsx用库

from evernote.api.client import EvernoteClient
devToken = "[Enter you developer token here]" #修改为自己的开发者token
client = EvernoteClient(token = devToken,sandbox=False) #沙盒同样写为Falsx
note_store = client.get_note_store()
user_store = client.get_user_store()


#请手动修改成相关笔记本题目和前一步得到的guid
notedict={'notebooktitle1':'notebookguid1',
          'notebooktitle2':'notebookguid2',
          'notebooktitle3':'notebookguid3',
          'notebooktitle4':'notebookguid4',
          'notebooktitle5':'notebookguid5'
          }

#edit xlsx
namecore=raw_input("输入文件名，支持中文等 \n 保存文件名将为 Expense[yyyyMMdd][输入内容].xlsx\n".decode('utf-8').encode(sys.getfilesystemencoding()))
nametime=time.strftime('%Y%m%d',time.localtime(time.time()))
namefull='Expensedata'+nametime+namecore+'.xlsx'

workbook=xlsxwriter.Workbook(namefull)

#set begin and end time
begin_time_str=raw_input("输入开始日期（含） \n 格式yyyymmdd".decode('utf-8').encode(sys.getfilesystemencoding()))
end_time_str=raw_input("输入结束日期（含） \n 格式yyyymmdd".decode('utf-8').encode(sys.getfilesystemencoding()))
begin_time=int(begin_time_str)
end_time=int(end_time_str)

def formtime(time_str):
    formed_y=int(time_str[:4])
    formed_m=int(time_str[5:7])
    formed_d=int(time_str[8:11])
        
    return datetime(year=formed_y,month=formed_m,day=formed_d)

for sort in notedict:
    givennoteguid=notedict[sort]
    #get useful record
    full=note_store.getNoteContent(devToken,givennoteguid)
    lst=re.findall('<div>\S+\s\S+</div>',full)
    sn=workbook.add_worksheet()
    sn.write(0,0,sort)
    sn.write(0,1,'名称')
    sn.write(0,2,'费用')
    
    number=1
    # add records of that sort
    for piece in lst:
        length=len(piece)
        end=length-6
        clear=piece[5:end]
        
        p1=clear.find(',')
        p2=clear.find('¥')
        time=clear[:p1]
        name=clear[p1+1:p2]
        fee=clear[p2:]
        
        #筛选有效和时间正确的记录
        if time.startswith('<'): continue #部分空行记录
        if time.startswith('#'): continue #允许以#排除部分记录
        if formtime(time) < begin_time: continue
        if formtime(time) > end_time:continue

        sn.write(number,0,time)
        sn.write(number,1,name)
        sn.write(number,2,fee)
        number=number+1

#save xlsx
workbook.close()
    
