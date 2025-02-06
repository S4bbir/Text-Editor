import os
from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter import messagebox
from tkinter.filedialog import *


def change_color():
    color = colorchooser.askcolor(title="Pick a color")
    text_area.config(fg = color[1])

def change_font(*args):
    text_area.config(font = (font_name.get(), size_box.get()))

def new_file():
    window.title("Untitled")
    text_area.delete("1.0", END)

def open_file():
    file = askopenfilename(defaultextension=".txt", file= [("All Files", "*.*"), ("Text Documents", "*.txt" )])
    try:
        window.title(os.path.basename(file))
        text_area.delete("1.0", END)

        file = open(file, "r")
        text_area.insert(1.0, file.read())

    except Exception as e:
        messagebox.showerror("Error", f"Could not open file: {e}")

    finally:
        file.close()

def save_file():
    file = filedialog.asksaveasfile(initialfile="Untitled.txt",
                                    defaultextension=".txt",
                                    filetypes=[("All Files", "*.*"),
                                  ("Text Documents", "*.txt" )])
    if file is None:
        return
    else:
        try:
            with open(file.name, "w") as file:
                file.write(text_area.get(1.0, END))
            window.title(f"{os.path.basename(file.name)}")
        except Exception as e:
            messagebox.showerror("Error", f"Could not save file: {e}")

        finally:
            file.close()


def cut():
    text_area.event_generate("<<Cut>>")

def copy():
    text_area.event_generate("<<Copy>>")

def paste():
    text_area.event_generate("<<Paste>>")

def about():
    messagebox.showinfo("About", "This is a simple text editor built with Python and Tkinter.")

def exit():
    if messagebox.askyesno("Exit", "Do you really want to exit?"):
        window.destroy()

#window config ----------------------------------------------------------
window = Tk()
window.title("Text Editor")
file = None

window_width = 600
window_height = 700

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))

# system font set ----------------------------------------------------------
font_name =StringVar(window)
font_name.set("System")

font_size = StringVar(window)
font_size.set("15")
text_area = Text(window, font=(font_name.get(), font_size.get()))

#scroll bar ----------------------------------------------------------
scroll_bar = Scrollbar(text_area)
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
text_area.grid(sticky=N+E+S+W)

scroll_bar.pack(side = RIGHT, fill = Y)
text_area.config(yscrollcommand = scroll_bar.set)

frame = Frame(window)
frame.grid()

# color and fonts ----------------------------------------------------------
color_button = Button(frame, text="Color", command=change_color)
color_button.grid(row=0, column=0)

font_box = OptionMenu(frame, font_name, *font.families(), command=change_font)
font_box.grid(row=0, column=1)

size_box = Spinbox(frame, from_=1, to=100, textvariable=font_size, command=change_font)
size_box.grid(row=0, column=2)

# menu bar ----------------------------------------------------------
menu_bar = Menu(window)
window.config(menu=menu_bar)


# file menu ----------------------------------------------------------
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
# file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit)

#edit menu ----------------------------------------------------------
edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)

#help menu ----------------------------------------------------------
help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label= "Help", menu= help_menu)

help_menu.add_command(label="About", command=about)



window.mainloop()