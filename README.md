# FilePicker
It is a command-line utility to select files.

# Implementation
Place FilePicker.py in same folder as your python project and use it as follows:
```python
from FilePicker import FilePicker

selectedFiles = FilePicker(path, permission)
"""
                path:
                    -the directory path where you want to pick files
                    -if not supplied or if supplied path is bad(does not exists, inaccessible), defaultPath is used
                    -defaultPath is set to current working directory, can be changed in FilePicker.py
                    
                permission:
                    -is permission for others(not owner and not groups)
                    -can be a valid combination of rwx, only files/folders with given permission are shown
                    -if not specified or if specified permission is bad(invalid permission, nothing matches given permission), default permission is used
                    -defaultPermission is set to "r", can be changed in FilePicker.py
               
               selectedFiles:
                   -it will be a list with full path of selected files
"""
```

# Usage
FilePicker prints all files/folders, in the given path having supplied permission, with a number preceding it and a trailing "[DIR]" if its a folder:
```
0 file1
1 file2
2 folder1 [DIR]
3 folder2 [DIR]
```


## Selection Methods

### individual selection

Input numbers seperated by commas to select files/folders crossponding to those number, after selecting all files if there is a directory it will switch to that directory to offer selection.

### select all

Selects every entry listed, it is not recursive so if there is a directory in selection, after selecting all files, it will switch to that directory to offer selection there.

### regex selection

To select using regular expression, input regular expression in this format:

>r regularExpression

small "r",without quotes, followed by a whitespace then your regular expression.



