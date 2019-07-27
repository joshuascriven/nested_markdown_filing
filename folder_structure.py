#!/usr/bin/env python
# coding: utf-8

# In[100]:


import os
from pathlib import Path # for Mac + Win compatability
path0 = os.getcwd()

# Inputs
chapters = 5
chapter_prefix = "C"
sections = ["Introduction", "Theory", "Research design", "Results", "Discussion"]
sup_sec = ["Notes", "Figs", "Other", "Drafts"]

# Magic
names = [chapter_prefix+f'{i}' for i in range(1, chapters+1)]
main_sec = list(range(1,len(sections)+1))
names_all = []

for i,chapname in enumerate(names, start=1):
    names_all.append(chapname)
#     print(chapname)
    for n,sec in enumerate(zip(main_sec,sections), start=1):
#         print(chapname+"_"+str(sec[0])+"_"+sec[1])
        secname = chapname+"_"+str(sec[0])+"_"+sec[1]
        names_all.append(secname)
    for s,ssec in enumerate(sup_sec, start=1):
#         print(chapname+"_"+str(ssec))
        ssecname = chapname+"_"+str(ssec)
        names_all.append(ssecname)
        
folders = [Path(path0 +  "/" + s) for s in names_all]

for folder in folders:
    try:
        os.mkdir(folder)
    except OSError:
        print ("Creation of the directory %s failed" % folder)
    else:
        print ("Successfully created the directory %s" % folder)

for folder in names_all:
    try:
        f1=open(Path(folder+"/"+folder+"_1_.md"), "a+")
        f1.write("# "+folder+" 1")
        f2=open(Path(folder+"/"+folder+"_2_.md"), "a+")
        f2.write("# "+folder+" 2")
    except:
        print ("Creation of the file pair failed")
    else:
        print ("Successfully created file pair")

