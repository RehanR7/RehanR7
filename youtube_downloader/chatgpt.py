import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import yt_dlp
import threading


def select_folder():
    folder = filedialog.askdirectory()
    folder_path.set(folder)


def progress_hook(d):
    """Updates the progress bar and label during download"""
    if d['status'] == 'downloading':
        percent = float(d['_percent_str'].strip('%'))
        progress_bar["value"] = percent
        progress_label.config(text=f"Downloading... {d['_percent_str']}")
    elif d['status'] == 'finished':
        progress_label.config(text="Download Complete!")
        progress_bar["value"] = 100


def download_media(audio_only=False):
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
        'format': 'bestaudio' if audio_only else 'bestvideo+bestaudio/best',  # Best quality
        'progress_hooks': [progress_hook],
        'noplaylist': False,  # Enable playlist downloading
        'embed_chapters': True,  # Embed chapters
    }

    def run_download():
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)  # Get playlist/video info

                if 'entries' in info:
                    total_videos = len(info['entries'])
                else:
                    total_videos = 1  # Single video

                completed_videos = 0

                for entry in info.get('entries', [info]):
                    if entry:
                        ydl.download([entry['webpage_url']])
                        completed_videos += 1
                        playlist_label.config(text=f"Downloaded {completed_videos} of {total_videos}")

                messagebox.showinfo("Success", "Download Completed!")
        except Exception as e:
            messagebox.showerror("Error", f"Download failed: {str(e)}")

    threading.Thread(target=run_download, daemon=True).start()
    url_entry.focus()

# GUI Setup
root = tk.Tk()
root.title("YouTube Downloader")
root.config(padx=20, pady=20, bg="white")

canvas = tk.Canvas(width=200, height=200, highlightthickness=0, bg="white")
lock_image = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

# URL Entry
tk.Label(root, text="YouTube URL:", bg="white").grid(row=1, column=0, padx=5, pady=5)
url_entry = tk.Entry(root, width=45)
url_entry.grid(row=1, column=1, columnspan=2, pady=5)

# Folder Selection
folder_path = tk.StringVar()
tk.Button(root, text="Select Folder", command=select_folder, bg="white").grid(row=2, column=1, pady=5)

# Download Buttons
tk.Button(root, text="Download Video", command=lambda: download_media(audio_only=False), bg="white").grid(row=3,
                                                                                                          column=0,
                                                                                                          pady=5)
tk.Button(root, text="Download Audio", command=lambda: download_media(audio_only=True), bg="white").grid(row=3,
                                                                                                         column=2,
                                                                                                         pady=5)

# Progress Bar
progress_label = tk.Label(root, text="", bg="white")
progress_label.grid(row=3, column=1, pady=5)
progress_bar = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
progress_bar.grid(row=4, column=1, pady=5)

# Playlist Progress
playlist_label = tk.Label(root, text="Waiting", bg="white")
playlist_label.grid(row=5, column=1, pady=5)

root.mainloop()
