from tkinter import*
from tkinter import ttk
import requests


win = Tk()
win.geometry("1280x720")
win.resizable(False,False)
win.title("YIMPS Tabs")
win['bg'] = 'gray'
back_ground = 'white'
window_width = 1280
window_height = 720

""" 
dict = {
    "Team": ["Team B" , "Team C" , "Team D" , "Team E" , "Team F"],
    "date": ["17-05-2021","16-05-2021","15-05-2021","14-05-2021","13-05-2021"] , 
    "time": ["17.00","16.00","15.00","14.00","13.00"],
    "CD": ["CD","Today","1 Day","2 Day","3 Day"]
}  
""" 
dict = {
    "Team": ["VS. Team B" , "VS. Team C" , "VS. Team D" , "VS. Team E" , "VS. Team F"],
    "date": ["Date : 17-05-2021","Date : 16-05-2021","Date : 15-05-2021","Date : 14-05-2021","Date : 13-05-2021"] , 
    "time": ["Time : 17.00","Time : 16.00","Time : 15.00","Time : 14.00","Time : 13.00"],
    "CD": ["Status : CD","Status : Today","Status : 1 Day","Status : 2 Day","Status : 3 Day"]
}  


temp = Canvas(win, bg=back_ground, width=window_width, height=window_height)
temp.place(x=1 , y=1)


yourScrim_Label = Label(win, text="Your Scrim", font=('Arial',20),bg=back_ground)
yourScrim_Label.place(x=250,y=135)
incom_Label = Label(win, text="Incoming Match :  ", font=('Arial',15),bg=back_ground)
incom_Label.place(x=880,y=150)
match_Incom_Label = Label(win, text="Team B ", font=('Arial',15),bg=back_ground)
match_Incom_Label.place(x=1040,y=150)
adBox = Label(win, width=10, height=30, bg='black')
adBox.place(relx=0.05,rely=0.2)
#########################################    Test Frame Borad ####################################
wrapper1 = LabelFrame(win)
#wrapper2 = LabelFrame(win)

mycanvas = Canvas(wrapper1)
mycanvas.pack(side=LEFT, fill=BOTH, expand=YES)

""" 
yScrollbar = ttk.Scrollbar(wrapper1, orient=VERTICAL, command=mycanvas.yview)
yScrollbar.pack(side=RIGHT, fill=Y)
mycanvas.config(yscrollcommand=yScrollbar.set)
"""
mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion = mycanvas.bbox('all')))

myFrame = Frame(mycanvas)
mycanvas.create_window((0,0), window=myFrame, anchor=NW)

#wrapper1.pack(fill=BOTH, expand=YES,padx=250, pady=220)
wrapper1.place(x=250,y=180,height=370,width=870)
#wrapper2.pack(fill=BOTH, expand=YES, padx=10, pady=10)

l = ["Team","date","time","CD"]
coutCol = 0
coutRow = 0
check_VS = True
#respone = requests.get("http://34.124.169.53:8000/api/getallposts")
#temp = dict(respone.json()) 

for i in range(len(dict["Team"])):
    label_TeamName = Label(myFrame,text=("   Match "+str(i+1)+"         "),font=('Arial',12)).grid(row=coutRow,column=coutCol)
    coutCol += 1
    for j in l:
        if check_VS == False:
            label = Label(myFrame,text=("VS. " + str(dict[j][i])),font=('Arial',12))
            label.grid(row=coutRow,column=coutCol)
            check_VS = True
        else:   
            label = Label(myFrame,text=dict[j][i],font=('Arial',12))
            label.grid(row=coutRow,column=coutCol,pady=25,padx=20)
        coutCol += 1
        label_space = Label(myFrame,text='            ')
        label_space.grid(row=coutRow,column=coutCol)
        coutCol += 1
        #Button(myFrame, text="Button" + str(i)).pack()
    label_space = Label(myFrame,text='    ')
    label_space.grid(row=coutRow,column=coutCol)
    coutCol += 1
    #Button(myFrame, text="  Request \n for Scrim" ).grid(row=coutRow,column=coutCol,pady=10,padx=10,ipadx=5,ipady=5)

    coutCol = 0
    coutRow += 1
    #check_VS = False

#Button(myFrame, text="  Request \n for Scrim" ).grid(row=coutRow+4,column=coutCol+12,pady=10,padx=10,ipadx=5,ipady=5)
    
#########################################    Test Frame Borad ####################################

frame_Topbar = Frame(win, width=window_width, height=70,bg='black')
frame_Topbar.place(relx=0,rely=0)
frame_Underbar = Frame(win, width=window_width, height=70,bg='black')
frame_Underbar.place(relx=0,rely=0.93)

label_stay = Label(win,bg='gray')
label_stay.place(x=89,y=0,height=70,width=140)
button_Home = Button(win, text='Home Page',font=('Arial',12))
button_Home.place(x=100,y=10,height=50,width=120)

button_Scrim = Button(win, text='Scrim Board Page',font=('Arial',12)) 
button_Scrim.place(x=270,y=10,height=50,width=150)
button_Team = Button(win, text='Create Team Page',font=('Arial',12))
button_Team.place(x=470,y=10,height=50,width=150)
button_Profile = Button(win, text='Profile Page',font=('Arial',12))
button_Profile.place(x=1000,y=10,height=50,width=120)

logo_label = Label(win,bg='pink')
logo_label.place(x=25,y=10,height=50,width=50)




#win.wm_attributes("-transparentcolor", 'grey')
win.mainloop()