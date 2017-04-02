#这是已经有笔记guid之后保存为xlsx的程序

import sys
reload(sys) 
sys.setdefaultencoding( "utf-8" ) 

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
workbook=xlsxwriter.Workbook('Expenses.xlsx')


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
        end=length-7
        clear=piece[5:end]
        
        p1=clear.find(',')
        p2=clear.find('¥')
        time=clear[:p1]
        name=clear[p1+1:p2]
        fee=clear[p2:]
        
        sn.write(number,0,time)
        sn.write(number,1,name)
        sn.write(number,2,fee)
        number=number+1

#save xlsx
workbook.close()
    
