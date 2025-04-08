#!/bin/bash

# Prompt for download directory
read -p "Enter the directory where you want to save the downloads: " save_dir

# Ask if it is a playlist or a single video
read -p "Is this a playlist or a single video? (playlist/video): " content_type

if [[ $content_type == "playlist" ]]; then
  # Prompt for the playlist URL
  read -p "Enter the playlist URL: " playlist_url
else
  # Prompt for the video URL
  read -p "Enter the video URL: " video_url
  read -p "Do you want to create a folder for this video? (yes/no): " create_folder
  if [[ $create_folder == "yes" ]]; then
    read -p "Enter the folder name: " folder_name
    save_dir="$save_dir/$folder_name"
    mkdir -p "$save_dir"
  fi
fi

# Prompt for whether to download subtitles
read -p "Do you want to download subtitles? (yes/no): " download_subs

if [[ $download_subs == "yes" ]]; then
  read -p "Enter the subtitle language (e.g., en, es, fr, de, it): " sub_lang
  read -p "Do you want to download auto-generated subtitles if manual ones are unavailable? (yes/no): " auto_subs
  read -p "Do you want to embed subtitles in the video? (yes/no): " embed_subs
  read -p "Which subtitle format do you want? (e.g., srt, vtt): " sub_format
fi

# Prompt for video format
read -p "Enter the desired video format (e.g., mp4, mkv, webm): " video_format

# Prompt for video quality
read -p "Enter the desired video quality (e.g., 144, 240, 360, 480, 720, 1080, 1440, 2160): " video_quality

# Build the yt-dlp command dynamically
if [[ $content_type == "playlist" ]]; then
  command="yt-dlp -o \"$save_dir/%(playlist_title)s/%(title)s.%(ext)s\""
  target_url="$playlist_url"
else
  command="yt-dlp -o \"$save_dir/%(title)s.%(ext)s\""
  target_url="$video_url"
fi

if [[ $download_subs == "yes" ]]; then
  command+=" --write-subs --sub-lang $sub_lang --convert-subs $sub_format"
  
  if [[ $auto_subs == "yes" ]]; then
    command+=" --write-auto-subs"
  fi
  
  if [[ $embed_subs == "yes" ]]; then
    command+=" --embed-subs"
  fi
fi

command+=" --merge-output-format $video_format -f \"bestvideo[height<=$video_quality]+bestaudio/best[height<=$video_quality]\" $target_url"

# Execute the command
eval $command

