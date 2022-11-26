import tkinter
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import customtkinter
import clamd

cd = clamd.ClamdNetworkSocket(host="127.0.0.1" , port=3311, timeout=None)


# Modes: "System" (standard), "Dark", "Light"
customtkinter.set_appearance_mode("System")

# Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_default_color_theme("dark-blue")


app = customtkinter.CTk()

app.geometry("400x580")

app.title("BrienProtect")


def select_file():


    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/'
        )

    filepath = filename.replace("/", "\\")
    result = cd.scan(filepath)
    print(type(result))
    showinfo(
        title='Selected File',
        message=result.get(f"{filepath}")
    )

frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)


button_scanfile = customtkinter.CTkButton(master=frame_1, command=select_file , text="scan a file")
button_scanfile.pack(pady=12, padx=10)



app.mainloop()