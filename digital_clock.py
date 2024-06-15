import tkinter as tk
import time
from tkinter import font

def update_time():
    # Get the current time, date, and day of the week
    current_hours_minutes = time.strftime('%I:%M')
    current_seconds = time.strftime('%S')
    current_am_pm = time.strftime('%p')
    current_date = time.strftime('%B %d %Y').upper()
    current_day = time.strftime('%A').upper()

    # Update the labels with the current time, date, and day of the week
    hours_minutes_label.config(text=current_hours_minutes)
    seconds_label.config(text=current_seconds)
    am_pm_label.config(text=current_am_pm)
    date_label.config(text=current_date) 
    day_label.config(text=current_day)
    
    # Schedule the update_time function to run again after 1000 milliseconds (1 second)
    root.after(1000, update_time)

# Create the main window
root = tk.Tk()
root.title('Digital Clock')

# Styling options
bg_color = 'black'
fg_color = 'limegreen'
font_large = ('Digital-7 Mono', 100)
font_medium = ('Digital-7', 60)
font_small = ('Digital-7', 30)

# Configure the main window background color
root.configure(bg=bg_color)

# Create and place the labels for hours and minutes
hours_minutes_label = tk.Label(root, font=font_large, bg=bg_color, fg=fg_color)
hours_minutes_label.grid(row=0, column=0, columnspan=2)

# Create and place the label for seconds
seconds_label = tk.Label(root, font=font_medium, bg=bg_color, fg=fg_color)
seconds_label.grid(row=0, column=2, sticky='nw')

# Create and place the label for AM/PM
am_pm_label = tk.Label(root, font=font_small, bg=bg_color, fg=fg_color)
am_pm_label.grid(row=0, column=3, sticky='n')

# Create and place the label for the date
date_label = tk.Label(root, font=font_small, bg=bg_color, fg=fg_color)
date_label.grid(row=1, column=0, columnspan=4)

# Create and place the label for the day of the week
day_label = tk.Label(root, font=font_small, bg=bg_color, fg=fg_color)
day_label.grid(row=2, column=0, columnspan=4)

# Start updating the time
update_time()

# Run the Tkinter event loop
root.mainloop()
