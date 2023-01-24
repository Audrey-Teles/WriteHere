import tkinter as tk
from tkinter import filedialog

file = False


def save():
    global file
    if file:
        with open(file, "w") as f:
            f.write(text_area.get("1.0", "end"))
            f.close()
    else:
        save_as()


def save_as():
    global file
    file = filedialog.asksaveasfilename(defaultextension=".txt", initialfile="new_file.txt")

    if file:
        with open(file, "w") as f:
            f.write(text_area.get("1.0", "end"))
            f.close()


def open_file():
    global file
    file = filedialog.askopenfilename()
    if file:
        with open(file, "r") as f:
            text_area.insert("1.0", f.read())
            f.close()


def new():
    global file
    if file:
        save()
    text_area.delete("1.0", "end")
    file = False


font = ("Arial", 10)

root = tk.Tk()
root.title("WriteHere")

menu = tk.Menu(root)
root.config(menu=menu)

sub_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=sub_menu)

sub_menu.add_command(label="New", command=new)
sub_menu.add_command(label="Open", command=open_file)
sub_menu.add_command(label="Save As", command=save_as)
sub_menu.add_command(label="Save", command=save)

text_area = tk.Text(root)
text_area.configure(font=font)
text_area.pack(expand=1, fill="both")

root.mainloop()
