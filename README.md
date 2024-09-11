#Text Editor Program
Welcome to the Text Editor Program! This is a simple text editor written in Python using the Tkinter library. This application allows you to create, open, save, and edit text files. You can also customize text color, font type, and font size.

##Features
Create a new text file
Open an existing text file
Save the current text file
Cut, copy, and paste text
Change text color
Change font type and size
About dialog providing information about the program

##Requirements
Python 3.x
Tkinter library (comes pre-installed with Python)

##Usage
1. Running the Program:

  To run the program, simply execute the script in a Python environment.

2. Basic Operations:

  New: Create a new, empty text document.
  Open: Open an existing text document from your file system.
  Save: Save the current document to your file system.
  Cut: Remove the selected text and copy it to the clipboard.
  Copy: Copy the selected text to the clipboard.
  Paste: Paste the text from the clipboard at the cursor position.

3. Changing Text Properties:

  Color: Click the "Color" button to choose a new text color.
  Font: Use the dropdown menu to select a different font.
  Font Size: Use the spinbox to adjust the font size.

4. About:

  Access the "About" dialog from the "Help" menu to get information about the program.

##Code Explanation
Importing Libraries
'''
import os
from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *
'''

##Functions
change_color(): Opens a color picker dialog and updates the text color.
change_font(*args): Updates the font type and size of the text area.
new_file(): Clears the text area and resets the window title to "Untitled".
open_file(): Opens a file dialog to select a file and loads its content into the text area.
save_file(): Opens a file dialog to save the current content of the text area to a file.
cut(), copy(), paste(): Performs the respective clipboard operations on the text area.
about(): Displays an information dialog about the program.
quit(): Closes the application window.

##GUI Setup
Window Setup: Initializes the main window and sets its size and position.
Text Area: Provides a text area with a scrollbar for displaying and editing text.
Tool Frame: Contains buttons and widgets for changing text properties.
Menus: Creates a menu bar with "File," "Edit," and "Help" menus.

##Execution
window.mainloop() - Starts the Tkinter event loop, displaying the window and awaiting user interaction.
