import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import time
import threading
from plyer import notification
import os

FILE_NAME = os.path.join(os.path.dirname(__file__), "reminders.json")

# Ensure JSON file exists
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w") as file:
        json.dump([], file)

# Load reminders
def load_reminders():
    with open(FILE_NAME, "r") as file:
        return json.load(file)

# Save reminders
def save_reminders(reminders):
    with open(FILE_NAME, "w") as file:
        json.dump(reminders, file, indent=4)

# Add Reminder
def add_reminder():
    task = simpledialog.askstring("New Reminder", "Enter Task:")
    remind_after = simpledialog.askinteger("Reminder Time", "Enter minutes until reminder:")
    
    if task and remind_after:
        reminder_time = time.time() + (remind_after * 60)
        reminders.append({"task": task, "time": reminder_time, "done": False})
        save_reminders(reminders)
        update_reminder_list()
        messagebox.showinfo("Success", "Reminder Added!")

# Delete Reminder
def delete_reminder():
    selected = listbox.curselection()
    if selected:
        reminders.pop(selected[0])
        save_reminders(reminders)
        update_reminder_list()

# Mark Task as Done
def task_done():
    selected = listbox.curselection()
    if selected:
        reminders[selected[0]]["done"] = True
        save_reminders(reminders)
        update_reminder_list()

# Update Reminder List
def update_reminder_list():
    listbox.delete(0, tk.END)
    for reminder in reminders:
        status = "[Done]" if reminder["done"] else "[Pending]"
        listbox.insert(tk.END, f"{status} {reminder['task']}")

# Notification Handler
def check_reminders():
    while True:
        now = time.time()
        for reminder in reminders:
            if not reminder["done"] and now >= reminder["time"]:
                notification.notify(title="Reminder Alert", message=reminder["task"], timeout=10)
                time.sleep(900)  # 15 minutes for silent reminders
        time.sleep(30)

# GUI Setup
root = tk.Tk()
root.title("Time Reminder App")

reminders = load_reminders()

frame = tk.Frame(root)
frame.pack()

listbox = tk.Listbox(frame, width=50, height=10)
listbox.pack()

btn_add = tk.Button(root, text="Add Reminder", command=add_reminder)
btn_add.pack()

btn_delete = tk.Button(root, text="Delete Reminder", command=delete_reminder)
btn_delete.pack()

btn_done = tk.Button(root, text="Task Done", command=task_done)
btn_done.pack()

update_reminder_list()

# Background Reminder Checker
threading.Thread(target=check_reminders, daemon=True).start()

root.mainloop()
