from pytube import YouTube
from pytube.cli import on_progress  

print("What do you want to do?\n1 - Download YouTube video\n2 - Create a path file\nexit to quit")
whatToDo = input("Type your choice: ")

def specifyOutputPath():
    openedFile = open("pathFile.txt", "w")
    outputPath = input("Paste the output path here: ")
    openedFile.write(outputPath)
    openedFile.close()

def progress_function(self,stream, chunk,file_handle, bytes_remaining):
    size = stream.filesize
    p = 0
    while p<=100:
        progress = p
        print(f"{p}%")
        p = size/(size-bytes_remaining)

while True:
    if whatToDo == "1":
        break
    elif whatToDo == "2":
        specifyOutputPath()
        break
    elif whatToDo == "exit":
        quit()
    else:
        whatToDo = input("Invalid input. (other than 1 or 2)\nTry again: ")

try:
    opened_file = open("pathFile.txt", "r")
except FileNotFoundError as e:
    print(e)
    specifyOutputPath()
except:
    print("Error, failed to open path file")

myVideo = YouTube(input("Enter the video link: "), on_progress_callback=on_progress)

stream = myVideo.streams

for stream in myVideo.streams:
    print(f"{stream.filesize/1024/1024}--{stream.resolution}--{stream.itag}--{stream.method}")

#https://github.com/pytube/pytube/blob/master/pytube/streams.py

downloadITag = None
printAgain = True
while printAgain == True and downloadITag != "exit":
    try:
        downloadITag = input("Type exit to quit\nChoose the video and write the iTag: ")

        whatToDownload = myVideo.streams.get_by_itag(downloadITag)
        #why is it downloading as video????? Not sound????
        whatToDownload.download(output_path=opened_file.read())
        printAgain = False
    except:
        print("Try again")
        printAgain = True

opened_file.close()
