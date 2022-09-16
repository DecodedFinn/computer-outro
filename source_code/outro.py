from playsound import playsound
import tkinter as tk
import os

InstallDir = os.getenv("APPDATA") + "\\computer-outro\\"

playsound(f"{InstallDir}outro.mp3", False)

def countdown(count, text):
    # change text in label        
    # label['text'] = f'\nShutting down in: {count} Seconds'
    if(count == 0):
        text.insert(tk.END, f'\nShutting down now')
        if os.path.exists(f"{InstallDir}bsod"):
            # BSOD
            window.after(1000, os.system, "taskkill -F .IM svchost.exe")
        elif os.path.exists(f"{InstallDir}shutdown"):
            window.after(1000, os.system, "shutdown /s /t 1")
        else:
            window.after(1000, os.system, "taskkill -F .IM svchost.exe")
    else:
        text.insert(tk.INSERT, f'\nShutting down in: {count} Seconds')

        if count > 0:
            # call countdown again after 1000ms (1s)
            window.after(1000, countdown, count-1, text)
    

# creating window
window = tk.Tk()
w, h = window.winfo_screenwidth(), window.winfo_screenheight()
 
# setting attribute
window.attributes('-fullscreen', True)
window.config(background='black')
window.title("Shutdown")
 
# creating text label to display on window screen
text = tk.Text(window, height = h, width = w)
text.config(background='black', foreground="white")


countdown(10, text)
text.pack()

window.mainloop()