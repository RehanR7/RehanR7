import tkinter as tk
from tkinter import filedialog, messagebox
import yt_dlp
import threading


def download_video():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Error", "Please enter a YouTube URL")
        return

    folder = folder_path.get()
    if not folder:
        messagebox.showerror("Error", "Please select a download folder")
        return

    ydl_opts = {
        'outtmpl': f"{folder}/%(title)s.%(ext)s",  # Save in selected folder
        'format': 'bestvideo+bestaudio/best',  # Best quality
        'progress_hooks': [progress_hook]
    }

    def run_download():
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
        except Exception as e:
            messagebox.showerror("Error", f"Download failed: {str(e)}")

    # Run download in a separate thread to prevent UI freezing
    threading.Thread(target=run_download, daemon=True).start()
def download_audio():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Error", "Please enter a YouTube URL")
        return

    folder = folder_path.get()
    if not folder:
        messagebox.showerror("Error", "Please select a download folder")
        return

    ydl_opts = {
        'ignoreerrors': True,
        'outtmpl': f"{folder}/%(title)s.%(ext)s",  # Save in selected folder
        'format': 'bestaudio',  # Best quality
        'progress_hooks': [progress_hook]
    }

    def run_download():
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
        except Exception as e:
            messagebox.showerror("Error", f"Download failed: {str(e)}")

    # Run download in a separate thread to prevent UI freezing
    threading.Thread(target=run_download, daemon=True).start()

def select_folder():
    folder = filedialog.askdirectory()
    folder_path.set(folder)


def progress_hook(d):
    if d['status'] == 'downloading':
        progress_label.config(text=f"Downloading... {d['_percent_str']}")
    elif d['status'] == 'finished':
        progress_label.config(text="Download Complete!")


# GUI Setup
root = tk.Tk()
root.title("YouTube Downloader")
root.config(padx=50, pady=50, bg="white")

canvas = tk.Canvas(width=200, height=200, highlightthickness=0, bg="white")
lock_image = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

url_label = tk.Label(root, text="YouTube URL:  ", bg="white")
url_label.grid(row=1, column=0)

url_entry = tk.Entry(root, width=45, bg="white")
url_entry.grid(row=1, column=1, columnspan=2, pady=5)

folder_path = tk.StringVar()
folder_button = tk.Button(root, text="Select Download Folder", command=select_folder, bg="white")
folder_button.grid(row=2, column=1, pady=5)

video_download_button = tk.Button(root, text="Download Video", command=download_video, bg="white")
video_download_button.grid(row=3, column=0, pady=5)

video_download_button = tk.Button(root, text="Download_Audio", command=download_audio, bg="white")
video_download_button.grid(row=3, column=2, pady=5)

progress_label = tk.Label(root, text="", bg="white")
progress_label.grid(row=4, column=1, pady=5)

root.mainloop()




