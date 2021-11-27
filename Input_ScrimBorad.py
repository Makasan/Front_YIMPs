from tkinter import*
from tkcalendar import*
import requests
import json

root = Tk()
window_width = 1280  # X
window_height = 720  # Y
#root.minsize(height=window_height,width=window_width)
root.geometry("1280x720")
root.resizable(width=False,height=False)
list = ["00sssssssdsds", "01", "02", "03", "0sddddddddd4", "05", "06sdsdsdsd", "07", "08", "09"]
server_list =["SG","JP","NA","AM"]
hour_list = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09"]
for i in range(10,24): hour_list.append(i)
min_list =["00", "01", "02", "03", "04", "05", "06", "07", "08", "09"]
for i in range(10,60): min_list.append(i)
input_TeamName = Entry(root, width=15,)
input_TeamName.place(x=400,y=20)
input_TeamName.get
input_TeamName.insert(0,"Team Name")

input_2 = Entry(root, width=15,)
#input_2.pack()
input_2.place(x=610,y=20)
input_2.get
input_2.insert(0,"Rank")
input_3 = Entry(root, width=15,)
#input_3.pack()
input_3.place(x=1000,y=20)
input_3.get
input_3.insert(0,"Rating")


def add():
     
    if input_TeamName.get() != '':                           # Team Name
        myLabel = Label(root, text= input_TeamName.get())
        #myLabel.place(rely=0.1,relx=0.1)
        #myLabel.grid(row=0,column=0)
        myLabel.pack(ipadx=20,ipady=10, side= LEFT)
        list.append(input_TeamName.get())
        #input_TeamName.delete(0,END)    

    myLabel = Label(root, text=server.get())                # Server
    #myLabel.grid(row=0,column=5)
    myLabel.pack(ipadx=20,ipady=10, side= LEFT)

    if input_2.get() != '':                                 # Rank
        myLabel = Label(root, text= input_2.get())
        #myLabel.grid(row=0,column=10)
        myLabel.pack(ipadx=20,ipady=10,side= LEFT)
        list.append(input_2.get())
        #input_2.delete(0,END)


    myLabel = Label(root,text=cal.get_date())               # Date
    #myLabel.grid(row=0,column=15)
    myLabel.pack(ipadx=20,ipady=10, side= LEFT)

    myLabel = Label(root, text=hour.get())                # Time
    #myLabel.grid(row=0,column=20)
    myLabel.pack(ipadx=0,ipady=10, side= LEFT)
    myLabel = Label(root,text=":").pack(ipadx=0,ipady=10, side= LEFT)
    myLabel = Label(root, text=min.get())   
    #myLabel.grid(row=0,column=25)             
    myLabel.pack(ipadx=0,ipady=10, side= LEFT)
    

    if input_3.get() != '':
        myLabel = Label(root, text= input_3.get())
        #myLabel.grid(row=0,column=30)
        myLabel.pack(ipadx=20,ipady=10, side= LEFT)
        list.append(input_3.get())
        #input_3.delete(0,END)

    time = str(hour.get()) + ":" + str(min.get())
    print("Rank = " + str(input_2.get()))
    dict = {
    "teamRank": str(input_2.get()) , #
    "date": str(cal.get_date()) , 
    "time":  time,
    "teamRating": float(input_3.get())
    }   
    print(dict)
    #respone = requests.post("http://34.124.169.53:8000/api/createpost", data=dict, headers={'Content-Type': 'application/x-www-form-urlencoded'})
    #print(respone.text)
    
    input_TeamName.delete(0,END)
    input_2.delete(0,END)
    input_3.delete(0,END)
    #print(list)
    #temp = Label(root)
    #temp.pack(side=TOP)

    


def delete():
    input_TeamName.delete(0,END)
    input_2.delete(0,END)
    input_3.delete(0,END)


def show():
    for i in range(len(list)):
        myLabel = Label(root, text= list[i])
        #myLabel.pack(ipadx=20,ipady=10,side= LEFT)
        myLabel.grid(row=0,column=i)

def showCalendar():
    cal.place(x=820,y=200)
    getDate_button.place(x=900,y=400)

def getDate():
    getdate_Label.config(text=cal.get_date(),font=('Arial',12))
    cal.place(x=1000,y=1000)
    getDate_button.place(x=1000,y=1000)


server = StringVar()
server.set("Server")
drop_server = OptionMenu(root, server, *server_list)
drop_server.place(x=510,y=14)
hour = StringVar()
hour.set("Hr")
drop_Hr = OptionMenu(root, hour, *hour_list)
drop_Hr.place(x=850,y=14)
min = StringVar()
min.set("Min")
drop_min = OptionMenu(root, min, *min_list)
drop_min.place(x=900,y=14)


add_Button = Button(root, text="Add ! ", command=add)
add_Button.place(x=650,y=125)
delete_Button = Button(root, text="Clear ! ", command=delete)
delete_Button.place(x=650,y=160)
show_Button = Button(root, text="Show !",command = show)
show_Button.place(x=650,y=200)


cal = Calendar(root, selectmode ="day", year=2020, month=1, day=1)
#boxlabel = Frame(root,bg='pink',width=20,height=20)
#boxlabel.place(x=770,y=18)
getDate_button = Button(root, text="Confirm Date", command=getDate)
showDate_button = Button(root, text="Date", command=showCalendar)
showDate_button.place(x=720,y=14)
getdate_Label = Label(root, text="")
getdate_Label.place(x=770,y=19)



root.mainloop()