import tkinter

# window
window = tkinter.Tk()
window.title("First GUI Program")
window.minsize(width=500,height=400)
# Label
label = tkinter.Label(text="I am a label.", font=("Arial", 18, "normal"))
label.grid(row=0, column=0)
#Button
def button_clicked():
    # print("I got clicked")
    new_text = entry.get()
    label.config(text=new_text)

button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(row=1, column=1)

new_button = tkinter.Button(text="New Buttom")
new_button.grid(row=0, column=2)
# Entry
entry = tkinter.Entry()
entry.grid(row=2, column=3)

window.mainloop()
