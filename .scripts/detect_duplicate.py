#!/usr/bin/python3
import os
print(os.path.dirname(__file__))

scriptpath=os.path.dirname(__file__)
existing=dict()
with open(scriptpath+"/../latex.dict.yaml","r") as f:
    begin_dict_q=False
    for l in f.readlines():
        if "..." in l: 
            begin_dict_q=True
            continue;
        if begin_dict_q:
            if l[0] in existing.keys():
                print(existing[l[0]]," <=> ",l.strip())
            else:
                existing[l[0]]=l.strip()

