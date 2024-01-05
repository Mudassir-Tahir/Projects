from tkinter import Tk, Label,  Entry, Button, filedialog
from tkinter import ttk, filedialog
import requests
import os
# https://dl.3u.com/update/v300/dl/3uTools_v3.05.031_Setup_x86.exe
class Downloader:
    def __init__(self):
        self.saveto = ""
        self.window = Tk()
        self.window.title("Python GUI Downloader")
        self.url_label = Label(text="Enter URL")
        self.url_label.pack()
        self.url_entry = Entry()
        self.url_entry.pack()
        self.browse_button = Button(text="Browse",command=self.browse_file)
        self.browse_button.pack()
        self.download_button = Button(text="Download",command=self.download)
        self.download_button.pack()
        self.window.geometry("800x300")
        self.progress_bar = ttk.Progressbar(self.window, orient="horizontal", maximum=100, length=300, mode="determinate")
        self.progress_bar.pack()
        self.window.mainloop()
    def browse_file(self):
        saveto = filedialog.asksaveasfilename(initialfile=self.url_entry.get().split("/")[-1].split("?")[0])
        self.saveto = saveto

    def download(self):
        url = self.url_entry.get()
        response = requests.get(url, stream=True)
        total_size_in_bytes = 100
        if(response.headers.get("content-length")):
            total_size_in_bytes = int(response.headers.get("content-length"))
        block_size=10000
        self.progress_bar["value"] = 0
        fileName = self.url_entry.get().split("/")[-1].split("?")[0]
        if(self.saveto == ""):
            self.saveto = fileName

            print(self.saveto)
        with open(self.saveto, "wb") as f:
            for data in response.iter_content(block_size):
                self.progress_bar["value"] += (100*block_size)/total_size_in_bytes
                self.window.update()
                f.write(data)



Downloader()