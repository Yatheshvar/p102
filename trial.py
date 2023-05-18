import os
import shutil

from_dir ="C:/Users/yathe/Downloads"
to_dir="C:/Users/yathe/OneDrive/Documents"

list_of_files = os.listdir(from_dir)
#print(list_of_files)

for files in list_of_files:
    name, extension =os.path.splitext(files)
    #print(name)
    #print(extension)

    if extension == " ":
        continue
    if extension in ['.pdf']:

        path1 = from_dir + '/' + files                       # Example path1 : Downloads/ImageName1.jpg        
        path2 = to_dir + '/' + "Docs"                     # Example path2 : D:/My Files/Image_Files      
        path3 = to_dir + '/' + "Docs" + '/' + files  # Example path3 : D:/My Files/Image_Files/ImageName1.jpg
        #print("path1 " , path1)
        #print("path3 ", path3)

        # Check if Folder/Directory Path Exists Before Moving
        # Else make a NEW Folder/Directory Then Move
        if os.path.exists(path2):
          print("Moving " + files + ".....")

          # Move from path1 ---> path3
          shutil.move(path1, path3)

        else:
          os.makedirs(path2)
          print("Moving " + files+ ".....")
          shutil.move(path1, path3)




