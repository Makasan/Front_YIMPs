from tkinter import*
from tkinter import ttk
import requests


window_width = 1280
window_height = 720
win = Tk()
win.geometry("1280x720")
win.resizable(False,False)
win.title("YIMPS Tabs")
win['bg'] = 'gray'
def Main():
    def profilePage():
        profile_Page = Canvas(win, bg='red', width=window_width, height=window_height)
        profile_Page.place(x=1 , y=1)
        label_1 = Label(win, text="Profile Page", font=('Arial',30),bg='red')
        label_1.place(x=450,y=200)
        Main()
        

    def scrimBoardPage():
        
        scrimBoard_Page = Canvas(win, width=window_width, height=window_height, bg='white') ##FFE0FD
        scrimBoard_Page.place(x=1 , y=1)
        label_1 = Label(win, text="Scrim Board Page", font=('Arial',30),bg='white')
        label_1.place(x=450,y=600)
        #sortType = [ "Team Name", "Server", "Rank", "Date&Time", "Rating"]
        sortType = ["rank", "date"]
        l = Label(win,text = "Sort by",font=('Arial',15),bg="white")                          #Sort By 
        l.place(relx=0.5,rely=0.18)
        dropdown_SortBy = StringVar()
        dropdown_SortBy.set(sortType[0])
        drop = OptionMenu(win, dropdown_SortBy, *sortType)
        drop.place(relx=0.5,rely=0.23)
        #Button(win,text='Sort',font=('Arial',20),command = sort_ScrimBoard).place(relx=0.6,rely=0.2)
        #input_SortBy = Entry(root, width=20,font=('Arial',10))
        #input_SortBy.place(relx=0.5,rely=0.23)
        l = Label(win,text = "Search Box",font=('Arial',15),bg="white")
        l.place(relx=0.2,rely=0.18)
        input_SearchBox = Entry(win, width=20,font=('Arial',10))
        input_SearchBox.place(relx=0.2,rely=0.23)
        
        adBox = Label(win, width=10, height=30, bg='black')
        adBox.place(relx=0.05,rely=0.2)
        #########################################    Test Frame ScrimBorad ####################################
        wrapper1 = LabelFrame(win)
        mycanvas = Canvas(wrapper1)
        mycanvas.pack(side=LEFT, fill=BOTH, expand=YES)
        mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion = mycanvas.bbox('all')))

        myFrame = Frame(mycanvas)
        mycanvas.create_window((0,0), window=myFrame, anchor=NW)
        wrapper1.place(x=250,y=210,height=350,width=900)
        #sortType = [ "Team Name", "Server", "Rank", "Date&Time", "Rating"]
        sortType = ["rank", "date"]
        l = ["time","date","teamRank","teamRating"]
        start = False
        respone = requests.get("http://34.124.169.53:8000/api/getallposts")
        data_backEnd = dict(respone.json()) 
   
        def sortScrimBoard():
            respone = requests.get("http://34.124.169.53:8000/api/getposts-sorted",data={'method':str(dropdown_SortBy.get())}, headers={'Content-Type': 'application/x-www-form-urlencoded'})
            print(dropdown_SortBy.get())
            global data_backEnd
            data_backEnd = dict(respone.json()) 
            #print(data_backEnd["allPosts"])
            show_boardscrim()

        def show_boardscrim():
            coutCol = 0
            coutRow = 0
            for i in data_backEnd["allPosts"]:
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
            print("1")
            show_boardscrim()
            start = True

        #########################################    Test Frame ScrimBorad ####################################

        Main()

    def createTeamPage():
        createTeam_Page = Canvas(win, bg='blue', width=window_width, height=window_height)
        createTeam_Page.place(x=1 , y=1)
        label_1 = Label(win, text="Create Page",font=('Arial',30),bg='blue')
        label_1.place(x=450,y=200)
        Main()
    
    def homePage():
        home_Page = Canvas(win, bg='Pink', width=window_width, height=window_height)
        home_Page.place(x=1 , y=1)
        label_1 = Label(win, text="Home Page",font=('Arial',30),bg='Pink')
        label_1.place(x=450,y=200)
        Main()

    
    
    #c = Canvas(root, bg='black', width=width, height=height)
    #c.place(x=1 , y=20)

    frame_Topbar = Frame(win, width=window_width, height=70,bg='black')
    frame_Topbar.place(relx=0,rely=0)
    frame_Underbar = Frame(win, width=window_width, height=70,bg='black')
    frame_Underbar.place(relx=0,rely=0.93)

    
    
    #label_TopBar = Label(root,text='             ',fg='black')
    #label_TopBar.place(x=100,y=20)
    
    button_Home = Button(win, text='Home Page',font=('Arial',15),command=homePage)
    button_Home.place(x=100,y=15)

    button_Scrim = Button(win, text='Scrim Board Page',font=('Arial',15),command=scrimBoardPage)
    button_Scrim.place(x=350,y=15)

    button_Team = Button(win, text='Create Team Page',font=('Arial',15),command=createTeamPage)
    button_Team.place(x=650,y=15)

    button_Profile = Button(win, text='Profile Page',font=('Arial',15),command=profilePage)
    button_Profile.place(x=1100,y=15)
    


    
Main()
win.mainloop()