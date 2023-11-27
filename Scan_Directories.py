import os
import webbrowser

filelist = open("GAMES_DIRECTORIES_AND_FILES.txt", "w")

countd = countf = lines = 0

printlist = list()


# BME = Beginning End
def ignoredItems(pathname, FolderOnly=False):
    ignoredFiles = [".gitignore", ".pyc", ".coverage"]

    ignoredFolders = ["__pycache__", "Deprecated", ".git", ".vscode", ".pytest_cache"]

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
                if tFile.endswith(".py"):
                    with open(tFile, "r") as document:
                        temp = len(document.read().split("\n"))
                        lines += temp
            except:
                continue
            countf += 1
    except:
        continue


HEADER_WIDTH = 26
dir_count = f" Total Directories: {str(countd)}".center(HEADER_WIDTH, " ")
file_count = f" Files: {str(countf)}".center(HEADER_WIDTH, " ")
line_count = f" Lines: {str(lines)}".center(HEADER_WIDTH, " ")

header = f"""FUNCLG Directories and Files

+{'='*(HEADER_WIDTH+2)}+
| {dir_count} |
| {file_count} |
| {line_count} |
+{'='*(HEADER_WIDTH+2)}+
"""

filelist.write(header)
filelist.write("\n")

for x in printlist:
    filelist.write(x)
    filelist.write("\n")

filelist.close()

print(header)
