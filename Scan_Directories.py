import os
import webbrowser

filelist = open("GAMES_DIRECTORIES_AND_FILES.txt", "w")

countd = countf = lines = 0

printlist = list()


# BME = Beginning End
def ignoredItems(pathname, FolderOnly=False):
    ignoredFiles = [".gitignore", ".pyc", "lib64", "pyvenv.cfg"]

    ignoredFolders = [
        "__pycache__",
        "Deprecated",
        "lib",
        "include",
        "share",
        "bin",
        ".git",
        ".vscode",
    ]

    if FolderOnly:
        ignores = ignoredFolders
    else:
        ignores = ignoredFiles + ignoredFolders

    for ignore in ignores:
        if True in (True for x in ("__pycache__", ".git") if x in pathname):
            return True
        if pathname.startswith("./" + ignore):
            return True
        if not FolderOnly and pathname.endswith(ignore):
            return True
    return False


for root, dirs, files in os.walk("."):
    try:
        for name in dirs:
            if ignoredItems(os.path.join(root, name), True):
                continue
            else:
                printlist.append(os.path.join(root, name))
            countd += 1
        for file in files:
            if ignoredItems(os.path.join(root, file)):
                continue
            printlist.append(os.path.join(root, file))
            try:
                tFile = os.path.join(root, file)
                with open(tFile, "r") as document:
                    temp = len(document.read().split("\n"))
                    lines += temp
            except:
                continue
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

print("Total Lines:", lines)
filelist.close()

print("+==============================+")
print(f"|{str('Total Directories: ' + str(countd)).center(30)}|")
print(f"|{str('Files: ' + str(countf)).center(30)}|")
print("+==============================+")

# webbrowser.open("GAMES_DIRECTORIES_AND_FILES.txt")
