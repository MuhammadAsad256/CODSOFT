import tkinter as tk
from tkinter import messagebox

# Function to add a task to the listbox
def add_task():
    task = entry_task.get()
    if task != "":
        # Insert task into the listbox
        listbox_tasks.insert(tk.END, task)
        # Clear entry field after adding task
        entry_task.delete(0, tk.END)
    else:
        # Show a warning if the task entry is empty
        messagebox.showwarning("Warning", "Please enter a task.")

# Function to delete a selected task from the listbox
def delete_task():
    try:
        # Get the index of the selected task
        task_index = listbox_tasks.curselection()[0]
        # Delete the task from the listbox
        listbox_tasks.delete(task_index)
    except IndexError:
        # Show a warning if no task is selected for deletion
        messagebox.showwarning("Warning", "Please select a task to delete.")

# Function to clear all tasks from the listbox
def clear_tasks():
    # Delete all tasks from the listbox
    listbox_tasks.delete(0, tk.END)

# Main Window
root = tk.Tk()
root.title("To-Do List")
root.geometry("420x470+50+50")
root.resizable(False, False)
root.configure(bg='#bfb8b8')

bg_color = '#61595b'
fg_color = '#FFFFFF'
highlight_bg_color = '#594646'
highlight_fg_color = '#FFFFFF'

frame_tasks = tk.Frame(root, bg=bg_color)
frame_tasks.pack(pady=10)

# Heading
label_heading = tk.Label(frame_tasks, text="All Tasks", bg=bg_color, fg=fg_color, font=("Helvetica", 16, "bold"))
label_heading.pack()

# Listbox to display tasks
listbox_tasks = tk.Listbox(frame_tasks, height=10, width=50, border=0, bg=bg_color, fg=fg_color, selectbackground=highlight_bg_color, selectforeground=highlight_fg_color, font=("Helvetica", 14))
listbox_tasks.pack(side=tk.LEFT)

# Scrollbar for listbox
scrollbar_tasks = tk.Scrollbar(frame_tasks, bg=bg_color, troughcolor=highlight_bg_color, activebackground=highlight_bg_color)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

# Heading for entering task
label_enter_task = tk.Label(root, text="Enter Task", bg=bg_color, fg=fg_color, font=("Helvetica", 15, "bold"))
label_enter_task.pack()

# Entry field for user to enter task
entry_task = tk.Entry(root, width=50, bg=bg_color, fg=fg_color, insertbackground=fg_color, highlightbackground=highlight_bg_color, highlightcolor=highlight_fg_color, font=("Helvetica", 13))
entry_task.pack(pady=10)

# Button to add task
button_add_task = tk.Button(root, text="Add Task", width=48, command=add_task, bg=highlight_bg_color, fg=highlight_fg_color, activebackground=highlight_bg_color, activeforeground=highlight_fg_color, font=("Helvetica", 14))
button_add_task.pack()

# Button to delete task
button_delete_task = tk.Button(root, text="Delete Task", width=48, command=delete_task, bg=highlight_bg_color, fg=highlight_fg_color, activebackground=highlight_bg_color, activeforeground=highlight_fg_color, font=("Helvetica", 14))
button_delete_task.pack()

# Button to clear all tasks
button_clear_tasks = tk.Button(root, text="Clear all Tasks", width=48, command=clear_tasks, bg=highlight_bg_color, fg=highlight_fg_color, activebackground=highlight_bg_color, activeforeground=highlight_fg_color, font=("Helvetica", 14))
button_clear_tasks.pack()

root.mainloop()
