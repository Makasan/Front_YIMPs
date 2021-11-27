from tkinter import*
from tkinter import ttk
from tkinter import font
import requests


window_width = 1280
window_height = 720
win = Tk()
win.geometry("1280x720")
win.resizable(False,False)
win.title("YIMPS Tabs")
win['bg'] = 'white'
back_ground = 'white'
myData = ["YIMPS","   JP","Bronz10"]
hour_list = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09"]
for i in range(10,24): hour_list.append(str(i))
min_list =["00", "01", "02", "03", "04", "05", "06", "07", "08", "09"]
for i in range(10,60): min_list.append(str(i))
day_list = ["01", "02", "03", "04", "05", "06", "07", "08", "09"]
for i in range(10,32): day_list.append(str(i))
month_list = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
year_list = ["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029", "2030"]
count_month = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09"]
for i in range(10,32): count_month.append(str(i))




respone = requests.get("http://34.124.169.53:8000/api/getallposts")
data_backEnd = dict(respone.json()) 

def sortScrimBoard(choice):
    choice = dropdown_SortBy.get()
    respone = requests.get("http://34.124.169.53:8000/api/getposts-sorted",data={'method':str(choice)}, headers={'Content-Type': 'application/x-www-form-urlencoded'})
    print(dropdown_SortBy.get())
    global data_backEnd
    data_backEnd = dict(respone.json()) 
    #print(data_backEnd["allPosts"])
    show_boardscrim()


def show_boardscrim():
    coutCol = 0
    coutRow = 0
    for i in range(len(data_backEnd["allPosts"])):
        clear_Label = Label(myFrame,text='                         ') #25 
        clear_Label.grid(row=coutRow+i,column=coutCol+7)
        #clear_Label.destroy()
    for i in data_backEnd["allPosts"]:
    
        label_TeamName = Label(myFrame,bg='black').grid(row=coutRow,column=coutCol,ipadx=20,ipady=10,padx=10)
        coutCol += 1
        label_TeamName = Label(myFrame,text="   Team Name          ",font=('Arial',12)).grid(row=coutRow,column=coutCol)
        coutCol += 1
        label_Server = Label(myFrame,text="Server             ",font=('Arial',12)).grid(row=coutRow,column=coutCol)
        coutCol += 1
        for j in l:
            label = Label(myFrame,text=i[j],font=('Arial',12))
            label.grid(row=coutRow,column=coutCol)
            coutCol += 1
            label_space = Label(myFrame,text='                       ')
            label_space.grid(row=coutRow,column=coutCol)
            coutCol += 1
            #Button(myFrame, text="Button" + str(i)).pack()
        #label_space = Label(myFrame,text='')
        #label_space.grid(row=coutRow,column=coutCol)
        coutCol += 1
        Button(myFrame, text="  Request \n for Scrim" ).grid(row=coutRow,column=coutCol,pady=10,padx=0,ipadx=0,ipady=5)
        coutCol = 0
        coutRow += 1

def addTeam () :
    
    coutCol = 0
    coutRow = 0
    hour = StringVar()
    hour.set("Hr")
    #drop_Hr = OptionMenu(boradAddFrame, hour, *hour_list)
    drop_Hr = ttk.Combobox(boradAddFrame, width = 3, textvariable = hour)
    drop_Hr['values'] = hour_list
    minute = StringVar()
    minute.set("Min")
    #drop_min = OptionMenu(boradAddFrame, min, *min_list)
    drop_min = ttk.Combobox(boradAddFrame, width = 3, textvariable = minute)
    drop_min['values'] = min_list

    day = StringVar()                                                       
    day.set("Day")
    drop_day = ttk.Combobox(boradAddFrame, width = 3, textvariable = day)
    drop_day['values'] = day_list
    month = StringVar()
    month.set("Month")
    drop_month = ttk.Combobox(boradAddFrame, width = 3, textvariable = month)
    drop_month['values'] = month_list
    year = StringVar()
    year.set("Year")
    drop_year = ttk.Combobox(boradAddFrame, width = 3, textvariable = year)
    drop_year['values'] = year_list
        


    boradFrame.place(x=250,y=300,height=300,width=850)
    boradAddFrame.place(x=250,y=220,height=70,width=850)
    

    emty_label = Label(myAddBorad,bg='black')
    emty_label.grid(row=coutRow,column=coutCol,ipadx=20,ipady=10,padx=10,pady=10)
    for i in range(1,3):
        emty_label = Label(myAddBorad,text=myData[i-1],font=('Arial',12))
        emty_label.grid(row=coutRow,column=coutCol+i,ipadx=20,ipady=10,padx=10,pady=10)
    emty_label = Label(boradAddFrame,text=myData[2],font=('Arial',12))
    emty_label.place(x=600,y=15,height=30,width=80)
    #drop_Hr.grid(row=coutRow,column=coutCol+2,ipadx=20,ipady=10,padx=10,pady=10)
    #drop_min.grid(row=coutRow,column=coutCol+4,ipadx=20,ipady=10,padx=10,pady=10)
    #drop_day.grid(row=coutRow,column=coutCol+5,ipadx=20,ipady=10,padx=10,pady=10)
    #drop_month.grid(row=coutRow,column=coutCol+6,ipadx=20,ipady=10,padx=10,pady=10)
    #drop_year.grid(row=coutRow,column=coutCol+7,ipadx=20,ipady=10,padx=10,pady=10)

    drop_Hr.place(x=290,y=15,height=30,width=40)
    drop_min.place(x=335,y=15,height=30,width=50)
    drop_day.place(x=400,y=15,height=30,width=50)
    drop_month.place(x=455,y=15,height=30,width=50)
    drop_year.place(x=510,y=15,height=30,width=50)
    
        ######## บัค for out of rang แล้ว แสดงผลปกติ #########
    
    # for i in range(5,7):
    #     emty_label = Label(myAddBorad,text=myData[i-1],font=('Arial',12))
    #     emty_label.grid(row=coutRow,column=coutCol+i,ipadx=20,ipady=10,padx=10,pady=10)

        ######## บัค for out of rang แล้ว แสดงผลปกติ #########
    def confirm() :
        print(count_month)
        check_error = False
        if str(month.get()) in ["01","03","05","07","08","10","12"] :  #31
            if str(day.get()) in count_month:
                warning = Label(boradAddFrame,text="Invalid date",fg='red')
                warning.place(x=420,y=45,height=20,width=100)
                check_error = True 
        elif str(month.get()) in ["02"] :  # 28
            if str(day.get()) not in count_month[0:29]:
                print("check")
                warning = Label(boradAddFrame,text="Invalid date",fg='red')
                warning.place(x=420,y=45,height=20,width=100)
                check_error = True 
        elif str(month.get()) in ["04","06","09","11"]: # 30
            if str(day.get()) not in count_month[0:31]:
                warning = Label(boradAddFrame,text="Invalid date",fg='red')
                warning.place(x=420,y=45,height=20,width=100)
                check_error = True 
        else:
            warning = Label(boradAddFrame,text="Invalid date",fg='red')
            warning.place(x=420,y=45,height=20,width=100)
            check_error = True 
        
        if check_error == False:
            time = str(hour.get()) + ":" + str(minute.get())
            date = str(day.get()) + "/" + str(month.get()) + "/" + str(year.get())
            dict = {
            "date": date , 
            "time":  time
            }
            print(dict)
            #respone = requests.post("http://34.124.169.53:8000/api/createpost", data=dict, headers={'Content-Type': 'application/x-www-form-urlencoded'})
            #print(respone.text)
            warning = Label(boradAddFrame,text="                      ")
            warning.place(x=420,y=45,height=20,width=100)
            boradFrame.place(x=250,y=210,height=350,width=850)
            boradAddFrame.place(x=1000,y=1000)
        


    def cancel() :
        warning = Label(boradAddFrame,text="                      ")
        warning.place(x=420,y=45,height=20,width=100)
        boradFrame.place(x=250,y=210,height=350,width=850)
        boradAddFrame.place(x=1000,y=1000)
    
    confirmAdd = Button(boradAddFrame,text="Comfirm",bg="pink",command=confirm)
    confirmAdd.place(x=710,y=5,height=50,width=60)
    cancelAdd = Button(boradAddFrame,text="Cancel",bg="pink",command=cancel)
    cancelAdd.place(x=780,y=5,height=50,width=60)

    # label_TeamName = Label(boradAddFrame,bg='black').grid(row=coutRow,column=coutCol,ipadx=20,ipady=10,padx=10)
    # coutCol += 1
    # label_TeamName = Label(boradAddFrame,text="   Team Name          ",font=('Arial',12)).grid(row=coutRow,column=coutCol)
    # coutCol += 1
    # label_Server = Label(boradAddFrame,text="Server          ",font=('Arial',12)).grid(row=coutRow,column=coutCol)
    # coutCol += 1
    

search_Box = Label(win,text = "Search Box",font=('Arial',15),bg=back_ground)
search_Box.place(relx=0.2,rely=0.18)
input_SearchBox = Entry(win, width=20,font=('Arial',10))
input_SearchBox.place(relx=0.2,rely=0.23)

addTeam_Button = Button(win,text="Add",command=addTeam)                                         # Add Team
addTeam_Button.place(x=1040,y=150,width=45,height=45)
showMyList_Button = Button(win,text="Show")
showMyList_Button.place(x=980,y=150,width=45,height=45)



#########################################    Test Frame ScrimBorad ####################################
boradFrame = LabelFrame(win)
mycanvas = Canvas(boradFrame)
mycanvas.pack(side=LEFT, fill=BOTH, expand=YES)
myScrollbar = ttk.Scrollbar(boradFrame, orient=VERTICAL, command=mycanvas.yview)
myScrollbar.pack(side=RIGHT, fill=Y)
mycanvas.config(yscrollcommand=myScrollbar.set)
mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion = mycanvas.bbox('all')))
myFrame = Frame(mycanvas)
mycanvas.create_window((0,0), window=myFrame, anchor=NW)
boradFrame.place(x=250,y=210,height=350,width=850)   # height 300 เหลือ 4 ทีม

boradAddFrame = LabelFrame(win)
mycanvas2 = Canvas(boradAddFrame)
mycanvas2.pack(side=LEFT, fill=BOTH, expand=YES)
myAddBorad = Frame(mycanvas2)
mycanvas2.create_window((0,0), window=myAddBorad, anchor=NW)


#wrapper1.place(x=250,y=300,height=300,width=850) 
#sortType = [ "Team Name", "Server", "Rank", "Date&Time", "Rating"]
sortType = ["rank", "date"]
l = ["time","date","teamRank"]
start = False
sortby_Label = Label(win,text = "Sort by",font=('Arial',15),bg=back_ground)                          #Sort By 
sortby_Label.place(relx=0.5,rely=0.18)
dropdown_SortBy = StringVar()
dropdown_SortBy.set(sortType[1])
drop = OptionMenu(win, dropdown_SortBy, *sortType, command=sortScrimBoard)
drop.place(relx=0.5,rely=0.23)
#Button(win,text='Sort',font=('Arial',20),command = sortScrimBoard).place(relx=0.6,rely=0.2)
adBox = Label(win, width=10, height=30, bg='black')
adBox.place(relx=0.05,rely=0.2)

if start == False:
    print("1")
    show_boardscrim()
    start = True

#########################################    Test Frame ScrimBorad ####################################






frame_Topbar = Frame(win, width=window_width, height=70,bg='black')
frame_Topbar.place(relx=0,rely=0)
frame_Underbar = Frame(win, width=window_width, height=70,bg='black')
frame_Underbar.place(relx=0,rely=0.93)

button_Home = Button(win, text='Home Page',font=('Arial',12))
button_Home.place(x=100,y=10,height=50,width=120)

label_stay = Label(win,bg='gray')
label_stay.place(x=260,y=0,height=70,width=170)
button_Scrim = Button(win, text='Scrim Board Page',font=('Arial',12))
button_Scrim.place(x=270,y=10,height=50,width=150)

button_Team = Button(win, text='Create Team Page',font=('Arial',12))
button_Team.place(x=470,y=10,height=50,width=150)
button_Profile = Button(win, text='Profile Page',font=('Arial',12))
button_Profile.place(x=1000,y=10,height=50,width=120)

logo_label = Label(win,bg='pink')
logo_label.place(x=30,y=10,height=50,width=50)



win.mainloop()