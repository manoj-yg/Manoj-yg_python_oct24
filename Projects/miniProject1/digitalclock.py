import tkinter as tk
from time import strftime

def update_time():
    # Get the current time in 12-hour format
    time = strftime("%I:%M:%S %p")  # %I for 12-hour format, %p for AM/PM
    clock_label.config(text=time)
    clock_label.after(1000, update_time)  # Update every second

# Create the main Tkinter window
root = tk.Tk()
root.title("Digital Clock - 12-Hour Format")
root.geometry("400x200")  # Optional, to set the size of the window

# Add a label for the clock
clock_label = tk.Label(
    root,
    font=("Arial", 48),
    background="black",
    foreground="white"
)
clock_label.pack(anchor="center", pady=50)

# Start the clock
update_time()

# Run the Tkinter event loop
root.mainloop()
