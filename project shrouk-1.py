from tkinter import *
from tkinter import messagebox 

from pytube import YouTube


def download_video(resolution):
    url = entry.get()
    if not url:
        messagebox.showerror("Error", "Please paste a YouTube link!")
        return
    
    try:
        yt = YouTube(url)

        if resolution == "high":
            stream = yt.streams.get_highest_resolution()
        elif resolution == "low":
            stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').first()
        elif resolution == "audio":
            stream = yt.streams.filter(only_audio=True).first()

        
        messagebox.showinfo("Downloading", f"Downloading {resolution} resolution...")
        stream.download()
        messagebox.showinfo("Success", f"{resolution.capitalize()} resolution download completed!")

    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong: {e}")


root = Tk()  
root.title("sh. Downloader")
root.configure(bg="antiquewhite4")


title_label = Label(root, text="YouTube Downloader", font=("times new roman", 18, "bold"))
title_label.pack(pady=10)


entry_label = Label(root, text="Paste Link Here:", font=("tahoma", 12))
entry_label.pack()
entry = Entry(root, width=50)
entry.pack(pady=5)
root.geometry("500x300")


high_res_button = Button(root, text="High Resolution", bg="antiquewhite2", fg="black", font=("comic sans ms", 12), 
                          command=lambda: download_video("high"))
high_res_button.pack(pady=5)

low_res_button = Button(root, text="Low Resolution", bg="antiquewhite2", fg="black", font=("comic sans ms", 12), 
                         command=lambda: download_video("low"))
low_res_button.pack(pady=5)

audio_button = Button(root, text="Audio Only", bg="antiquewhite2", fg="black", font=("comic sans ms", 12), 
                       command=lambda: download_video("audio"))
audio_button.pack(pady=5)


root.mainloop()