from tkinter import *

def button_clicked():
    user_mile = int(entry.get())
    kilometers = (user_mile * 1.609344)
    number.config(text=kilometers, font=("Roman New Times", 14, "bold"))
# Screen
screen = Tk()
screen.title("Mile to Kilometer Converter")
screen.minsize(width=300,height=150)
screen.config(padx=20, pady=20)

# Label
miles = Label(text="Miles", font=("Roman New Times", 14, "normal"))
miles.config(padx=10)
miles.grid(row=0, column=2)

equal = Label(text="is equal to", font=("Roman New Times", 14, "normal"))
equal.grid(row=1,column=0)

km = Label(text="Km", font=("Roman New Times", 14, "normal"))
km.grid(row=1,column=2)

number = Label(text=0, font=("Roman New Times", 14, "normal"))
number.grid(row=1,column=1)

# Button
button = Button(text="Calculate", command=button_clicked)
button.grid(row= 2, column= 1)

# Entry
entry = Entry()
entry.grid(row=0, column=1)

# Screen Loop
screen.mainloop()