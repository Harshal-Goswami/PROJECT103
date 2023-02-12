import sys
import os
import random
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:\Users\DELL"
to_dir = "C:\Users\DELL\Downloads"

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.jfif'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt']
}

class FileMovementHandler(FileSystemEventHandler):
   def on_created(self, event):

    name,extension = os.path.splitext(event.src_path)

    path1 = from_dir + '/' + file_name
    path2 = to_dir + '/' + key
    path3 = to_dir + '/' + key + '/' + file_name
    
    time.sleep(3)

    if os.path.exists(to_dir+'/'+key):

        if os.path.exists(path2):
            print("Moving "+ file_name + ".............")
            shutil.move(path1, path3)

        else :
            os.makedirs(path2)
            print("Moving "+ file_name + ".............")
            shutil.move(path1, path3)

    print(event)

event_handler = FileMovementHandler()   

observer = Observer()
observer.schedule(event_handler, from_dir, recursive=True)
observer.start()

try:
    while True:
        time.sleep(2)
        print("running......")
except KeyboardInterrupt:
        print("stopped !")
        observer.stop()