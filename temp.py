from tkinter import*
from tkcalendar import*
import requests

#34.124.169.53
#respone = requests.get("http://34.124.169.53:8000/api/getposts-sorted",data={'method':"rank"}, headers={'Content-Type': 'application/x-www-form-urlencoded'})
#temp = dict(respone.json())
#print(temp["allPosts"])

dict_1 = {
    "username" : 'DiFve' ,
    "password" : '123456'
}
#print(dict_1)
respone = requests.get("http://34.124.169.53:8000/api/login",data=dict_1, headers={'Content-Type': 'application/x-www-form-urlencoded'})
data_backEnd = dict(respone.json()) 
print(data_backEnd)

user_pass = requests.get("http://34.124.169.53:8000/api/getUserInfo/" + str(data_backEnd["currentUserID"]), headers={'Content-Type': 'application/x-www-form-urlencoded'} )
i_d = dict(user_pass.json())
print(i_d)