import tkinter as tk
from tkinter import messagebox

class GymMember:
    def __init__(self, name, age, membership_status):
        self.name = name
        self.age = age
        self.membership_status = membership_status

members = []

def add_member():
    name = name_entry.get()
    age = age_entry.get()
    membership_status = membership_status_var.get()

    if name and age and membership_status:
        member = GymMember(name, age, membership_status)
        members.append(member)
        member_listbox.insert(tk.END, member.name)
        name_entry.delete(0, tk.END)
        age_entry.delete(0, tk.END)
        membership_status_var.set("Select Membership Status")
    else:
        messagebox.showwarning("Warning", "Please fill in all fields.")

def display_member_details(event):
    selected_member = member_listbox.curselection()
    if selected_member:
        member = members[selected_member[0]]
        details_label.config(text=f"Name: {member.name}\nAge: {member.age}\nMembership: {member.membership_status}")
    else:
        details_label.config(text="Select a member to display details")

# Create the main application window
root = tk.Tk()
root.title("Gym Member Management System")

# Create entry fields and labels
name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

age_label = tk.Label(root, text="Age:")
age_label.pack()
age_entry = tk.Entry(root)
age_entry.pack()

membership_status_label = tk.Label(root, text="Membership Status:")
membership_status_label.pack()
membership_status_var = tk.StringVar()
membership_status_var.set("Select Membership Status")
membership_status_optionmenu = tk.OptionMenu(root, membership_status_var, "Regular", "Premium")
membership_status_optionmenu.pack()

# Create a button to add members
add_button = tk.Button(root, text="Add Member", command=add_member)
add_button.pack()

# Create a listbox to display member names
member_listbox = tk.Listbox(root)
member_listbox.pack()
member_listbox.bind("<<ListboxSelect>>", display_member_details)

# Create a label to display member details
details_label = tk.Label(root, text="")
details_label.pack()

# Start the main event loop
root.mainloop()
