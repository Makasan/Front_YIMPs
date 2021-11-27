from tkinter import*
import hashlib
import requests

root =Tk()
root.title("Test")
root.geometry("400x400")


# def myClick():
#     result = hashlib.md5(data.encode("utf-8"))
#     print(result.hexdigest())

# e = Entry(root,width=50)
# e.pack(padx=10,pady=10)
# data = e.get()
# myButton = Button(root, text="Enter Name",command=myClick)
# myButton.pack(pady=10)


# dict_1 = {
#     "username": "Maka" , 
#     "password": "123456" , 
# }
# respone = requests.get("http://34.124.169.53:8000/api/login",data=dict_1, headers={'Content-Type': 'application/x-www-form-urlencoded'})
# print(respone.text)
# data_backEnd = dict(respone.json()) 
# print(data_backEnd)


respone = requests.get("http://34.124.169.53:8000/api/getallposts")
data_backEnd = dict(respone.json()) 
print(data_backEnd["allPosts"])

root.mainloop()



