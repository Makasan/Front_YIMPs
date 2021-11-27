from tkinter import*
from tkinter import ttk
from PIL import ImageTk, Image
import requests

window_width = 1280
window_height = 720
win = Tk()
win.geometry("1280x720")
win.resizable(False,False)
win.title("YIMPS Tabs")
win['bg'] = 'pink'
back_ground = 'white'
uID = ["Makasan","Gold2","YIMPS"]

image = Image.open("Makasan.png")
profile_Image = ImageTk.PhotoImage(image.resize((300, 300)))




profileFrame = LabelFrame(win,bg="black",border=10)
my_profile = Canvas(profileFrame,bg=back_ground)
my_profile.pack(side=LEFT, fill=BOTH, expand=YES)
myFrame = Frame(my_profile)
my_profile.create_window((0,0), window=myFrame, anchor=NW)
profileFrame.place(x=150,y=110,height=520,width=1000)
line_label = Label(profileFrame,bg="gray")
line_label.place(relx=0.5,rely=0,relheight=1,relwidth=0.01)




myProfile_Label = Label(profileFrame, image= profile_Image,bg=back_ground)
myProfile_Label.place(relx=0.1,rely=0.05) #x=100,y=30
name_Label = Label(profileFrame,text="Name :",font=('Arial',30),bg=back_ground).place(relx=0.05,rely=0.75)
myname_Label = Label(profileFrame,text=uID[0],font=('Arial',25),bg=back_ground).place(relx=0.21,rely=0.76)

name2_Label = Label(profileFrame,text="Name :",font=('Arial',25),bg=back_ground).place(relx=0.55,rely=0.05)
myname2_Label = Label(profileFrame,text=uID[0],font=('Arial',25),bg=back_ground).place(relx=0.68,rely=0.05)

rank_Label = Label(profileFrame,text="Rank  :",font=('Arial',25),bg=back_ground).place(relx=0.55,rely=0.15)
myrank_Label = Label(profileFrame,text=uID[1],font=('Arial',25),bg=back_ground).place(relx=0.68,rely=0.15)
team_Label = Label(profileFrame,text="Team :",font=('Arial',25),bg=back_ground).place(relx=0.55,rely=0.25)
myteam_Label = Label(profileFrame,text=uID[2],font=('Arial',25),bg=back_ground).place(relx=0.68,rely=0.25)

my_bio = Entry(profileFrame,font=('Arial',15),bg=back_ground,bd=1) 
my_bio.place(relx=0.55,rely=0.5,height=200,width=400)









frame_Topbar = Frame(win, width=window_width, height=70,bg='black')
frame_Topbar.place(relx=0,rely=0)
frame_Underbar = Frame(win, width=window_width, height=70,bg='black')
frame_Underbar.place(relx=0,rely=0.93)

button_Home = Button(win, text='Home Page',font=('Arial',12))
button_Home.place(x=100,y=10,height=50,width=120)
button_Scrim = Button(win, text='Scrim Board Page',font=('Arial',12))
button_Scrim.place(x=270,y=10,height=50,width=150)
button_Team = Button(win, text='Create Team Page',font=('Arial',12))
button_Team.place(x=470,y=10,height=50,width=150)

label_stay = Label(win,bg='gray')
label_stay.place(x=985,y=0,height=70,width=150)
button_Profile = Button(win, text='Profile Page',font=('Arial',12))
button_Profile.place(x=1000,y=10,height=50,width=120)

logo_label = Label(win,bg='pink')
logo_label.place(x=30,y=10,height=50,width=50)



win.mainloop()