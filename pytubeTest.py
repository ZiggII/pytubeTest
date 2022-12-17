from pytube import YouTube
from pytube.cli import on_progress  
from pathlib import Path
import os

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


#open a path file and create a variable for its contents
try:
    opened_file = open("pathFile.txt", "r")
except FileNotFoundError as e:
    print(e)
    specifyOutputPath()
    opened_file = open("pathFile.txt", "r")
except:
    print("Error, failed to open path file")

path_file_content = opened_file.read()
#-------------------------------


#Getting infromation about the video from the link
printAgain1 = True
while printAgain1 == True:
    try:
        myVideo = YouTube(input("Enter the video link: "))
        printAgain1 = False
    except:
        print("Try again")
        printAgain1 = True
#-----------------------

stream = myVideo.streams
print(myVideo.title)

for stream in myVideo.streams: 
    print(f"{round(stream.filesize/1024/1024, 3)}\t{stream.resolution}\t{stream.itag}\t{stream.parse_codecs()}")

downloadITag = None
printAgain2 = True
while printAgain2 == True and downloadITag != "exit":
    try:
        downloadITag = input("Type exit to quit\nChoose the video and write the iTag: ")

        whatToDownload = myVideo.streams.get_by_itag(downloadITag)
        #why is it downloading as video????? Not sound????
        whatToDownload.download(output_path=path_file_content)
        printAgain2 = False
    except:
        print("Try again")
        printAgain2 = True

print("Download finished")


#need to know what filetype it is, can be other than mp4
#change extension from mp4 to mp3
if whatToDownload.video_codec is None:
    continue_loop1 = True
    while continue_loop1 is True:
        convertToMp3 = input("Do you want to change the file format from mp4 to mp3? (y/n)\nType your choice: ")
        if convertToMp3 == "y" or convertToMp3 == "n" or convertToMp3 == "exit":
            continue_loop1 = False
        else:
            print("Invalid input, try again")
    if convertToMp3 == "y":
        try:
            folder_path = path_file_content
            old_video_name = myVideo.title + ".mp4"
            new_video_name = myVideo.title + ".mp3"
            Folder_path = Path(folder_path)
            old_path = Folder_path / old_video_name
            new_path = Folder_path / new_video_name
            os.rename(old_path, new_path)
            print("File format change succesfull")
        except:
            print("failed to change the file format")
#-----------------------------------

if whatToDownload.audio_codec is None:
    continue_loop2 = True
    while continue_loop2 is True:
        download_audio = input("You only downloaded vieo, do you want to also download audio and merge the two together? (y/n)\nType your choice: ")
        if download_audio == "y" or download_audio == "n" or download_audio == "exit":
            continue_loop2 = False
        else:
            print("Invalid input, try again")
    if download_audio == "y":
        for stream in myVideo.streams:
            if stream.resolution is None:
                print(f"{round(stream.filesize/1024/1024, 3)}\t{stream.itag}\t{stream.parse_codecs()}")
        
        printAgain3 = True
        while printAgain3 == True:
            try:
                downloadITag = input("Type exit to quit\nChoose the video and write the iTag: ")

                whatToDownload = myVideo.streams.get_by_itag(downloadITag)
                whatToDownload.download(output_path=path_file_content)
                printAgain3 = False
            except:
                print("Try again")
                printAgain3 = True
        
        


opened_file.close()
print("finished")



#print file format as well
#bypass apge restrictions
#merge audio and video