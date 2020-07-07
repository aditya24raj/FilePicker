# FilePicker
cmd line file picker.
enter number shown beside the files/folders to choose them.
enter .. for previous directory.
returns a list with full file path of chosen files.

Note:
Directly changing directory will loose
previous selections. 
To preserve previous selections,
select all needed files from current
directory then hit enter, select y, and
navigate to desired directory and then 
select necessary files. 

# Usage
place filePicker.py in same directory 
and import using 

import filePicker
selectedFiles=filePicker.SelectedFiles()

selectedFiles will contain list of path  selected files
