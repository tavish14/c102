import os
import shutil
source="C:/Users/tejta/OneDrive/Desktop/Python/C102_assets-main"
dest = "C:/Users/tejta/OneDrive/Desktop/Python/C102_assets-main/test"
list_of_files=os.listdir(source)
for file in list_of_files:
    name,extension=os.path.splitext(file)
    if extension=='':
        continue
    if extension in ['.gif','.png','.jpg','.jpeg','.jfif']:
        path1=source+'/'+file
        path2=dest+'/'+"image_files"
        path3=dest+'/'+"image_files"+file
        if os.path.exists(path2):
            shutil.move(path1,path3)
        else:
            os.mkdir(path2)
            shutil.move(path1,path3)