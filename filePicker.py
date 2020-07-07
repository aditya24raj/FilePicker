import os
import re



def GenerateDirDict(path):
	try:
		dirList=sorted(os.listdir(path))
	except PermissionError:
		print("Permission Denied!")
		exit()
	
	print("\n",path,"\n")
	dirDict={"..":"Previous Directory"}
	for number,name in zip(range(len(dirList)),dirList):
		dirDict[str(number)]=name
	return dirDict
	
def Choice(path,dirDict):
	for k,v in dirDict.items():
		if os.path.isdir(v):
			print("  ",k,v,"[Dir]")
		else:
			print("  ",k,v)

	
	selection=input("\n:").split(",")
	selectedFiles=[]
	
	for choiceNum in selection:
		choiceNum=choiceNum.strip()
		try:
			choice=dirDict[choiceNum]
			if choice=="Previous Directory" or os.path.isdir(choice):
				return (choice, False)	
				
			else:
				selectedFiles.append(path+"/"+choice)
		
		except KeyError:
			print("InValid Choice:",choiceNum)
			selection.remove(choiceNum)
			continue
	
	return (selectedFiles,True)

def DirNavigate(path,choice):
	if choice=="Previous Directory":
		newPath=re.findall("(.+)+/.+",path)[0]
	else:
		newPath=path+"/"+choice
	
	return newPath


def FilePicker():
	path=os.getcwd()
	picked=(None,False)
	
	while True:
		dirDict=GenerateDirDict(path)
		picked=Choice(path,dirDict)
		
		if picked[1]:
			break
		else:
			path=DirNavigate(path,picked[0])
			try:
				os.chdir(path)
			except PermissionError:
				print("permission denied!")
				exit()
			
	return picked[0]
	


"""
FilePicker

Directly changing directory will loose
previous selections.

To preserve previous selections,
select all needed files from current 
directory then hit enter, select y, and
navigate to desired directory and then 
select necessary files.

"""


def SelectedFiles():
	selectedFiles=[]
	while True:
		for files in FilePicker():
			selectedFiles.append(files)
		
		if input("\nPick More[y/n]: ")=="y":
			continue
		
		else:
			print("\n")
			return selectedFiles
			
		
		
		

	
	
	
	
	
	
	
	
	
	
	
	
	
	











