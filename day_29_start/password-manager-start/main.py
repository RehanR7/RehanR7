from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)
    generated_password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, generated_password)
    pyperclip.copy(generated_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as f:
                # Reading old data
                data = json.load(f)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            with open("data.json", "w") as f:
                json.dump(new_data, f, indent=4)
        else:
            if website in data:
                update = messagebox.askyesno("Warning", f"There is already a password saved for"
                                                        f" {website}.\nWould you like to overwrite?")
                if update:
                    pass
                else:
                    return
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as f:
                # Saving updated data
                json.dump(data, f, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()


# ---------------------------- SAVE PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as f:
            data = json.load(f)

    except (FileNotFoundError, json.decoder.JSONDecodeError):
        messagebox.showinfo(title="Oops", message="No Data File Found or Data File is empty.")
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title="Result", message=f"Email: {email}\n"
                                                        f"Password: {password}")
        else:
            messagebox.showinfo(title="Oops", message=f"No details for the {website} exists.")

# ---------------------------- UI SETUP ------------------------------- #
# SCREEN
screen = Tk()
screen.title("Password Manager")
screen.config(padx=50, pady=50, bg="white")
# CANVAS
canvas = Canvas(width=200, height=200, highlightthickness=0, bg="white")
lock_image = PhotoImage(file="logo.png")
canvas.create_image(120, 100, image=lock_image)
canvas.grid(row=0, column=1)

# LABEL
website_label = Label(text="Website:", bg="white")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:", bg="white")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:", bg="white")
password_label.grid(row=3, column=0)

# ENTRY
website_entry = Entry(width=18, bg="white")
website_entry.focus()
website_entry.grid(row=1, column=1)

email_entry = Entry(width=37, bg="white")
email_entry.insert(0, "rhnather@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2, pady=5)

password_entry = Entry(width=18, bg="white")
password_entry.grid(row=3, column=1)

# BUTTON
generate_button = Button(text="Generate Password", bg="white", command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=34, bg="white", command=save_password)
add_button.grid(row=4, column=1, columnspan=2, pady=5)

search_button = Button(text="Search", bg="white", width=15, command=find_password)
search_button.grid(row=1, column=2)

screen.mainloop()
