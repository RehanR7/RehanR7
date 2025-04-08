import customtkinter as ctk
from tkinter import messagebox
from PIL import Image
from random import randint, choice, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!#$%&()*+'

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)
    generated_password = "".join(password_list)

    password_entry.delete(0, ctk.END)
    password_entry.insert(0, generated_password)
    pyperclip.copy(generated_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website: {"email": email, "password": password}}

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as f:
                data = json.load(f)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            with open("data.json", "w") as f:
                json.dump(new_data, f, indent=4)
        else:
            if website in data:
                update = messagebox.askyesno("Warning", f"There is already a password saved for {website}.\nWould you like to overwrite?")
                if not update:
                    return
            data.update(new_data)
            with open("data.json", "w") as f:
                json.dump(data, f, indent=4)
        finally:
            website_entry.delete(0, ctk.END)
            password_entry.delete(0, ctk.END)
            website_entry.focus()

# ---------------------------- FIND PASSWORD ------------------------------- #
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
            messagebox.showinfo(title="Result", message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Oops", message=f"No details for {website} exist.")

# ---------------------------- UI SETUP ------------------------------- #
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

screen = ctk.CTk()
screen.title("Password Manager")
screen.geometry("500x400")

# CANVAS (Image Display)
lock_image = ctk.CTkImage(light_image=Image.open("logo.png"), size=(150, 150))
canvas = ctk.CTkLabel(master=screen, image=lock_image, text="")
canvas.grid(row=0, column=1, pady=10)

# LABELS
website_label = ctk.CTkLabel(master=screen, text="Website:")
website_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
email_label = ctk.CTkLabel(master=screen, text="Email/Username:")
email_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
password_label = ctk.CTkLabel(master=screen, text="Password:")
password_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")

# ENTRIES
website_entry = ctk.CTkEntry(master=screen, width=150)
website_entry.focus()
website_entry.grid(row=1, column=1, padx=5, pady=5)
email_entry = ctk.CTkEntry(master=screen, width=300)
email_entry.insert(0, "rhnather@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2, padx=5, pady=5)
password_entry = ctk.CTkEntry(master=screen, width=150, show="*")
password_entry.grid(row=3, column=1, padx=5, pady=5)

# BUTTONS
generate_button = ctk.CTkButton(master=screen, text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2, padx=5, pady=5)
add_button = ctk.CTkButton(master=screen, text="Add", width=300, command=save_password)
add_button.grid(row=4, column=1, columnspan=2, padx=5, pady=10)
search_button = ctk.CTkButton(master=screen, text="Search", width=130, command=find_password)
search_button.grid(row=1, column=2, padx=5, pady=5)

screen.mainloop()
