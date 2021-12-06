import hashlib
from tkinter import*
from tkinter import ttk
from PIL import ImageTk, Image
import requests
from requests.models import Response
from tkinter.filedialog import askopenfile
import base64

window_width = 1280
window_height = 720
win = Tk()
win.geometry("1280x720")
win.resizable(False,False)
win.title("YIMPS Tabs")
back_ground = 'black' #ใส่ BlackGround เป็นรูปด้วย
pageChoose = True
########## เริ่มทำตรงนี้ #############

password = hashlib.md5("123456789".encode("utf-8"))
id_user = {
    "username": "MakasanKawaii" , 
    "password": str(password.hexdigest()) , 
}

respone = requests.get("http://34.124.169.53:8000/api/login",data=id_user, headers={'Content-Type': 'application/x-www-form-urlencoded'})
checkID = dict(respone.json())
UserID = checkID["currentUserID"]

####################################################
image = Image.open("XboxBG.jpeg")
BGimage = ImageTk.PhotoImage(image.resize((window_width,window_height)))

temp = Canvas(win,bg=back_ground, width=window_width, height=window_height)
temp.place(x=0 , y=0)

bg_Image = Label(win,image=BGimage)
bg_Image.place(x=-2,y=0)


#---------------------------------------------No Team Page--------------------------------------------------------#

def noTeamPage():
    Middle_BG = Label(win,bg='white')
    Middle_BG.place(x=340,y=100,width=600,height=590)

    text_label = Label(win,text="Oops You Don't Have Team Yet",font=('Arial',30),bg='white')
    text_label.place(x=360,y=120)

    btn_createTeam_page = Button(win,text="Create Your Team NOW!!!",font=('Arial',20),command=createTeamPage)
    btn_createTeam_page.place(x=470,y=200)

#---------------------------------------------Create Team Page----------------------------------------------------#

def createTeamPage():
    Middle_BG = Label(win,bg='white')
    Middle_BG.place(x=150,y=70,width=980,height=650)

    pic_box = Label(win,text="PIC 500x500??",font=('Arial',10),bg='grey')
    pic_box.place(x=170,y=90,width=150,height=150)

    name_team = Label(win,text='Team Name',font=('Arial',12),bg='white')
    name_team.place(x=340,y=90)

    input_teamName = Entry(win,font=('Arial',12),bg='lightgrey')
    input_teamName.place(x=440,y=90,width=200,height=20)

    name_bio = Label(win,text='BIO',font=('Arial',12),bg='white')
    name_bio.place(x=340,y=120)

    bioBox = Text(win,width=570,height=90,font=('Arial',12),bg='lightblue')
    bioBox.place(x=340,y=150,width=570,height=90)

    def createTeamFuction():
        #Get UserID from Login Scene
        respone = requests.get("http://34.124.169.53:8000/api/getUserInfoByID/"+str(UserID))
        checkRank = dict(respone.json())
        teamRank = checkRank['userInfo']['rank']
        teamName = input_teamName.get()
        bio = bioBox.get(1.0,END)
        dictdata = {
            "teamName":teamName,
            "teamRank":teamRank,
            "teamLead":UserID,
            "bio":bio,
        }
        print(dictdata)
        if dictdata['teamName'] == '':
            print("TeamName cannnot be Blank")
        else:
            respone = requests.post("http://34.124.169.53:8000/api/createteam", data=dictdata, headers={'Content-Type': 'application/x-www-form-urlencoded'})
            print(respone.text)
            teamPage()

    createTeam = Button(win,text='Create Team',command=createTeamFuction)
    createTeam.place(x=580,y=280,width=120,height=40)

#---------------------------------------------Team Page--------------------------------------------------------#

def teamPage():
    Middle_BG = Label(win,bg='white')
    Middle_BG.place(x=150,y=70,width=980,height=650)

    # Get TeamName Data
    respone = requests.get("http://34.124.169.53:8000/api/getUserInfoByID/"+str(UserID))
    checkTeamID = dict(respone.json())
    loginUserID = checkTeamID['userInfo']['_id']
    teamID = checkTeamID['userInfo']["team"]

    respone = requests.get("http://34.124.169.53:8000/api/getteam/"+str(teamID))
    teamData = dict(respone.json())
    memberList = teamData['reqTeam']['teamMember']

    nMember = len(memberList)   #Use for FOR-LOOP and Pos of Box
    teamName = teamData['reqTeam']['teamData']['teamName']
    teamRank = teamData['reqTeam']['teamData']['teamRank']
    teamBio = teamData['reqTeam']['teamData']['bio']

    def downloadMemberPicture():
        global memberData
        memberData = []
        for n in range(nMember):
            memberID = memberList[n]['userid']
            download_respone = requests.get("http://34.124.169.53:8000/api/getProfileImage/"+str(memberID))
            picture = dict(download_respone.json())
            image_ = picture["image"].encode('utf-8')
            image_ = base64.decodebytes(image_)
            download = ('Image/PictureProfile/' + memberID + ".png")
            output = open(download, 'wb')
            output.write(image_)
            output.close()  

    def updateMemberPicture():
        for n in range(nMember):
            memberID = memberList[n]['userid']
            pathPicture = "Image/PictureProfile/" + memberID + ".png"
            imagepic = Image.open(pathPicture)
            memberData.append(ImageTk.PhotoImage(imagepic.resize((150, 150))))
            member_Image = Label(win, image= memberData[n])
            member_Image.place(x=180+(190*n),y=300)

    def updateTeamPicture():
        download_respone = requests.get("http://34.124.169.53:8000/api/getTeamImage/"+str(teamID))
        picture = dict(download_respone.json())
        image_ = picture["image"].encode('utf-8')
        image_ = base64.decodebytes(image_)
        download = ('Image/PictureTeam/' + teamID + ".png")
        output = open(download, 'wb')
        output.write(image_)
        output.close()
        global profile_Image
        pathPicture = "Image/PictureTeam/" + teamID + ".png"

        imagepic = Image.open(pathPicture)
        profile_Image = ImageTk.PhotoImage(imagepic.resize((150, 150)))
        myProfile_Label = Label(win, image= profile_Image).place(x=170,y=90,width=150,height=150)
        
    def chooseFile():
        file_path = askopenfile(mode='rb', filetypes=[('Image Files', '*jpg')])
        if file_path is not None:
            pass
        data = file_path.read()
        data = base64.encodebytes(data)
        global dictPic
        dictPic = {
            "_id" : teamID,
            "pictureProfile" : data
        }
        label = Label(win,text="Comeplete")
        label.place(x=920,y=190,height=20,width=80)
        
    def uploadFile():
        print("uploadFile")
        respone = requests.put("http://34.124.169.53:8000/api/setTeamImage", data=dictPic, headers={'Content-Type': 'application/x-www-form-urlencoded'})
        print(respone.text)
        teamPage()

    updateTeamPicture()
    updateMemberPicture()
    #downloadMemberPicture()

    name_team = Label(win,text='Team Name :',font=('Arial',12),bg='white')
    name_team.place(x=340,y=90)

    userTeamName = Label(win,text=teamName,font=('Arial',12),bg='white')
    userTeamName.place(x=450,y=90)

    avg_team = Label(win,text='Avg Team Rank :',font=('Arial',12),bg='white')
    avg_team.place(x=700,y=90)

    userTeamRank = Label(win,text=teamRank,font=('Arial',12),bg='white')
    userTeamRank.place(x=830,y=90)

    name_bio = Label(win,text='BIO',font=('Arial',12),bg='white')
    name_bio.place(x=340,y=120)

    userBio = Label(win,text=teamBio,font=('Arial',12),bg='lightblue',anchor='nw')
    userBio.place(x=340,y=150,width=570,height=90)

    line = Label(win,bg='black')
    line.place(x=150,y=260,width=980,height=10)

    #---------------------------------------------Edit Page--------------------------------------------------------#
    def editButton():
        userTeamName = Entry(win,text=teamName,font=('Arial',12),bg='white')
        userTeamName.delete(0,END)
        userTeamName.insert(0,teamName)
        userTeamName.place(x=450,y=90)

        userBio = Text(win,width=570,height=90,font=('Arial',12),bg='lightblue')
        userBio.insert(INSERT,teamBio)
        userBio.place(x=340,y=150,width=570,height=90)

        rdyRemoveRMember = []
        #Remove Member BTN
        for n in range(1,nMember):
            memberID = memberList[n]['userid']
            rMember = Button(win,text='-',font=('Arial',15),bg='red',command= lambda data=[memberID,n]:removeMemberConfirm(data))
            rMember.place(x=315+(190*n),y=300,width=15,height=15)
            rdyRemoveRMember.append(rMember)

        
        def comfirmEdit():
            teamNameText = userTeamName.get()
            bioText = userBio.get(1.0,END)
            editData = {
                'teamName':teamNameText,
                'bio':bioText,
            }
            respone = requests.put('http://34.124.169.53:8000/api/editteam/'+teamID, data=editData, headers={'Content-Type': 'application/x-www-form-urlencoded'})
            print(respone.text)
            teamPage()

        def cancelEdit():
            userTeamName.destroy()
            userBio.destroy()
            Yedit_Button.destroy()
            Nedit_Button.destroy()
            choose_file_btn.destroy()
            upload_file_btn.destroy()
            for btn in rdyRemoveRMember:
                btn.destroy()

        
        Yedit_Button = Button(win,text='Y',font=('Arial',12),bg='lightgreen',command=comfirmEdit)
        Yedit_Button.place(x=980,y=90,width=50,height=30)

        Nedit_Button = Button(win,text='N',font=('Arial',12),bg='red',command=cancelEdit)
        Nedit_Button.place(x=1050,y=90,width=50,height=30)

        choose_file_btn = Button(win,text='Choose File',font=('Arial',10),command=chooseFile)
        choose_file_btn.place(x=920,y=220,width=80,height=20)

        upload_file_btn = Button(win,text='Upload File',font=('Arial',10),command=uploadFile)
        upload_file_btn.place(x=1010,y=220,width=80,height=20)

    respone = requests.get("http://34.124.169.53:8000/api/getteam/"+str(teamID))
    teamData = dict(respone.json())
    teamLeadID = teamData['reqTeam']['teamData']['teamLead']

    if loginUserID == teamLeadID:
        edit_Button = Button(win,text='EDIT',font=('Arial',12),command=editButton)
        edit_Button.place(x=1050,y=90,width=50,height=30)

    #---------------------------------------------Add Member--------------------------------------------------------#
    def addMember():

        def cancelAddMember():
            BGadd.destroy()
            backBtn.destroy()
            text_enterUsername.destroy()
            input_username.destroy()
            addMemberConfirm.destroy()
        
        def confirmAddMember():
            username = input_username.get()
            respone = requests.get("http://34.124.169.53:8000/api/getUserInfoByName/"+str(username))
            usernameCheck = dict(respone.json())
            userID = usernameCheck['userInfo']['_id']

            dictMember = {
                'userid':userID
            }
            respone = requests.put('http://34.124.169.53:8000/api/addmember/'+str(teamID),data=dictMember, headers={'Content-Type': 'application/x-www-form-urlencoded'})
            print(respone.text)
            downloadMemberPicture()
            teamPage()

        BGadd = Label(win)
        BGadd.place(x=180+(190*nMember),y=300,width=150,height=150)

        backBtn = Button(win,text='X',font=('Arial',15),command=cancelAddMember,bg='red')
        backBtn.place(x=315+(190*nMember),y=300,width=15,height=15)

        text_enterUsername = Label(win,text='Enter Username',font=('Arial',12))
        text_enterUsername.place(x=180+(190*nMember),y=320,width=150,height=20)

        input_username = Entry(win,font=('Arial',12),bg='lightgrey')
        input_username.place(x=200+(190*nMember),y=350,width=110,height=20)

        addMemberConfirm = Button(win,text='Confirm',font=('Arial',15),command=confirmAddMember)
        addMemberConfirm.place(x=210+(190*nMember),y=390,width=90,height=30)

    #---------------------------------------------Remove Member--------------------------------------------------------#

    def removeMemberConfirm(data):
        userID = data[0]
        n = data[1]

        def nRemove():
            text_enterUsername.destroy()
            BGremove.destroy()
            Y_remove.destroy()
            N_remove.destroy()

        def yRemove():
            dictMember = {
                "userid":userID
            }
            respone = requests.put('http://34.124.169.53:8000/api/removemember/'+str(teamID),data=dictMember,headers={'Content-Type': 'application/x-www-form-urlencoded'})
            print(respone.text)
            downloadMemberPicture()
            teamPage()

        BGremove = Label(win)
        BGremove.place(x=180+(190*n),y=300,width=150,height=150)

        text_enterUsername = Label(win,text='Are You Sure?',font=('Arial',12))
        text_enterUsername.place(x=180+(190*n),y=320,width=150,height=20)

        Y_remove = Button(win,text='Y',font=('Arial',12),command=yRemove)
        Y_remove.place(x=220+(190*n),y=350,width=30,height=20)

        N_remove = Button(win,text='N',font=('Arial',12),command=nRemove)
        N_remove.place(x=270+(190*n),y=350,width=30,height=20)

    #------------------------------------------Create Profile Box-----------------------------------------------------#
    
    updateMemberPicture()
    
    for n in range(0,nMember):
        #Get Each Member ID
        memberID = memberList[n]['userid']

        #Get Name From Each Member ID
        respone = requests.get("http://34.124.169.53:8000/api/getUserInfoByID/"+str(memberID))
        checkMemberData = dict(respone.json())
        memberName = checkMemberData['userInfo']['username']
        rankMember = checkMemberData['userInfo']['rank']

        playerName = Label(win,text=memberName,font=('Arial',15))
        playerName.place(x=180+(190*n),y=460,width=150,height=28)

        respone = requests.get("http://34.124.169.53:8000/api/getteam/"+str(teamID))
        teamData = dict(respone.json())
        teamLeadID = teamData['reqTeam']['teamData']['teamLead']

        rank_text = Label(win,text=rankMember,font=('Arial',13))
        rank_text.place(x=180+(190*n),y=490,width=150,height=28)

        if memberID == teamLeadID:
            playerPos = Label(win,text="Leader",font=('Arial',8))
            playerPos.place(x=180+(190*n),y=520,width=150,height=28)
        else:
            playerPos = Label(win,text="Member",font=('Arial',8))
            playerPos.place(x=180+(190*n),y=520,width=150,height=28)

    #Create Add Member Button
    if nMember < 5 and loginUserID == teamLeadID:
        addMember = Button(win,text='+',font=('Arial',20),command=addMember)
        addMember.place(x=180+(190*nMember),y=300,width=150,height=150)

    
global memberData

#Check User have team or not
respone = requests.get("http://34.124.169.53:8000/api/getUserInfoByID/"+str(UserID))
teamCheck = dict(respone.json())
teamID = teamCheck['userInfo']['team']
if teamID == '':
    noTeamPage()
else:
    respone = requests.get("http://34.124.169.53:8000/api/getUserInfoByID/"+str(UserID))
    checkTeamID = dict(respone.json())
    loginUserID = checkTeamID['userInfo']['_id']
    teamID = checkTeamID['userInfo']["team"]

    respone = requests.get("http://34.124.169.53:8000/api/getteam/"+str(teamID))
    teamData = dict(respone.json())
    memberList = teamData['reqTeam']['teamMember']

    nMember = len(memberList)   #Use for FOR-LOOP and Pos of Box
    teamName = teamData['reqTeam']['teamData']['teamName']
    teamRank = teamData['reqTeam']['teamData']['teamRank']
    teamBio = teamData['reqTeam']['teamData']['bio']

    memberData = []
    for n in range(nMember):
        memberID = memberList[n]['userid']
        download_respone = requests.get("http://34.124.169.53:8000/api/getProfileImage/"+str(memberID))
        picture = dict(download_respone.json())
        image_ = picture["image"].encode('utf-8')
        image_ = base64.decodebytes(image_)
        download = ('Image/PictureProfile/' + memberID + ".png")
        output = open(download, 'wb')
        output.write(image_)
        output.close()
    
    teamPage()

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