import tkinter as tk
from tkinter import messagebox

class HotelManagementGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("600x400")
        
        # Data structures
        self.rooms = {i: {'type': 'Single', 'price': 1000, 'status': 'Available'} for i in range(1, 11)}
        self.rooms.update({i: {'type': 'Double', 'price': 2000, 'status': 'Available'} for i in range(11, 21)})
        self.bookings = {}

        # GUI Components
        self.create_widgets()
    
    def create_widgets(self):
        # Title
        title = tk.Label(self.root, text="Hotel Management System", font=("Arial", 16, "bold"))
        title.pack(pady=10)

        # Buttons
        tk.Button(self.root, text="Display Rooms", width=20, command=self.display_rooms).pack(pady=5)
        tk.Button(self.root, text="Book a Room", width=20, command=self.book_room).pack(pady=5)
        tk.Button(self.root, text="Check Out", width=20, command=self.check_out).pack(pady=5)
        tk.Button(self.root, text="Generate Bill", width=20, command=self.generate_bill).pack(pady=5)
        tk.Button(self.root, text="Exit", width=20, command=self.root.quit).pack(pady=5)

    def display_rooms(self):
        # Show room details in a new window
        display_window = tk.Toplevel(self.root)
        display_window.title("Room Details")
        display_window.geometry("400x300")
        
        text = tk.Text(display_window, wrap=tk.WORD, font=("Arial", 10))
        text.pack(expand=True, fill=tk.BOTH)

        for room_no, details in self.rooms.items():
            text.insert(tk.END, f"Room {room_no}: Type: {details['type']}, Price: {details['price']}, Status: {details['status']}\n")
    
    def book_room(self):
        def confirm_booking():
            room_no = int(room_entry.get())
            customer_name = name_entry.get()
            customer_contact = contact_entry.get()
            
            if room_no in self.rooms and self.rooms[room_no]['status'] == 'Available':
                self.rooms[room_no]['status'] = 'Booked'
                self.bookings[room_no] = {'name': customer_name, 'contact': customer_contact}
                messagebox.showinfo("Success", f"Room {room_no} has been booked successfully!")
                book_window.destroy()
            else:
                messagebox.showerror("Error", "Invalid room number or room already booked.")
        
        # Booking window
        book_window = tk.Toplevel(self.root)
        book_window.title("Book Room")
        book_window.geometry("300x200")
        
        tk.Label(book_window, text="Room Number:").grid(row=0, column=0, pady=5)
        room_entry = tk.Entry(book_window)
        room_entry.grid(row=0, column=1, pady=5)
        
        tk.Label(book_window, text="Customer Name:").grid(row=1, column=0, pady=5)
        name_entry = tk.Entry(book_window)
        name_entry.grid(row=1, column=1, pady=5)
        
        tk.Label(book_window, text="Customer Contact:").grid(row=2, column=0, pady=5)
        contact_entry = tk.Entry(book_window)
        contact_entry.grid(row=2, column=1, pady=5)
        
        tk.Button(book_window, text="Book", command=confirm_booking).grid(row=3, column=0, columnspan=2, pady=10)
    
    def check_out(self):
        def confirm_checkout():
            room_no = int(room_entry.get())
            
            if room_no in self.rooms and self.rooms[room_no]['status'] == 'Booked':
                self.rooms[room_no]['status'] = 'Available'
                del self.bookings[room_no]
                messagebox.showinfo("Success", f"Room {room_no} has been checked out.")
                checkout_window.destroy()
            else:
                messagebox.showerror("Error", "Invalid room number or room is not booked.")
        
        # Checkout window
        checkout_window = tk.Toplevel(self.root)
        checkout_window.title("Check Out")
        checkout_window.geometry("250x100")
        
        tk.Label(checkout_window, text="Room Number:").grid(row=0, column=0, pady=5)
        room_entry = tk.Entry(checkout_window)
        room_entry.grid(row=0, column=1, pady=5)
        
        tk.Button(checkout_window, text="Check Out", command=confirm_checkout).grid(row=1, column=0, columnspan=2, pady=10)
    
    def generate_bill(self):
        def show_bill():
            room_no = int(room_entry.get())
            nights = int(nights_entry.get())
            
            if room_no in self.rooms and self.rooms[room_no]['status'] == 'Booked':
                bill_amount = nights * self.rooms[room_no]['price']
                messagebox.showinfo("Bill", f"Bill for Room {room_no}:\nAmount: ${bill_amount}")
                bill_window.destroy()
            else:
                messagebox.showerror("Error", "Invalid room number or room is not booked.")
        
        # Bill window
        bill_window = tk.Toplevel(self.root)
        bill_window.title("Generate Bill")
        bill_window.geometry("250x150")
        
        tk.Label(bill_window, text="Room Number:").grid(row=0, column=0, pady=5)
        room_entry = tk.Entry(bill_window)
        room_entry.grid(row=0, column=1, pady=5)
        
        tk.Label(bill_window, text="Nights Stayed:").grid(row=1, column=0, pady=5)
        nights_entry = tk.Entry(bill_window)
        nights_entry.grid(row=1, column=1, pady=5)
        
        tk.Button(bill_window, text="Generate Bill", command=show_bill).grid(row=2, column=0, columnspan=2, pady=10)

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = HotelManagementGUI(root)
    root.mainloop()
