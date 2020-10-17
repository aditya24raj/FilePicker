import os, stat
import re



print("\nFilePicker: Make selection using numbers,seperated by commas\n")

defaultpath = os.getcwd() # default path to use if supplied path is bad
defaultPermission = "r" # default permission code to be used if supplied permission is bad
filePickerSelection = []
features = {
    ".." : "Go To Previous Directory",
    "a " : "Select All",
    "r " : r"Select By Regex, r regex, Ex: r .*\.py"
}




# print information about selection methods
def printFeatures(features):
    print("\n")
    for k,v in features.items():
        print("    {}  {}".format(k,v))
    print("\n",end="")
    



# print all files/folders having given permission, with a number to select them, return the number with crossponding object as dict

def PrintAndReturnAllEntries(path, permission):
    global defaultpath
    global defaultPermission
    global features
    allEntryDict = {} # to store all objects(files/folders) with crossponding number(entryPosition)
    entryPosition = "0"

    try:
        os.chdir(path) # useful to change directory to make sure it exists and can be accessed if not revert to default path
        entries = os.scandir(os.getcwd()) # get all files/folder in current directory

        print("\nPath:",path,end="")
        printFeatures(features)

        for entry in entries:

            # get st_mode(int) convert it to string format(rw-rw-rw) and get permission for others, last 3 char
            entryPermission = stat.filemode(entry.stat().st_mode)[-3:].strip("-")

            if permission in entryPermission:

                if entry.is_dir():
                    print("    {}  {} [DIR]".format(entryPosition, entry.name))
                    allEntryDict[entryPosition] = entry
                    # adding entry to get all its features rather just entry name or path, 
                    # with entryPosition as key for selecting it based on the number 

                else:
                    print("    {}  {}".format(entryPosition, entry.name))
                    allEntryDict[entryPosition] = entry

                entryPosition=str(int(entryPosition)+1)
                # change entry position by after every acceptable entry
        
        
        assert(allEntryDict) # check if it is empty
    
    except (NotADirectoryError, FileNotFoundError) as e: # if given path is inaccesible revert to default path
        print("WARNING:",e)
        print("WARNING: Using default path:",defaultpath)
        allEntryDict = PrintAndReturnAllEntries(defaultpath, permission)
    
    except AssertionError as e:
        if entries: # allEntryDict was empty because of bad permission, as there were entries but were ignored because of permission errors
            print("WARNING: No files/folders with permission:",repr(permission))
            print("WARNING: Using default permission:",defaultPermission)
            allEntryDict = PrintAndReturnAllEntries(path, defaultPermission)

    return allEntryDict


# various selection methods

# select by regex

def SelectRegex(allEntryDict, regex):
    selectedDir, selectedFiles = [], []

    for _, entry in allEntryDict.items():
        if re.match(regex, entry.name):
            if entry.is_dir():
                selectedDir.append(entry.path)
            else:
                selectedFiles.append(entry.path)
    
    return(selectedDir, selectedFiles)


def SelectAll(allEntryDict):
    selectedDir, selectedFiles = [], []

    for _, entry in allEntryDict.items():
        if entry.is_dir():
            selectedDir.append(entry.path)
        else:
            selectedFiles.append(entry.path)

    return(selectedDir, selectedFiles)
       

# get input from user and return path of selected entry


def GetUserInputAndGenerateSelection(allEntryDict):
    selectedDir, selectedFiles = [], []

    choices = input("\n: ").split(",")

    for choice in choices:
        try:
            choice = choice.strip()
            assert(len(choice)>0)
        except AssertionError:
            continue

        if choice == "..":
            selectedDir.append(os.path.split(os.getcwd())[0])
            
        elif choice == "a":
            selectedDir, selectedFiles = SelectAll(allEntryDict)
            return(selectedDir, selectedFiles)

        elif choice.startswith("r "):
            if re.match(r"^r\s[\S]+$", choice):
                regex=re.split(r"^r\s",choice)[1]
                regexSelection = SelectRegex(allEntryDict, regex)
                    
                if not regexSelection[0] and not regexSelection[1]:
                    print("WARNING: regex returned no matches")
                else:
                    selectedDir += regexSelection[0]
                    selectedFiles += regexSelection[1]
            else:
                print("ERROR: Invalid regex, {}".format(repr(choice[2:])))
        
        else:
            try:
                entry = allEntryDict[choice]
                if entry.is_dir():
                    selectedDir.append(entry.path)
                else:
                    selectedFiles.append(entry.path)

            except KeyError:
                print("ERROR: Invalid choice: {}".format(repr(choice)))

    return(selectedDir, selectedFiles)
           

# using above functions ask user for input while selection involves a directory
# once selection involves only files return file paths including all previously selected files' path


def FilePicker(path=defaultpath, permission=defaultPermission):
    global filePickerSelection

    allEntryDict = PrintAndReturnAllEntries(path, permission)
    selectedDir, selectedFiles =  GetUserInputAndGenerateSelection(allEntryDict)

    filePickerSelection = filePickerSelection+selectedFiles

    while selectedDir:
        for dir in selectedDir:
            selectedDir.remove(dir)
            try:
                FilePicker(dir, permission)
            except RecursionError as error:
                print("ERROR:",error)
    
    return filePickerSelection

































