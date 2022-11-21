import pytube
from pytube import YouTube

myVideo = YouTube("https://www.youtube.com/watch?v=Ctqi5Y4X-jA")


stream = myVideo.streams
#itagOfStream = stream.
#print(stream.)

for stream in myVideo.streams:
    print(f"{stream.filesize/1024/1024}--{stream.resolution}--{stream.itag}")

downloadITag = input("NOw choose the video and write the iTag: ")    