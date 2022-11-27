from infi.systray import SysTrayIcon
import os

brienprotectpath = r"C:\Program Files\Brienprotect"
mainexe = "main.exe"
def open_ui(name):
    os.system('\"C:\Program Files\Brienprotect\main.exe"')
    
menu_options = (("Open", None, open_ui),)
systray = SysTrayIcon("icon.ico", "brienprotect", menu_options)
systray.start()