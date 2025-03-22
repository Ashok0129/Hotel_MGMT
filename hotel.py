import tkinter as tk
from tkinter import messagebox
import pickle
import os

# File to store guest data
GUEST_FILE = "hotel_data.dat"

# Check if the guest file exists, if not create it
if not os.path.exists(GUEST_FILE):
    with open(GUEST_FILE, 'wb') as file:
        pickle.dump([], file)

# Guest class to store guest information
class Guest:
    def __init__(self, name, address, mobile_no, room_no, price):
        self.name = name
        self.address = address
        self.mobile_no = mobile_no
        self.room_no = room_no
        self.price = price

# Function to save guest data to file
def save_guest_data(guest_data):
    with open(GUEST_FILE, 'wb') as file:
        pickle.dump(guest_data, file)

# Function to load guest data from file
def load_guest_data():
    with open(GUEST_FILE, 'rb') as file:
        return pickle.load(file)

# Function to add a new guest
def add_guest(name, address, mobile_no, room_no, price):
    guest_data = load_guest_data()
    guest = Guest(name, address, mobile_no, room_no, price)
    guest_data.append(guest)
    save_guest_data(guest_data)
    messagebox.showinfo("Success", f"Guest {name} checked-in successfully!")

# Function to check-out a guest
def checkout_guest(room_no):
    guest_data = load_guest_data()
    for guest in guest_data:
        if guest.room_no == room_no:
            guest_data.remove(guest)
            save_guest_data(guest_data)
            messagebox.showinfo("Success", f"Guest in room {room_no} checked-out successfully!")
            return
    messagebox.showerror("Error", "Room not found!")

# Function to view guest list
def view_guest_list():
    guest_data = load_guest_data()
    if not guest_data:
        messagebox.showinfo("Guest List", "No guests currently checked-in.")
        return
    guest_list_window = tk.Toplevel()
    guest_list_window.title("Guest List")
    guest_list_window.geometry("400x300")
    
    listbox = tk.Listbox(guest_list_window, width=50, height=15)
    listbox.pack(padx=20, pady=20)
    
    for guest in guest_data:
        listbox.insert(tk.END, f"Room: {guest.room_no} | Name: {guest.name}")
    
    close_button = tk.Button(guest_list_window, text="Close", command=guest_list_window.destroy)
    close_button.pack(pady=10)

# Function to get guest information
def get_guest_info(room_no):
    guest_data = load_guest_data()
    for guest in guest_data:
        if guest.room_no == room_no:
            messagebox.showinfo("Guest Info", f"Name: {guest.name}\nAddress: {guest.address}\nMobile: {guest.mobile_no}\nPrice: {guest.price}")
            return
    messagebox.showerror("Error", "Room not found!")

# Main application class
class HotelManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("400x400")

        # Welcome label
        self.label = tk.Label(root, text="Welcome to the Hotel Management System", font=("Arial", 14))
        self.label.pack(pady=20)

        # Check-in button
        self.checkin_button = tk.Button(root, text="1. Check-In", width=20, command=self.checkin)
        self.checkin_button.pack(pady=10)

        # Show guest list button
        self.guest_list_button = tk.Button(root, text="2. Show Guest List", width=20, command=view_guest_list)
        self.guest_list_button.pack(pady=10)

        # Check-out button
        self.checkout_button = tk.Button(root, text="3. Check-Out", width=20, command=self.checkout)
        self.checkout_button.pack(pady=10)

        # Get guest info button
        self.info_button = tk.Button(root, text="4. Get Guest Info", width=20, command=self.get_guest_info)
        self.info_button.pack(pady=10)

    # Check-in method
    def checkin(self):
        self.checkin_window = tk.Toplevel(self.root)
        self.checkin_window.title("Check-In")
        self.checkin_window.geometry("400x350")

        tk.Label(self.checkin_window, text="Enter Name:").pack(pady=5)
        self.name_entry = tk.Entry(self.checkin_window)
        self.name_entry.pack(pady=5)

        tk.Label(self.checkin_window, text="Enter Address:").pack(pady=5)
        self.address_entry = tk.Entry(self.checkin_window)
        self.address_entry.pack(pady=5)

        tk.Label(self.checkin_window, text="Enter Mobile No:").pack(pady=5)
        self.mobile_entry = tk.Entry(self.checkin_window)
        self.mobile_entry.pack(pady=5)

        tk.Label(self.checkin_window, text="Enter Room No:").pack(pady=5)
        self.room_entry = tk.Entry(self.checkin_window)
        self.room_entry.pack(pady=5)

        tk.Label(self.checkin_window, text="Enter Price:").pack(pady=5)
        self.price_entry = tk.Entry(self.checkin_window)
        self.price_entry.pack(pady=5)

        checkin_button = tk.Button(self.checkin_window, text="Check-In", width=20, command=self.perform_checkin)
        checkin_button.pack(pady=20)

    def perform_checkin(self):
        name = self.name_entry.get()
        address = self.address_entry.get()
        mobile_no = self.mobile_entry.get()
        room_no = self.room_entry.get()
        price = self.price_entry.get()

        if not (name and address and mobile_no and room_no and price):
            messagebox.showerror("Error", "Please fill all fields!")
        else:
            add_guest(name, address, mobile_no, room_no, price)
            self.checkin_window.destroy()

    # Check-out method
    def checkout(self):
        self.checkout_window = tk.Toplevel(self.root)
        self.checkout_window.title("Check-Out")
        self.checkout_window.geometry("400x200")

        tk.Label(self.checkout_window, text="Enter Room No to Check-Out:").pack(pady=5)
        self.room_checkout_entry = tk.Entry(self.checkout_window)
        self.room_checkout_entry.pack(pady=5)

        checkout_button = tk.Button(self.checkout_window, text="Check-Out", width=20, command=self.perform_checkout)
        checkout_button.pack(pady=20)

    def perform_checkout(self):
        room_no = self.room_checkout_entry.get()
        if not room_no:
            messagebox.showerror("Error", "Please enter a room number!")
        else:
            checkout_guest(room_no)
            self.checkout_window.destroy()

    # Get guest info method
    def get_guest_info(self):
        self.info_window = tk.Toplevel(self.root)
        self.info_window.title("Get Guest Info")
        self.info_window.geometry("400x200")

        tk.Label(self.info_window, text="Enter Room No to get Guest Info:").pack(pady=5)
        self.room_info_entry = tk.Entry(self.info_window)
        self.room_info_entry.pack(pady=5)

        info_button = tk.Button(self.info_window, text="Get Info", width=20, command=self.perform_get_info)
        info_button.pack(pady=20)

    def perform_get_info(self):
        room_no = self.room_info_entry.get()
        if not room_no:
            messagebox.showerror("Error", "Please enter a room number!")
        else:
            get_guest_info(room_no)
            self.info_window.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = HotelManagementApp(root)
    root.mainloop()
