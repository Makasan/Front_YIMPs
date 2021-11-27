from tkinter import*
from tkinter import ttk
import requests
import hashlib


win = Tk()
win.geometry("1280x720")
win.resizable(False,False)
win.title("YIMPS Tabs")
win['bg'] = 'black'
back_ground = 'white'
window_width = 1280
window_height = 720
check = False

test_Loing = ["Makasan"]
test_password = ["123456"]
test_Register =[]


login_Frame = LabelFrame(win)
register_Frame = LabelFrame(win)

mycanvas_login = Canvas(login_Frame,bg="pink")
mycanvas_login.pack(fill=BOTH, expand=YES)
mycanvas_login.bind('<Configure>', lambda e: mycanvas_login.configure(scrollregion = mycanvas_login.bbox('all')))
myFrame_login = Frame(mycanvas_login) # ใช้
mycanvas_login.create_window((0,0), window=myFrame_login, anchor=NW)
login_Frame.place(x=350,y=60,height=600,width=600)

def home_page():
    mycanvas_login.destroy()
    login_Frame.destroy()
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

def login_page():
    check_pass = False

    clear_Label = Label(mycanvas_login,font=('Arial',50),bg=back_ground)
    clear_Label.place(x=0,y=0,width=600,height=600)
    login_Label = Label(mycanvas_login,text="Login",font=('Arial',50),bg=back_ground)
    login_Label.place(x=220,y=50)
    input_UserName = Entry(mycanvas_login, font=('Arial',15),bg=back_ground)
    input_UserName.place(x=270,y=200,width=300,height=30)
    #input_UserName.get
    #input_UserName.insert(0,"        8-16 character ")
    input_Label = Label(mycanvas_login,text="User Name       :",font=('Arial',20),bg=back_ground)
    input_Label.place(x=50,y=200,width=210,height=30)

    input_Password = Entry(mycanvas_login, show="*" ,font=('Arial',15),bg=back_ground)
    input_Password.place(x=270,y=250,width=300,height=30)
    #input_Password.get
    #input_Password.insert(0,"Password")
    Password_Label = Label(mycanvas_login,text="Password         :",font=('Arial',20),bg=back_ground)
    Password_Label.place(x=50,y=250,width=210,height=30)

    def check_home_page():
        password = hashlib.md5(input_Password.get().encode("utf-8"))
        id_user = {
            "username": str(input_UserName.get()) , 
            "password": str(password.hexdigest()) , 
        }
        respone = requests.get("http://34.124.169.53:8000/api/login",data=id_user, headers={'Content-Type': 'application/x-www-form-urlencoded'})
        #print(respone.text)
        checkID = dict(respone.json()) 
        print(checkID["currentUserID"])
        if 'Wrong Username' in checkID['message']  :
            warning_UserName = Label(mycanvas_login,text="User Name Incorrect",font=('Arial',15),bg=back_ground,fg="red")
            warning_UserName.place(x=10,y=300,width=250,height=30)
        elif 'Wrong Password' in checkID["message"] :
            warning_Password = Label(mycanvas_login,text="Password Incorrect",font=('Arial',15),bg=back_ground,fg="red")
            warning_Password.place(x=10,y=300,width=250,height=30)
        else:
            print("Go Home")
            home_page() 
            

    def showpass():
        input_Password.config(show='')
        showpass_Button = Button(mycanvas_login,command=hiddenpass,text="")
        showpass_Button.place(x=575,y=255,width=20,height=20)
    #input_ConfirmPass.insert(0,"Confirm Password")
    def hiddenpass():
        input_Password.config(show='*')
        showpass_Button = Button(mycanvas_login,command=showpass,text="")
        showpass_Button.place(x=575,y=255,width=20,height=20)

    register_Button = Button(mycanvas_login,text="Register", font=('Arial',15),command=register_page)
    register_Button.place(x=500,y=10,width=90,height=30)
    login_Button = Button(mycanvas_login,text="Login", font=('Arial',15),command=check_home_page)
    login_Button.place(x=400,y=290,width=80,height=35)

    if check_pass == False:
        hiddenpass()
        check_pass = True


def register_page():
    def register():
        warning = Label(mycanvas_login,text="                                          ",font=('Arial',15),bg=back_ground)
        warning.place(x=0,y=350,width=400,height=30)
        print(len(input_UserName.get()))
        if input_UserName.get() == '' or int(len(input_UserName.get())) < 8 or int(len(input_UserName.get()) > 16):
            warning = Label(mycanvas_login,text="User Name has 8-16 characters",font=('Arial',15),fg="red",bg=back_ground)
            warning.place(x=10,y=350,width=280,height=30)
        elif input_Password.get() == ''or int(len(input_Password.get())) < 8 or int(len(input_Password.get()) > 16):
            warning = Label(mycanvas_login,text="Password has 8-16 characters",font=('Arial',15),fg="red",bg=back_ground)
            warning.place(x=10,y=350,width=280,height=30)
        elif input_Password.get() != input_ConfirmPass.get() :
            warning = Label(mycanvas_login,text="Passwords do not match",font=('Arial',15),fg="red",bg=back_ground)
            warning.place(x=0,y=350,width=250,height=30)
        else:
            test_Register.append(input_UserName.get())
            test_Register.append(input_Password.get())
            print(test_Register)
            password = hashlib.md5(input_Password.get().encode("utf-8")) 
            dict = {
            "username": str(input_UserName.get()) , 
            "password": str(password.hexdigest()) , 
            }
            respone = requests.post("http://34.124.169.53:8000/api/createUser", data=dict, headers={'Content-Type': 'application/x-www-form-urlencoded'})
            print(respone.text)
            print(dict)
            if "username is already exist" in respone.text:
                warning = Label(mycanvas_login,text="Username is already !",font=('Arial',15),fg="red",bg=back_ground)
                warning.place(x=0,y=350,width=250,height=30)
                dict = {
                    "username": "",
                    "password": ""
                }
            else:
                login_page()
    #clear_Label = Label(mycanvas_login,font=('Arial',50),bg="pink")
    #clear_Label.place(x=200,y=50)
    clear_Label = Label(mycanvas_login,font=('Arial',50),bg=back_ground)
    clear_Label.place(x=0,y=0,width=600,height=600)
    Register_Label = Label(mycanvas_login,text="Register",font=('Arial',50),bg=back_ground)
    Register_Label.place(x=200,y=50)

    input_UserName = Entry(mycanvas_login, font=('Arial',15),bg=back_ground)
    input_UserName.place(x=270,y=200,width=300,height=30)
    #input_UserName.insert(0," 8-16 character ")
    input_Label = Label(mycanvas_login,text="User Name       :",font=('Arial',20),bg=back_ground)
    input_Label.place(x=50,y=200,width=210,height=30)

    input_Password = Entry(mycanvas_login, show="*" ,font=('Arial',15),bg=back_ground)
    input_Password.place(x=270,y=250,width=300,height=30)
    #input_Password.insert(0,"Password")
    Password_Label = Label(mycanvas_login,text="Password         :",font=('Arial',20),bg=back_ground)
    Password_Label.place(x=50,y=250,width=210,height=30)


    input_ConfirmPass = Entry(mycanvas_login, show="*",font=('Arial',15), bg=back_ground)
    input_ConfirmPass.place(x=270,y=300,width=300,height=30)
    
    ConfirmPass_Label = Label(mycanvas_login,text="Confirm Password :",font=('Arial',20),bg=back_ground)
    ConfirmPass_Label.place(x=10,y=300,width=250,height=30)


    """
    #clear_Label = Label(mycanvas_login,text="            ",font=('Arial',50),bg=back_ground)
    #clear_Label.place(x=10,y=200,width=160,height=30)
    input_UserName = Entry(mycanvas_login, font=('Arial',20),bg=back_ground)
    input_UserName.place(x=180,y=200,width=300,height=30)
    input_Label = Label(mycanvas_login,text="User Name :",font=('Arial',20),bg=back_ground)
    input_Label.place(x=10,y=200,width=160,height=30)


    clear_Label = Label(mycanvas_login,text="                                            ",font=('Arial',50),bg=back_ground)
    clear_Label.place(x=5,y=200,width=600,height=30)
     
    input_Password = Entry(mycanvas_login, show="*" ,font=('Arial',20),bg=back_ground)
    input_Password.place(x=180,y=250,width=300,height=30)
    input_Password.get
    #input_Password.insert(0,"Password")
    Password_Label = Label(mycanvas_login,text="Password   :eiei",font=('Arial',20),bg=back_ground)
    Password_Label.place(x=10,y=250,width=160,height=30)
    

    input_ConfirmPass = Entry(mycanvas_login, show="*",font=('Arial',20), bg=back_ground)
    input_ConfirmPass.place(x=180,y=300,width=300,height=30)
    input_ConfirmPass.get
    
    """
    login_backpage = Button(mycanvas_login,text="login", font=('Arial',15),bg=back_ground,command=login_page)
    login_backpage.place(x=5,y=10,width=90,height=30)
    register_Button = Button(mycanvas_login,text="Register", font=('Arial',15),command=register)
    #register_Button.place(x=150,y=500,width=150,height=50)
    register_Button.place(x=250,y=500,width=150,height=50)

    
    

if check == False:
    login_page()
    check = True

win.mainloop()