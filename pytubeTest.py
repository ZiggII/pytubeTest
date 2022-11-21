from pytube import YouTube

myVideo = YouTube(input("Enter the video link: "))


stream = myVideo.streams

for stream in myVideo.streams:
    print(f"{stream.filesize/1024/1024}--{stream.resolution}--{stream.itag}")

downloadITag = "llllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll"
printAgain = True
while printAgain == True and downloadITag != "exit":
    try:
        downloadITag = input("Now choose the video and write the iTag: ")    

        whatToDownload = myVideo.streams.get_by_itag(downloadITag)
        whatToDownload.download
        printAgain = False
    except:
        print("Try again")
        printAgain = True