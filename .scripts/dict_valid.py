#!/usr/bin/python3
import os

def check_tab(l:str):
    if (l.find(" ")!=-1):
        print(l.strip())

print("invailds:")
scriptpath=os.path.dirname(__file__)
with open(scriptpath+"/../latex.dict.yaml","r") as f:
    begin_dict_q=False
    for l in f.readlines():
        if "..." in l: begin_dict_q=True;
        if begin_dict_q:
            check_tab(l)

