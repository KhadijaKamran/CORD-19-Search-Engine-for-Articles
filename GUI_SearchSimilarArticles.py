# -*- coding: utf-8 -*-
"""
Created on Fri May 22 05:16:42 2020

@author: Khadija Kamran
"""
import pandas as pd 
import numpy as np
from tkinter import *
from scidownl.scihub import *

df = pd.read_pickle("DataFrame")
similar_1 = np.load("similar_id_1.npy")
similar_2 = np.load("similar_id_2.npy")
similar_3 = np.load("similar_id_3.npy")

def downloadPaper():
    out = 'Papers Downloaded'
    SciHub(doi_1, out).download(choose_scihub_url_index=3)
    SciHub(doi_2, out).download(choose_scihub_url_index=3)
    SciHub(doi_3, out).download(choose_scihub_url_index=3)
    SciHub(doi_4, out).download(choose_scihub_url_index=3)

    
def currentPaper(filename):
    txt = '\nInput Article: \nTitle: '
    val = df.loc[df['paper_id'] == filename] 
    txt += val['title'].values[0].replace("<br>"," ") +'\n'
    txt += 'Abstract: ' + val['abstract_summary'].values[0].replace("<br>"," ") + '\n'
    txt += 'DOI: ' + val['doi'].values[0].replace("<br>"," ") + '\n'
    txt += '\n\n Top Three Most Similar Articles:\n'
    return txt, val['doi'].values[0].replace("<br>"," "), val.index[0]

def similarPaper(index):
    txt = ''
    sim_paper = df.loc[df.index == index]
    txt += "Paper ID: " + (sim_paper['paper_id'].values[0]) 
    txt += "\nTitle: " + (sim_paper['title'].values[0].replace("<br>"," ")) 
    txt += "\nAbstract: " + (sim_paper['abstract_summary'].values[0].replace("<br>"," "))
    txt += '\nDOI: ' + (sim_paper['doi'].values[0]) +'\n'
    return txt, sim_paper['doi'].values[0]
        
#def downloadPaper(doi):
    
def showSimilar():
    global e,doi_1,doi_2,doi_3,doi_4,string
    string = e.get() 
    l1['text'] = ' '
    l2['text'] = ' '
    l3['text'] = ' '
    l4['text'] = ' '

    l1['text'],doi_1,index = currentPaper(string)
    l2['text'],doi_2 = similarPaper(similar_1[index])
    l3['text'],doi_3 = similarPaper(similar_2[index])
    l4['text'],doi_4 = similarPaper(similar_3[index])





root = Tk()
root.geometry("1200x700")
root.title('search a Similar Article')
l=Label(text="")
l.pack()
e = Entry(root,width = 50)
e.pack()
filename = e.get()
e.focus_set()

b = Button(root,text='Search Similar Articles',command=showSimilar)
b.pack()

doi_1,doi_2,doi_3,doi_4 = '','','',''
string = e.get() 

l1 = Label(root,wraplength=1200)
l2 = Label(root,wraplength=1200)

l3 = Label(root,wraplength=1200)
l4 = Label(root,wraplength=1200)
l1.pack()
l2.pack()
#b2.pack()
l3.pack()
l4.pack()
b2 = Button(root,text='Download Papers',command=downloadPaper)
b2.pack()
root.mainloop()
