import tkinter
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from tkinter.messagebox import showerror
import customtkinter
import clamd
import os
import threading


cd = clamd.ClamdNetworkSocket(host="127.0.0.1" , port=3311, timeout=None)
try:
    cd.ping()
except:
    showerror(
        title='brien protect error',
        message="brienprotect service not running"
    )
    exit()

# Modes: "System" (standard), "Dark", "Light"
customtkinter.set_appearance_mode("System")

# Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_default_color_theme("dark-blue")


app = customtkinter.CTk()

app.geometry("400x150")

app.title("BrienProtect")
app.iconbitmap("icon.ico")


def select_file():
    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/'
        )

    filepath = filename.replace("/", "\\")
    result = cd.scan(filepath)
    showinfo(
        title='Selected File',
        message=result.get(f"{filepath}")
    )

def select_folder():
    t = threading.Thread(target=threaded_scanfolder, args=(1,))
    t.start()
    

def threaded_scanfolder(name):
    foldername = fd.askdirectory(
        title='Open a folder',
        initialdir='/'
        )
    detects = []
    folderpath = foldername.replace("/", "\\")
    for root, dirs, files in os.walk(folderpath):
        for filename in files:
            filepath = os.path.join(root, filename).replace("/", "\\")
            result = cd.scan(filepath)
            print(result)
            if "FOUND" in result.get(f"{filepath}"):
                detects.append(filepath)
            
    print(detects)
    if not detects:
        showinfo(
            title='scanned folder',
            message="nothing found"
        )
    else:
        showinfo(
            title='scanned folder',
            message=f"number of detected viruses: {len(detects)}"
        )



frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)


button_scanfile = customtkinter.CTkButton(master=frame_1, command=select_file , text="scan a file")
button_scanfile.pack(pady=12, padx=10)

button_scanfolder = customtkinter.CTkButton(master=frame_1, command=select_folder , text="scan a folder")
button_scanfolder.pack(pady=12, padx=10)


app.mainloop()