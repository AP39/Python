"""
Allows the downloading of youtube video and audio from playlists or single pages.  Files saved in the same directory as the acetube.py file as .mp4 for video, .mp3 for audio only
For PLAYLIST make sure the playlist is listed as 'public'
Only for downloading videos you have the rights to
"""
import pytube
from pytube import Playlist
import re
import os
import os.path
import time

print("\nWELCOME to ACETUBE\n\nYOUTUBE VIDEO AND AUDIO DOWNLOADER\n")

def outro():
    outty = input("Press 1 to CONTINUE, any other key to EXIT\n  > > > ")
    if outty == "1":
        intro()
    else:
        print("BYE")
        exit(0)

def singlevideo():
    url = input("Please paste the URL of the SINGLE VIDEO you want to download\n  > > > ")
    youtube = pytube.YouTube(url)
    title = youtube.title
    print(f"Downloading: {title}")
    video = youtube.streams.get_highest_resolution().download()
    print("FINISHED DOWNLOADING!")
    outro()

def singleaudio():
    url = input("Please paste the URL of the SINGLE AUDIO you want to download\n  > > > ")
    youtube = pytube.YouTube(url)
    title = youtube.title
    print(f"Downloading: {title}")
    video = youtube.streams.get_audio_only().download()
    path = os.getcwd() + ('\\')
    for filename in os.listdir(path):
        main, extension = os.path.splitext(filename)
        if extension == ".mp4":
            old = path + filename
            new = path + filename[:-4] + ".mp3"
            os.rename(old, new)
        else:
            pass
    print("FINISHED DOWNLOADING!")
    outro()

def playlistvideo():
    url = input("Please paste the URL of the VIDEO PLAYLIST you want to download\n  > > > ")
    playlist = Playlist(url)
    playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

    lengthy = len(playlist.video_urls)
    print(f"There are {lengthy} videos in the playlist.")

    z = 1
    for video in playlist.videos:
        if z <= 10:
            title = video.title
            print(f"Downloading: {title}")
            video.streams.get_highest_resolution().download()
            z += 1
        else:
            time.sleep(20)
            z = 1
    print("FINISHED DOWNLOADING!")
    outro()

def playlistaudio():
    url = input("Please paste the URL of the PLAYLIST AUDIO you want to download\n  > > > ")
    playlist = Playlist(url)
    playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

    lengthy = len(playlist.video_urls)
    print(f"There are {lengthy} videos in the playlist.")

    z = 1
    for video in playlist.videos:
        if z <= 10:
            title = video.title
            print(f"Downloading: {title}")
            video.streams.get_audio_only().download()
            z += 1
        else:
            time.sleep(20)
            z = 1
    path = os.getcwd() + ('\\')
    for filename in os.listdir(path):
        main, extension = os.path.splitext(filename)
        if extension == ".mp4":
            old = path + filename
            new = path + filename[:-4] + ".mp3"
            os.rename(old, new)
        else:
            pass
    print("FINISHED DOWNLOADING!")
    outro()

def sorter(choice1, choice2):
    if choice1 == "2" and choice2 == "1":
        singlevideo()
    if choice1 == "2" and choice2 == "2":
        singleaudio()
    if choice1 == "1" and choice2 == "1":
        playlistvideo()
    if choice1 == "1" and choice2 == "2":
        playlistaudio()
    else:
        print("error")
        exit(0)

def intro():
    choice1 = input("Would you like to download a PLAYLIST or SINGLE video?\n  Press 1 for PLAYLIST\n  Press 2 for SINGLE\n  > > > ")
    choice2 = input("Would you like to download a VIDEO or AUDIO ONLY video?\n  Press 1 for VIDEO\n  Press 2 for AUDIO ONLY\n  > > > ")
    if choice1 == "1" or choice1 == "2":
        pass
    if choice2 == "1" or choice2 == "2":
        sorter(choice1, choice2)
    else:
        print("Please enter only 1 or 2")
        intro()

intro()
