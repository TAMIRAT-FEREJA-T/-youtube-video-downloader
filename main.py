# pip install yt-dlp

import yt_dlp

url = input("enter the vedio URL: ")
ydl_opts = {}

try:
  with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
    print("vedio downloaded successfully.")
except Exception as e:
  print("Error downloading video: ", e)
