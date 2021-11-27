# python program demonstrating
# Combobox widget using tkinter
  
  
from tkinter import*
from tkinter import ttk
  
# Creating tkinter window
window = Tk()
window.title('Combobox')
window.geometry("1280x720")
day_list = ["01", "02", "03", "04", "05", "06", "07", "08", "09"]
for i in range(10,32): day_list.append(str(i))
month_list = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
year_list = ["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029", "2030"]
hour_list = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09"]
for i in range(10,24): hour_list.append(str(i))
min_list =["00", "01", "02", "03", "04", "05", "06", "07", "08", "09"]
for i in range(10,60): min_list.append(str(i))

hour = StringVar()
hour.set("Hr")
#drop_Hr = OptionMenu(boradAddFrame, hour, *hour_list)
drop_Hr = ttk.Combobox(window, width = 3, textvariable = hour)
drop_Hr['values'] = hour_list
min = StringVar()
min.set("Min")
#drop_min = OptionMenu(boradAddFrame, min, *min_list)
drop_min = ttk.Combobox(window, width = 3, textvariable = min)
drop_min['values'] = min_list

day = StringVar()                                                       #########################################
day.set("Day")
drop_day = ttk.Combobox(window, width = 3, textvariable = day)
drop_day['values'] = day_list
month = StringVar()
month.set("Month")
drop_month = ttk.Combobox(window, width = 3, textvariable = month)
drop_month['values'] = month_list
year = StringVar()
year.set("Year")
drop_year = ttk.Combobox(window, width = 3, textvariable = year)
drop_year['values'] = year_list

drop_Hr.place(x=290,y=15,height=30,width=40)
#drop_Hr.grid(row=coutRow,column=coutCol+3,ipadx=10,ipady=0,padx=0,pady=10)
drop_min.place(x=335,y=15,height=30,width=50)
#drop_min.grid(row=coutRow,column=coutCol+4,ipadx=10,ipady=0,padx=10,pady=10)
drop_day.place(x=400,y=15,height=30,width=50)
drop_month.place(x=455,y=15,height=30,width=50)
drop_year.place(x=510,y=15,height=30,width=50)


window.mainloop()