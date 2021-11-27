from tkinter import*
from tkinter import ttk
import requests

window_width = 1280
window_height = 720
win = Tk()
win.geometry("1280x720")
win.resizable(False,False)
win.title("YIMPS Tabs")

########## เริ่มทำตรงนี้ #############










########## จบตรงนี้ #############

frame_Topbar = Frame(win, width=window_width, height=70,bg='black')
frame_Topbar.place(relx=0,rely=0)
frame_Underbar = Frame(win, width=window_width, height=70,bg='black')
frame_Underbar.place(relx=0,rely=0.93)
button_Home = Button(win, text='Home Page',font=('Arial',12))
button_Home.place(x=100,y=10,height=50,width=120)
button_Scrim = Button(win, text='Scrim Board Page',font=('Arial',12))
button_Scrim.place(x=270,y=10,height=50,width=150)
label_stay = Label(win,bg='gray')
label_stay.place(x=455,y=0,height=70,width=180)
button_Team = Button(win, text='Create Team Page',font=('Arial',12))
button_Team.place(x=470,y=10,height=50,width=150)
button_Profile = Button(win, text='Profile Page',font=('Arial',12))
button_Profile.place(x=1000,y=10,height=50,width=120)
logo_label = Label(win,bg='pink')
logo_label.place(x=30,y=10,height=50,width=50)

win.mainloop()