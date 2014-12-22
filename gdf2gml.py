from Tkinter import *
from tkMessageBox import *
import tkFileDialog
from ctypes import *

##  choose your gdf file

path = tkFileDialog.askopenfilename(
        title='Open GDF File')
print path
f = open(path)
fo=open('C:/socialnw/fgdf.txt','w')
global arr
arr=[]
try:
    for line in f:
        arr[len(arr):]=[line]
    i=1
    fo.write('graph\n')
    fo.write('[\n')
    while arr[i] != 'edgedef>node1 VARCHAR,node2 VARCHAR\n':
        string_this=arr[i].split(',')
        iden=string_this[0]
        sex=string_this[2]
        fo.write('\tnode\n')
        fo.write('\t[\n')
        fo.write('\t\tid '+iden+'\n')
        fo.write('\t\tsex "'+sex+'"\n')
        fo.write('\t]\n')
        i=i+1
    
    print i
    while i<len(arr):
        string_this=arr[i].split(',')
        iden_s=string_this[0]
        iden_t=string_this[1]
        fo.write('\tedge\n')
        fo.write('\t[\n')
        fo.write('\t\tsource '+iden_s+'\n')
        fo.write('\t\ttarget '+iden_t+'\n')
        fo.write('\t]\n')
        i=i+1
    fo.write(']\n')
    
finally:
    f.close()
    fo.close()
