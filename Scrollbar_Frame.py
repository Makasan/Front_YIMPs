from tkinter import * 
from tkinter import ttk
import requests

window_width = 1280
window_height = 720
win = Tk()
win.geometry("1280x720")
win.resizable(False,False)
win.title("YIMPS Tabs")
win['bg'] = 'gray'

wrapper1 = LabelFrame(win)
wrapper2 = LabelFrame(win)
mycanvas = Canvas(wrapper1)
mycanvas.pack(side=LEFT, fill=BOTH, expand=YES)

myScrollbar = ttk.Scrollbar(wrapper1, orient=VERTICAL, command=mycanvas.yview)
myScrollbar.pack(side=RIGHT, fill=Y)

mycanvas.config(yscrollcommand=myScrollbar.set)

mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion = mycanvas.bbox('all')))

myFrame = Frame(mycanvas)
mycanvas.create_window((0,0), window=myFrame, anchor=NW)

#wrapper1.pack(fill=BOTH, expand=YES, padx=250, pady=100)
wrapper1.place(x=250,y=210,height=350,width=900)
#wrapper2.pack(fill=BOTH, expand=YES, padx=10, pady=10)


#sortType = [ "Team Name", "Server", "Rank", "Date&Time", "Rating"]
sortType = ["rank", "date"]
l = ["time","date","teamRank","teamRating"]
start = False
respone = requests.get("http://34.124.169.53:8000/api/getallposts")
temp = dict(respone.json()) 
""" 
for i in temp["allPosts"]:
    for j in l:
        label = Label(win,text=i[j])
        label.grid(row=coutRow+1,column=coutCol+1)
        coutCol += 1
    coutCol = 0
    coutRow += 1   
   """     
def sortScrimBoard():
    respone = requests.get("http://34.124.169.53:8000/api/getposts-sorted",data={'method':str(dropdown_SortBy.get())}, headers={'Content-Type': 'application/x-www-form-urlencoded'})
    print(dropdown_SortBy.get())
    global temp
    temp = dict(respone.json()) 
    #print(temp["allPosts"])
    show_boardscrim()

def show_boardscrim():
    coutCol = 0
    coutRow = 0
    for i in temp["allPosts"]:
        label_TeamName = Label(myFrame,bg='black').grid(row=coutRow,column=coutCol,ipadx=20,ipady=10)
        coutCol += 1
        label_TeamName = Label(myFrame,text="Team Name          ",font=('Arial',12)).grid(row=coutRow,column=coutCol)
        coutCol += 1
        label_Server = Label(myFrame,text="Server          ",font=('Arial',12)).grid(row=coutRow,column=coutCol)
        coutCol += 1
        for j in l:
            label = Label(myFrame,text=i[j],font=('Arial',12))
            label.grid(row=coutRow,column=coutCol)
            coutCol += 1
            label_space = Label(myFrame,text='            ')
            label_space.grid(row=coutRow,column=coutCol)
            coutCol += 1
            #Button(myFrame, text="Button" + str(i)).pack()
        label_space = Label(myFrame,text='    ')
        label_space.grid(row=coutRow,column=coutCol)
        coutCol += 1
        Button(myFrame, text="  Request \n for Scrim" ).grid(row=coutRow,column=coutCol,pady=10,padx=10,ipadx=5,ipady=5)
        coutCol = 0
        coutRow += 1

dropdown_SortBy = StringVar()
dropdown_SortBy.set(sortType[0])
drop = OptionMenu(win, dropdown_SortBy, *sortType)
drop.place(relx=0.5,rely=0.23)
Button(win,text='Sort',font=('Arial',20),command = sortScrimBoard).place(relx=0.6,rely=0.2)

if start == False:
    show_boardscrim()
    start = True




frame_Topbar = Frame(win, width=window_width, height=70,bg='black')
frame_Topbar.place(relx=0,rely=0)
frame_Underbar = Frame(win, width=window_width, height=70,bg='black')
frame_Underbar.place(relx=0,rely=0.93)
button_Home = Button(win, text='Home Page',font=('Arial',15))
button_Home.place(x=100,y=15)
button_Scrim = Button(win, text='Scrim Board Page',font=('Arial',15))
button_Scrim.place(x=350,y=15)
button_Team = Button(win, text='Create Team Page',font=('Arial',15))
button_Team.place(x=650,y=15)
button_Profile = Button(win, text='Profile Page',font=('Arial',15))
button_Profile.place(x=1100,y=15)






win.geometry("1280x720")
win.resizable(False,False)
win.title("Scroller")
win.mainloop()