# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 19:38:55 2017

@author: @tsaihsing.me
"""

#This is for exe useage


import sys
reload(sys) 
sys.setdefaultencoding( "utf-8" ) 
import re
import xlsxwriter
from evernote.api.client import EvernoteClient

devToken =raw_input("输入你的 developer token\n".decode('utf-8').encode(sys.getfilesystemencoding())) 
client = EvernoteClient(token = devToken,sandbox=False)
from evernote.edam.notestore import NoteStore 
note_store = client.get_note_store()
user_store = client.get_user_store()

givennotebooktitle=raw_input("输入存放账本的笔记本名。支持中文名\n".decode('utf-8').encode(sys.getfilesystemencoding()))
givennotebooktitle=givennotebooktitle.decode(sys.getfilesystemencoding()).encode('utf-8')

#save notebooks titles and guids
nbt2g=dict()
for notebook in note_store.listNotebooks():
    notebookName = notebook.name
    notebookGuid = notebook.guid
    nbt2g[notebookName]=notebookGuid
    if notebookName == givennotebooktitle: givennotebookGuid=notebookGuid # get the requried notebookGuid 

f = NoteStore.NoteFilter()
f.notebookGuid=givennotebookGuid
#spec
spec = NoteStore.NotesMetadataResultSpec()
spec.includeTitle = True
#get notes' titles and guids
nt2g=dict()
ourNoteList=note_store.findNotesMetadata(devToken,f,0,100,spec)
for  notemeta in ourNoteList.notes:
    notet=notemeta.title
    noteg=notemeta.guid
    nt2g[notet]=noteg 

#Save xlsx
xlsxname=raw_input("输入要保存的xlsx文件名，含后缀。支持中文  \n".decode('utf-8').encode(sys.getfilesystemencoding()))

workbook=xlsxwriter.Workbook(xlsxname)


for sort in nt2g:
    givennoteguid=nt2g[sort]
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
        goods=clear[p1+1:p2]
        fee=clear[p2:]
        
        sn.write(number,0,time)
        sn.write(number,1,goods)
        sn.write(number,2,fee)
        number=number+1
#我每一条记录的格式是： 'YYYY年MM月D日 hh:ss,名称,¥费用'（参见分享的workflow）. 
#不一样的格式可能需要重新编写上一段正则
#save xlsx
workbook.close()

print "成功".decode('utf-8').encode(sys.getfilesystemencoding())