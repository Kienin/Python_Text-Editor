import os
from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *

# Define functions with comments explaining their purpose
def change_color():
    """Opens a color picker dialog and changes the text area font color"""
    color = colorchooser.askcolor(title="Pick a color")
    print("Color picked is: ", color)  # For debugging purposes (can be removed)
    text_area.config(fg=color[1])  # Set text color to the chosen color

def change_font(*args):
    """Updates the text area font based on selected font and size"""
    text_area.config(font=(font_name.get(), size_box.get()))

def new_file():
    """Creates a new empty file"""
    window.title("Untitled")
    text_area.delete(1.0, END)  # Delete all text from the text area

def open_file():
    """Opens a file and displays its content in the text area"""
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if file is None:
        return  # Do nothing if no file is selected

    try:
        window.title(os.path.basename(file))  # Set window title to file name
        text_area.delete(1.0, END)  # Clear text area before opening new content

        file = open(file, "r")  # Open the selected file in read mode
        text_area.insert(1.0, file.read())  # Insert file content into text area
    except Exception:
        print("Unable to read file")
    finally:
        file.close()  # Ensure file is closed even if an exception occurs

def save_file():
    """Saves the text area content to a file"""
    file = filedialog.asksaveasfilename(initialfile="untitled.txt", defaultextension=".txt",
                                       filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])

    if file is None:
        return  # Do nothing if no file is selected

    try:
        window.title(os.path.basename(file))  # Set window title to file name
        file = open(file, "w")  # Open the selected file in write mode
        file.write(text_area.get(1.0, END))  # Write text area content to the file
    except Exception:
        print("Unable to save file")
    finally:
        file.close()  # Ensure file is closed even if an exception occurs

def cut():
    """Uses Tkinter event to simulate cut functionality"""
    text_area.event_generate("<<Cut>>")

def copy():
    """Uses Tkinter event to simulate copy functionality"""
    text_area.event_generate("<<Copy>>")

def paste():
    """Uses Tkinter event to simulate paste functionality"""
    text_area.event_generate("<<Paste>>")

def about():
    """Displays a message box with information about the program"""
    showinfo("About this program", "This is a Text Editor Program written by Kevin. Have a good day!")

def quit():
    """Exits the program by destroying the main window"""
    window.destroy()


# Create the main window
window = Tk()

window.title("Text Editor Program")
file = None  # Keeps track of the currently opened file

window_width = 500
window_height = 500
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Center the window on the screen
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))

# Create string variables to store font name and size
font_name = StringVar(window)
font_name.set("Comic Sans")

font_size = StringVar(window)
font_size.set("20")

# Create the text area widget
text_area = Text(window, font=(font_name.get(), font_size.get()))

# Create a scrollbar for the text area
scroll_
