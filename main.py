import tkinter as tk

root = tk.Tk()
root.title("To Do List")

check_list = []

def remove_task(task):
    check_list.remove(task)
    for widget in root.winfo_children():
        if widget.winfo_class() == "Frame":
            widgets = widget.winfo_children()
            if len(widgets) >= 2:
                check_button = widgets[0]
                check_task = check_button.cget("text")
                if check_task == task:
                    widget.destroy()

def create_task_frame(task):
    task_frame = tk.Frame(root)
    task_frame.pack(anchor="w")
    
    # Create a Checkbutton
    new_check_button = tk.Checkbutton(task_frame, text=task, font=("calibri", 10))
    new_check_button.pack(side="left")
    
    # Create a Remove Button
    remove_button = tk.Button(task_frame, text="Remove", font=("calibri", 10), command=lambda: remove_task(task))
    remove_button.pack(side="left")

def create_check_button():
    task = task_entry.get()
    if task not in check_list and task != "":
        check_list.append(task)
        create_task_frame(task)
        task_entry.delete(0, "end")  # Clear the task_entry field

task_entry = tk.Entry(root, width=50, font=("calibri", 12))
task_entry.pack()

add_btn = tk.Button(root, text="Add Task", font=("calibri", 12), command=create_check_button)
add_btn.pack()

root.mainloop()
