import pytube
from pytube import YouTube

myVideo = YouTube("https://www.youtube.com/watch?v=Ctqi5Y4X-jA")


stream = myVideo.streams

for stream in myVideo.streams:
    print(f"{stream.filesize/1024/1024}--{stream.resolution}--{stream.itag}")

downloadITag = input("Now choose the video and write the iTag: ")    

whatToDownload = myVideo.streams.get_by_itag(downloadITag)
whatToDownload.download