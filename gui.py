import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
import requests

root = tk.Tk()
root.title('Image 2 Ascii gui')
root.resizable(1000,1000)
root.geometry('300x150')

def selected_file():
    filetype=(('jpg files','*.jpg'),('png files','*.png'))
    filename = fd.askopenfilename(title = 'select the file',filetypes = filetype)
    baseurL='https://image2ascii.herokuapp.com/uploadfile/'
    f = open(filename, 'rb')
    files = {"file": (f.name, f, "multipart/form-data")}
    x=requests.post(url=baseurL, files=files)
    a=x.json().get('op')
    print(a)
    print('')
    
    
open_button = ttk.Button(root,text='Select the image',command=selected_file)

open_button.pack(expand=True)

root.mainloop()

