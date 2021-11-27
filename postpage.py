from tkinter import *
#from ..services import postpageServices
import requests
import json

root = Tk()
root.minsize(height=500,width=900)
l = ["time","date","teamRank","teamRating"]
coutCol = 0
coutRow = 0
respone = requests.get("http://34.124.169.53:8000/api/getallposts")
temp = dict(respone.json())
#print(temp["allPosts"][0])
#print(len(temp["allPosts"]))
for i in range(len(temp["allPosts"])):
    print(i)
for i in temp["allPosts"]:
    print(i)   
#print(temp["allPosts"][0])
#label_1 = Label(root,text='eiei')
#label_1.grid(row=0,column=0)
for i in temp["allPosts"]:
    for j in l:
        label = Label(root,text=i[j])
        label.grid(row=coutRow+1,column=coutCol+1)
        coutCol += 1
    coutCol = 0
    coutRow += 1
        #print(i['time'])
        #respone
        
def show():
    for i in range(len(list)):
        myLabel = Label(root, text= list[i])
        #myLabel.pack(ipadx=20,ipady=10,side= LEFT)
        myLabel.grid(row=0,column=i)

def Next():
    respone = requests.get("http://34.124.169.53:8000/api/getallposts")
    return print(respone.text)


#label_1 = Label(root,text="This is first TAB",font=("Times_New_Roman",25))
#label_1.pack()
#button_1 = Button(root,text="NEXT",font=("Times_New_Roman",25), command=Next)
#button_1.pack()
root.mainloop()


