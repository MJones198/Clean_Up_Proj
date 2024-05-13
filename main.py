"""
This script organizes files in the 'D:\Downloads' directory into subdirectories based on their file extensions. It creates the following subdirectories if they don't already exist:

- Audio
- Compressed
- Code
- Documents
- Images
- Softwares
- Videos
- Others

The script first defines lists of file extensions for each category, then iterates through all files in the 'D:\Downloads' directory, moving each file to the appropriate subdirectory based on its file extension.
"""
import os
import collections
from pprint import pprint


"""
Defines lists of file extensions for various file types, including audio, compressed, code, documents, images, software, videos, and other files. These lists are used to organize files in the 'D:\Downloads' directory into corresponding subdirectories.
"""
EXT_Audio =  ['aif','cda','mid','midi','mp3','mpa','ogg','wav','wma']
EXT_Compressed = ['7z','deb','pkg','rar','rpm', 'tar.gz','z', 'zip']
EXT_Code = ['js','jsp','html','ipynb','py','java','css', 'bat']
EXT_Documents = ['ppt','pptx','pdf','xls', 'xlsx','doc','docx','txt', 'tex', 'epub']
EXT_Images = ['bmp','gif .ico','jpeg','jpg','png','jfif','svg','tif','tiff']
EXT_Softwares = ['apk','bat','bin', 'exe','jar','msi','py']
EXT_Videos = ['3gp','avi','flv','h264','mkv','mov','mp4','mpg','mpeg','wmv']
EXT_Others = ['NONE', 'srt', 'torrent']


"""
Initializes the base directory path and creates the necessary subdirectories if they don't already exist. It also creates a dictionary to map file extensions to their corresponding file names.
"""
base_Path = os.path.expanduser(r'D:\Downloads')
dest_Directory = ['Audio', 'Compressed', 'Code', 'Documents', 'Images', 'Softwares', 'Videos', 'Others']
for d in dest_Directory:
    dir_path = os.path.join(base_Path, d)
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
        
files_mapping = collections.defaultdict(list)
files_list = os.listdir(base_Path)


for file_name in files_list:
    file_ext = file_name.split('.')[-1]
    files_mapping[file_ext].append(file_name)
    



"""
Organizes files in the 'D:\Downloads' directory into subdirectories based on their file extensions. It creates the following subdirectories if they don't already exist:

- Audio
- Compressed
- Code
- Documents
- Images
- Softwares
- Videos
- Others

The function iterates through all files in the 'D:\Downloads' directory, moving each file to the appropriate subdirectory based on its file extension.
"""
for file_ext, file_list in files_mapping.items():
    if file_ext in EXT_Compressed:
        for file in file_list:
            os.rename(os.path.join(base_Path, file), os.path.join(base_Path, 'Compressed', file))
            
    elif file_ext in EXT_Code:
        for file in file_list:
            os.rename(os.path.join(base_Path, file), os.path.join(base_Path, 'Code', file))
            
    elif file_ext in EXT_Audio:
        for file in file_list:
            os.rename(os.path.join(base_Path, file), os.path.join(base_Path, 'Audio', file))
                
    elif file_ext in EXT_Documents:
        for file in file_list:
            os.rename(os.path.join(base_Path, file), os.path.join(base_Path, 'Documents', file))
                
    elif file_ext in EXT_Images:
        for file in file_list:
            os.rename(os.path.join(base_Path, file), os.path.join(base_Path, 'Images', file))
                
    elif file_ext in EXT_Softwares:
        for file in file_list:
            os.rename(os.path.join(base_Path, file), os.path.join(base_Path, 'Softwares', file))
                
    elif file_ext in EXT_Videos:
        for file in file_list:
            os.rename(os.path.join(base_Path, file), os.path.join(base_Path, 'Videos', file))
                
    elif file_ext in EXT_Others:
        for file in file_list:
            os.rename(os.path.join(base_Path, file), os.path.join(base_Path, 'Others', file))
