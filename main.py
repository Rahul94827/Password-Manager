# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letter = [random.choice(letters) for _ in range(nr_letters)]
    password_symbol = [random.choice(symbols) for _ in range(nr_symbols)]
    password_number = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letter + password_symbol + password_number
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json","r") as data:
            read_data=json.load(data)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops",message="No Data found")
    else:
        if website in read_data:
            email=read_data[website]["email"]
            password=read_data[website]["password"]
            messagebox.showinfo(title="Message",message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Oops",message=f"No details for {website} exits")

def save_password():
    website = website_entry.get()
    email = email_user_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please dont leave field empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                 data = json.load(data_file)
                # print(data)
        except FileNotFoundError:
            with open("data.json","w") as data_file:
                json.dump(new_data,data_file,indent=4)
            # Update old data with new data
        else:
            data.update(new_data)


            with open("data.json","w") as data_file:
                # # Saving Updated data
                json.dump(data, data_file, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=100, pady=100)

canvas = Canvas(width=200, height=200)
pass_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pass_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_user_label = Label(text="Email/Username:")
email_user_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entry
website_entry = Entry(width=32)
website_entry.grid(column=1, row=1)
website_entry.focus()

email_user_entry = Entry(width=50)
email_user_entry.grid(column=1, row=2, columnspan=2)
email_user_entry.insert(0, "rahul@gmail.com")

password_entry = Entry(width=32)
password_entry.grid(column=1, row=3)

# buttons
pass_button = Button(text="Generate Password", width=14, command=generate_password)
pass_button.grid(column=2, row=3)

add_button = Button(text="Add", width=42, bg="Green", command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=14,command=find_password)
search_button.grid(column=2, row=1)

window.mainloop()
