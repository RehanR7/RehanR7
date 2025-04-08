import os
import subprocess

# Prompt for download directory
save_dir = input("Enter the directory where you want to save the downloads (e.g., /home/nano/Videos): ")

# Ask if it is a playlist or a single video
content_type = input("Is this a playlist or a single video? (playlist/video): ")

# Handle playlist or single video based on user input
if content_type == "playlist":
    playlist_url = input("Enter the playlist URL: ")
    target_url = playlist_url
    # Set the output template for playlists
    output_template = f'"{save_dir}/%(playlist_title)s/%(title)s.%(ext)s"'
else:
    video_url = input("Enter the video URL: ")
    target_url = video_url
    create_folder = input("Do you want to create a folder for this video? (yes/no): ")

    # Create a folder for the video if user wants to
    if create_folder.lower() == "yes":
        folder_name = input("Enter the folder name: ")
        save_dir = os.path.join(save_dir, folder_name)
        os.makedirs(save_dir, exist_ok=True)

    # Set the output template for single videos
    output_template = f'"{save_dir}/%(title)s.%(ext)s"'

# Prompt for whether to download subtitles
download_subs = input("Do you want to download subtitles? (yes/no): ")

sub_options = ""
if download_subs.lower() == "yes":
    sub_lang = input("Enter the subtitle language (e.g., en, es, fr, de, it): ")
    auto_subs = input("Do you want to download auto-generated subtitles if manual ones are unavailable? (yes/no): ")
    embed_subs = input("Do you want to embed subtitles in the video? (yes/no): ")
    sub_format = input("Which subtitle format do you want? (e.g., srt, vtt): ")

    # Add subtitle-related options to the command
    sub_options = f'--write-subs --sub-lang {sub_lang} --convert-subs {sub_format}'

    if auto_subs.lower() == "yes":
        sub_options += " --write-auto-subs"

    if embed_subs.lower() == "yes":
        sub_options += " --embed-subs"

# Prompt for video format
video_format = input("Enter the desired video format (e.g., mp4, mkv, webm): ")

# Prompt for video quality
video_quality = input("Enter the desired video quality (e.g., 144, 240, 360, 480, 720, 1080, 1440, 2160): ")

# Construct the `yt-dlp` command based on user inputs
yt_dlp_command = f"yt-dlp -o {output_template} {sub_options} --merge-output-format {video_format} -f \"bestvideo[height<={video_quality}]+bestaudio/best[height<={video_quality}]\" {target_url}"

# Execute the yt-dlp command
subprocess.run(yt_dlp_command, shell=True)
