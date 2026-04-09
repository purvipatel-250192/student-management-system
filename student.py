import tkinter as tk

students = []

def add_student():
    name = name_entry.get()
    roll = roll_entry.get()

    if name == "" or roll == "":
        result_label.config(text="Enter all fields", fg="red")
    else:
        students.append(f"{name} - {roll}")
        result_label.config(text="Student Added", fg="green")
        name_entry.delete(0, tk.END)
        roll_entry.delete(0, tk.END)

def show_students():
    display_box.delete("1.0", tk.END)
    for s in students:
        display_box.insert(tk.END, s + "\n")

root = tk.Tk()
root.title("Student Management System")
root.geometry("400x400")

tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Roll No").pack()
roll_entry = tk.Entry(root)
roll_entry.pack()

tk.Button(root, text="Add", command=add_student).pack()
tk.Button(root, text="Show", command=show_students).pack()

result_label = tk.Label(root, text="")
result_label.pack()

display_box = tk.Text(root, height=10)
display_box.pack()

root.mainloop()
