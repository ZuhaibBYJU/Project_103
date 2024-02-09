import sys
import time
import random

import os
import shutil
import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/ultim/Downloads"
# Event Handler Class

class FileMovementHandler(FileSystemEventHandler): 
    
    def on_created(self, event):
        print(f"Hi,{event.src_path} has been created")
    
    def on_deleted(self, event):
        print(f"Hi,{event.src_path} has been deleted")
    
    def on_modified(self, event):
        print(f"Hi,{event.src_path} has been modified")

    def on_moved(self, event):
        print(f"Hi,{event.src_path} has been moved to {event.dest_path}")

# Initialize Event Handler Class
event_handler = FileMovementHandler()

# Initialize Observer
observer = Observer()

# Schedule the observer
observer.schedule(event_handler, from_dir, recursive=True)

# Start the observer
observer.start()

try: 
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("Stopped!")
    observer.stop()

   
    

        