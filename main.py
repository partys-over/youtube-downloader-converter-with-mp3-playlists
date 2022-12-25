#   NEW FEATURES
#   

print("Welcome to NeuralNine YouTube Downloader and Converter v0.2 Alpha")
print("Loading...")

import pytube
import youtube_downloader
import file_converter
from datetime import datetime
import os

print('''
What do you want?

(1) [MP4] Download YouTube Video(s)
(2) [MP4] Download YouTube Playlist
(3) [MP3] Download YouTube Video(s)
(4) [MP3] Download YouTube Playlist [NEW!]


Downloading copyrighted YouTube videos is illegal!
I am not responsible for your downloads! Go at your own risk!

''')

choice = input("Choice: ")

if choice == "1" or choice == "2":
    quality = input("Please choose a quality (low, medium, high, very high):")
    if choice == "2":
        link = input("Enter the link to the playlist: ")
        print("Downloading playlist...")
        ledate = (str(datetime.now()).partition(' ')[2] + ' ' + str(datetime.now()).partition(' ')[0])
        print('Songs will be placed in a folder called ' + str(ledate) + '.')
        os.mkdir(ledate)
        os.chdir(ledate)
        youtube_downloader.download_playlist(link, quality)
        print("Download finished!")
    if choice == "1":
        links = youtube_downloader.input_links()
        if len(links) >= 2:
            ledate = (str(datetime.now()).partition(' ')[2] + ' ' + str(datetime.now()).partition(' ')[0])
            print('Songs will be placed in a folder called ' + str(ledate) + '.')
            os.mkdir(ledate)
            os.chdir(ledate)
        for link in links:
            youtube_downloader.download_video(link, quality)
elif choice == "3":
    links = youtube_downloader.input_links()
    if len(links) >= 2:
        ledate = (str(datetime.now()).partition(' ')[2] + ' ' + str(datetime.now()).partition(' ')[0])
        print('Songs will be placed in a folder called ' + str(ledate) + '.')
        os.mkdir(ledate)
        os.chdir(ledate)
    for link in links:
        print("Downloading...")
        filename = youtube_downloader.download_video(link, 'low')
        print("Converting...")
        file_converter.convert_to_mp3(filename)
elif choice == "4":
        link = input("Enter the link to the playlist: ")
        print("Downloading playlist...")
        ledate = (str(datetime.now()).partition(' ')[2] + ' ' + str(datetime.now()).partition(' ')[0])
        print('Songs will be placed in a folder called ' + str(ledate) + '.')
        os.mkdir(ledate)
        os.chdir(ledate)
        youtube_downloader.download_mp3playlist(link, 'low')
        print("Download finished!")
else:
    print("Invalid input! Terminating...")
