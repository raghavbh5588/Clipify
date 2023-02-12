import tkinter as tk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

folder = ""


window = tk.Tk()
frame = tk.Frame(height = 500, width = 1000, background= "#d3d3d3")

frame.pack()

Welcome = tk.Label(text = "Welcome to Clipify!", font=("Impact", 40))
Welcome.place(anchor= "center", x= 500, y = 60)

explanation = tk.Label(text = "We create short and consumable snippets from your long-form videos using a amazing AI model", font=("Calibri", 18))
explanation.place(anchor= "center", x= 500, y = 120)

selectFileText = tk.Label(text = "To start select a file you want to create sippets of:", font=("Calibri", 18))
selectFileText.place(anchor= "center", x= 500, y = 200)

selectDirText = tk.Label(text = "Now select the location you want your video snippets:", font=("Calibri", 18))
selectDirText.place(anchor= "center", x= 500, y = 350)

def select_file():
    global filename
    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',)

    showinfo(
        title='Selected File',
        message=filename
    )

# open button
fileSelectButton = tk.Button(
    window,
    text='Open a File',
    command=select_file
)

def select_Dir():
    global folder
    folder = fd.askdirectory()

DirSelectButton = tk.Button(
    window,
    text='Select a Folder',
    command=select_Dir
)

DirSelectButton.place(anchor = "center", x = 500, y = 400)
DirSelectButton.config(width = 10, height = 2)

fileSelectButton.pack(expand=True)
fileSelectButton.place(anchor = "center", x = 500, y = 250)
fileSelectButton.config(width = 10, height = 2)


frame.mainloop()

userInput = [folder, filename]
print(userInput)