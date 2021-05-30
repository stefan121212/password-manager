from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- SEARCH ------------------------------- #
COLOR = "#7868e6"

def find_password():
    website = website_entry.get().capitalize()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title=website, message="No Data file Found.")
    else:
        if website in data:
            email = data[website]["email"]
            pass1 = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword is: {pass1}")
            pyperclip.copy(pass1)
        else:
            messagebox.showerror(title="Error", message=f"No details for the {website} exists.")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_list += [choice(letters) for char in range(randint(8, 10))]
    password_list += [choice(numbers) for number in range(randint(2, 4))]
    password_list += [choice(symbols) for symbol in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get().capitalize()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Warning", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
            # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()


def scale_used(value):
    n = value

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
my_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=my_img)
canvas.grid(row=0, column=1)
# labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_username_label = Label(text="Email/Username: ")
email_username_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
# entries
website_entry = Entry()
website_entry.grid(row=1, column=1, sticky="EW")
website_entry.focus()

email_entry = Entry()
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
email_entry.insert(0, "Stefan.ssss22@gmail.com")
password_entry = Entry()
password_entry.grid(row=3, column=1, sticky="EW")

generate_pass_button = Button(text="Generate Password", command=generate_password)
generate_pass_button.grid(row=3, column=2, sticky="EW")

add_button = Button(text="Add", command=save)
add_button.config(width=20)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

search_button = Button(text="Search", command=find_password, bg=COLOR, fg="white")
search_button.config(width=20)
search_button.grid(row=1, column=2, sticky="EW")

scale = Scale(from_=8, to=24, command=scale_used, orient=HORIZONTAL, label="length of password", length=150)
scale.grid(row=5, column=1, columnspan=2)

window.mainloop()