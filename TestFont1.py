from tkinter import*
from tkcalendar import*


root = Tk()
window_width = 1280  # X
window_height = 720  # Y
root.minsize(height=window_height,width=window_width)

cal = Calendar(root, selectmode ="day", year=2020, month=1, day=1)
def showCal():
    cal.place(x=1000,y=200)

def date():
    my_label.config(text=cal.get_date(),font=('Arial',15))
    print(cal.get_date())

button = Button(root, text="Get Date", command=date)
button.pack(pady=20)

button_showDate = Button(root, text="Show Date", command=showCal)
button_showDate.pack(pady=20)

my_label = Label(root, text="")
my_label.pack(pady=20)


root.mainloop()