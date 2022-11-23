from pytube import YouTube

print("What do you want to do?\n1 - Download YouTube video\n2 - Create a path file")
whatToDo = input("Type your choice: ")

def specifyOutputPath():
    openedFile = open("pathFile.txt", "w")
    outputPath = input("Paste the output path here: ")
    openedFile.write(outputPath)
    openedFile.close()

while True:
    if whatToDo == 1:
        break
    elif whatToDo == 2:
        specifyOutputPath()
        break
    else:
        whatToDo = input("Invalid input. (other than 1 or 2)\nTry again: ")

try:
    opened_file = open("pathFile.txt", "r")
except FileNotFoundError as e:
    print(e)
    specifyOutputPath()
except:
    print("Error, failed to open path file")

myVideo = YouTube(input("Enter the video link: "))

stream = myVideo.streams

for stream in myVideo.streams:
    print(f"{stream.filesize/1024/1024}--{stream.resolution}--{stream.itag}")

downloadITag = None
printAgain = True
while printAgain == True and downloadITag != "exit":
    try:
        downloadITag = input("Type exit to exit\nChoose the video and write the iTag: ")

        whatToDownload = myVideo.streams.get_by_itag(downloadITag)

        whatToDownload.download(output_path=opened_file.read())
        printAgain = False
    except:
        print("Try again")
        printAgain = True

opened_file.close()