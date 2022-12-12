from pytube import YouTube
from pytube.cli import on_progress  
from pathlib import Path

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
print(myVideo.title)

for stream in myVideo.streams:
    if stream.resolution is None:
        streamType = "Only audio"
        isVideo = False
        
    print(f"{round(stream.filesize/1024/1024, 3)}\t{stream.resolution}\t{stream.itag}\t{stream.parse_codecs()}")

#https://github.com/pytube/pytube/blob/master/pytube/streams.py line 90

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

if whatToDownload.video_codec is None:
    continue_loop = True
    while continue_loop is True:
        convertToMp3 = input("Do you want to change the file format from mp4 to mp3? (y/n)\nType your choice: ")
        if convertToMp3 == "y" or convertToMp3 == "n" or convertToMp3 == "exit":
            continue_loop = False
        else:
            print("Invalid input, try again")
    if convertToMp3 == "y":
        print(opened_file.read())
        path = Path(opened_file.read()) /  myVideo.title + ".mp4"
        path.rename(path.with_suffix('.mp3'))
        
opened_file.close()
print("finished")


#download as audio
#print file format as well
#bypass apge restrictions
#merge audio and video