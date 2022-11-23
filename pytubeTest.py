from pytube import YouTube

myVideo = YouTube(input("Enter the video link: "))

stream = myVideo.streams

try:
    opened_file = open("pathFile.txt", "r")
except FileNotFoundError:
    print("Fail, try creating a path file, for that restart application and select the option...")

for stream in myVideo.streams:
    print(f"{stream.filesize/1024/1024}--{stream.resolution}--{stream.itag}")

downloadITag = None
printAgain = True
while printAgain == True and downloadITag != "exit":
    try:
        downloadITag = input("Now choose the video and write the iTag: ")    

        whatToDownload = myVideo.streams.get_by_itag(downloadITag)
        #find a way to specify output path
        whatToDownload.download(output_path=opened_file.read())
        printAgain = False
    except:
        print("Try again")
        printAgain = True