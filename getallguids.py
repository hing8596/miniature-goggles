# -*- coding: utf-8 -*-


import sys
reload(sys) 
sys.setdefaultencoding( "utf-8" ) #避免中文乱码

from evernote.api.client import EvernoteClient
devToken = "[Enter you developer token]"  
client = EvernoteClient(token = devToken,sandbox=False)
note_store = client.get_note_store()
user_store = client.get_user_store()
from evernote.edam.notestore import NoteStore 

#file preparing
fhand1=open('booktxg.txt','w') 
txg1=[]
fhand2=open('notetxg.txt','w') 
txg2=[]

givennotebooktitle=('[enter the name of the notebooks you need]')

#save all notebooks' guid 
for notebook in note_store.listNotebooks():
    notebookName = notebook.name
    notebookGuid = notebook.guid
    txg1.append(notebookName)
    txg1.append(notebookGuid)
    txg1.append('\n')
    if notebookName ==givennotebooktitle:givennotebookGuid=notebookGuid # get the requried notebookGuid 

txg1str=' '.join(txg1)  
fhand1.write(txg1str)
fhand1.close()

#save all notes' guids in that notebook

f = NoteStore.NoteFilter()
f.notebookGuid=givennotebookGuid
#spec
spec = NoteStore.NotesMetadataResultSpec()
spec.includeTitle = True
#get notes' titleXguid
ourNoteList=note_store.findNotesMetadata(devToken,f,0,100,spec)
for  notemeta in ourNoteList.notes:
    notet=notemeta.title
    noteg=notemeta.guid
    txg2.append(notet)
    txg2.append(noteg)
    txg2.append('\n')
#save notes' guids
txg2str=' '.join(txg2)
fhand2.write(txg2str)
fhand2.close()

