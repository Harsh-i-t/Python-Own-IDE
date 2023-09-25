# for visual graphics
import subprocess
from tkinter import *
import tkinter as tk
from tkinter import END, Label, Menu, Text, ttk
# from tkinter import font
from tkinter import messagebox
from tkinter.filedialog import asksaveasfilename, askopenfilename
# from turtle import width

# for code editor
from tkcode import CodeEditor

# code = input("Enter File Title:")
file_path = ''

def set_file_path(path):
    global file_path
    file_path = path


# for heading block
root = tk.Tk()
root2 = tk.Tk()
root.title("My Code Editor")
root2.title("Output Window")
root.option_add("*tearoff",0)

# functionality of button "run"
def run():
    if file_path == "":
        messagebox.showinfo("Caution","Save Your Code")
        return
    command = f'python {file_path}'
    process = subprocess.Popen(command, stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = True)
    output, error = process.communicate()
    code_output.insert('1.0',output)                          
    code_output.insert('1.0',error)                          

def save_as():
    if file_path == '':
        path = asksaveasfilename(filetypes=[('Python Files', '*.py')])
    else:
        path = file_path 
    with open(path, 'w') as file:
        code = code_editor.get('1.0',END)
        file.write(code)
        set_file_path(path)

def open_file():
    path = askopenfilename(filetypes=[('Python Files', '*.py')])
    with open(path, 'r') as file:
        code = file.read()
        code_editor.delete('1.0',END)
        code_editor.insert('1.0',code)
        set_file_path(path)


def exitS():
    result = messagebox.askquestion('Caution','Do you want to save your work?')
    if result == 'yes': save_as()
    else: exit()
        

# adding menu bar at top of the window
menu_bar = Menu(root)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_as)
file_menu.add_command(label="Save As", command=save_as)
file_menu.add_command(label="Exit", command=exitS)
menu_bar.add_cascade(label="File",menu=file_menu)

run_bar = Menu(menu_bar, tearoff=0)
run_bar.add_command(label="Run", command=run)
menu_bar.add_cascade(label="Run",menu=run_bar)
root.config(menu = menu_bar)

# creating a notebook frame and giving it title and '.py' extension 
notebook = ttk.Notebook(root)
tab_1 = ttk.Frame(notebook)
notebook.add(tab_1)
notebook.pack(fill="both" , expand=True)
notebook2 = ttk.Notebook(root2)
tab_2 = ttk.Frame(notebook2)
notebook2.add(tab_2)
notebook2.pack(fill="both" , expand=True)

# with the help of library setting the properties of our code block
code_editor = CodeEditor(
    tab_1,
    width = 99,
    height = 20,
    language = 'python',
    background  = 'black',
    highlighter = 'dracula',
    font = 'Consolas',
    autofocus = True,
    blockcursor = True,
    insertofftime = 0,
    padx = 10,
    pady = 10
)

code_editor.pack(fill="both" , expand=True)
root.update()
# root.maxsize(root.winfo_width(),root.winfo_height())
code_output = Text(tab_2,font='Consolas')
code_output.pack()
root.mainloop()