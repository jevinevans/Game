import os
import webbrowser

filelist = open("GAMES_DIRECTORIES_AND_FILES.txt", "w")

countd = countf = words = 0

printlist = list()

for root, dirs, files in os.walk("."):
    try:
        for name in dirs:
            if os.path.join(root,name)[0:3] == ".\.": continue
            #filelist.write("=====DIRECTORIES=====\n")
            printlist.append(os.path.join(root, name))
            # filelist.write("\n")
            countd += 1
        for file in files:
            if os.path.join(root,name)[0:3] == ".\.": continue
            # filelist.write("=====FILES=====\n")
            printlist.append(os.path.join(root,file))
            try:
                tFile = os.path.join(root, file)
                with open(tFile, "r") as document:
                    temp = len(document.read().split("\n"))
                    words += temp
                    print(temp, end=" ")
                    print(tFile)
            except:
                continue
            # filelist.write("\n")
            countf += 1
    except:
        continue
    
filelist.write("+==========================================+\n")
filelist.write("|\tTotal Directories: ")
filelist.write(str(countd))
filelist.write("\t\t\t|\n|\tFiles: ")
filelist.write(str(countf))
filelist.write("\t\t\t\t|\n")
filelist.write("+==========================================+\n")

printlist.sort()
filelist.write("\n")

for x in printlist:
    filelist.write(x)        
    filelist.write("\n")

print("Total Lines:", words)
filelist.close()

webbrowser.open("GAMES_DIRECTORIES_AND_FILES.txt")