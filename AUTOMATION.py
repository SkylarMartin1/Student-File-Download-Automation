import os
from os.path import splitext, exists, join
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import shutil
import sys
import os
import DateAutomation
import time
import datetime
import os
import threading


source_dir = "C:/Users/skyla/Downloads"
dest_dir_music = "C:/Users/skyla/Music"
dest_dir_image = "C:/Users/skyla/OneDrive/Pictures"
dest_dir_video = "C:/Users/skyla/Videos"
dest_dir_pdf = ""

image_extensions = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw",
                    ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"]
video_extensions = [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg",
                    ".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd"]
audio_extensions = [".m4a", ".flac", ".mp3", ".wav", ".wma", ".aac"]
document_extensions = [".doc", ".docx", ".odt",
                       ".pdf", ".xls", ".xlsx", ".ppt", ".pptx"]
sunday_times = [
    "2025-04-20 23:59:59", "2025-05-11 23:59:59", "2025-05-18 23:59:59", "2025-05-25 23:59:59",
    "2025-06-01 23:59:59", "2025-06-08 23:59:59", "2025-06-15 23:59:59", "2025-06-22 23:59:59",
    "2025-07-06 23:59:59", "2025-07-13 23:59:59", "2025-07-20 23:59:59", "2025-07-27 23:59:59",
    "2025-08-03 23:59:59", "2025-08-24 23:59:59", "2025-08-31 23:59:59", "2025-09-07 23:59:59", 
    "2025-09-14 23:59:59", "2025-09-21 23:59:59", "2025-09-28 23:59:59"
    ]


def makeUnique(dest, name):
    filename, extension = splitext(name)
    counter = 1
    while exists(f"{dest}/{name}"):
        name = f"{filename}({str(counter)}){extension}"
        counter += 1
    
    return name

def move(dest, entry, name):
    file_exists = os.path.exists(f"{dest}/{name}")
    print(f"{dest}/{name}")
    if file_exists:
        unique_name = makeUnique(dest, name)
        oldName = join(dest, name)
        newName = join(dest, unique_name)
        os.rename(oldName, newName)
    shutil.move(entry, dest)



class MoveHandler(FileSystemEventHandler):
    def __init__(self):
        self.directory_name = self.create_pdf()
        if self.directory_name:
            self.process_files(self.directory_name)  # manual call for initial processing

    def on_modified(self, event):
        if self.directory_name:
            self.process_files(self.directory_name)

    def process_files(self, directory_name):
        with os.scandir(source_dir) as entries:
            for entry in entries:
                name = entry.name
                self.check_music_files(entry, name)
                self.check_image_files(entry, name)
                self.check_video_files(entry, name)
                self.check_pdf_files(entry, name, directory_name)
    
    def create_pdf(self):
        is_running = True

        while is_running:
            current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            if current_datetime == sunday_times[0]:
                directory_name = "C:/Users/skyla/OneDrive/Documents/PDF DOCUMENTATION/Block 2 Week 5"
                createdirectory(directory_name)
                return directory_name
            
            elif current_datetime == "2025-05-05 14:28:00":
                directory_name = "C:/Users/skyla/OneDrive/Documents/PDF DOCUMENTATION/Testing2"  #testing file
                createdirectory(directory_name)
                return directory_name

            elif current_datetime == sunday_times[1]:
                directory_name = "C:/Users/skyla/OneDrive/Documents/PDF DOCUMENTATION/Block 3 Week 1"
                createdirectory(directory_name)
                return directory_name

            elif current_datetime == sunday_times[2]:
                directory_name = "C:/Users/skyla/OneDrive/Documents/PDF DOCUMENTATION/Block 3 Week 2"
                createdirectory(directory_name)
                return directory_name

            elif current_datetime == sunday_times[3]:
                directory_name = "C:/Users/skyla/OneDrive/Documents/PDF DOCUMENTATION/Block 3 Week 3"
                createdirectory(directory_name)
                return directory_name

            elif current_datetime == sunday_times[4]:
                directory_name = "C:/Users/skyla/OneDrive/Documents/PDF DOCUMENTATION/Block 3 Week 4"
                createdirectory(directory_name)
                return directory_name

            elif current_datetime == sunday_times[5]:
                directory_name = "C:/Users/skyla/OneDrive/Documents/PDF DOCUMENTATION/Block 3 Week 5"
                createdirectory(directory_name)
                return directory_name

            elif current_datetime == sunday_times[6]:
                directory_name = "C:/Users/skyla/OneDrive/Documents/PDF DOCUMENTATION/Block 3 Week 6"
                createdirectory(directory_name)
                return directory_name

            elif current_datetime == sunday_times[7]:
                directory_name = "C:/Users/skyla/OneDrive/Documents/PDF DOCUMENTATION/Block 3 Week 7"
                createdirectory(directory_name)
                return directory_name

            elif current_datetime == sunday_times[8]:
                directory_name = "C:/Users/skyla/OneDrive/Documents/PDF DOCUMENTATION/Block 4 Week 1"
                createdirectory(directory_name)
                return directory_name

            elif current_datetime == sunday_times[9]:
                directory_name = "C:/Users/skyla/OneDrive/Documents/PDF DOCUMENTATION/Block 4 Week 2"
                createdirectory(directory_name)
                return directory_name

            elif current_datetime == sunday_times[10]:
                directory_name = "C:/Users/skyla/OneDrive/Documents/PDF DOCUMENTATION/Block 4 Week 3"
                createdirectory(directory_name)
                return directory_name
            
            elif current_datetime == sunday_times[11]:
                directory_name = "C:/Users/skyla/OneDrive/Documents/PDF DOCUMENTATION/Block 4 Week 4"
                createdirectory(directory_name)
                return directory_name
            
            elif current_datetime == sunday_times[12]:
                directory_name = "C:/Users/skyla/OneDrive/Documents/PDF DOCUMENTATION/Block 4 Week 5"
                createdirectory(directory_name)
                return directory_name
            
            elif current_datetime == sunday_times[13]:
                directory_name = "C:/Users/skyla/OneDrive/Documents/PDF DOCUMENTATION/Block 5 Week 1"
                createdirectory(directory_name)
                return directory_name
            
            elif current_datetime == sunday_times[14]:
                directory_name = "C:/Users/skyla/OneDrive/Documents/PDF DOCUMENTATION/Block 5 Week 2"
                createdirectory(directory_name)
                return directory_name

            elif current_datetime == sunday_times[15]:
                directory_name = "C:/Users/skyla/OneDrive/Documents/PDF DOCUMENTATION/Block 5 Week 3"
                createdirectory(directory_name)
                return directory_name
            
            elif current_datetime == sunday_times[16]:
                directory_name = "C:/Users/skyla/OneDrive/Documents/PDF DOCUMENTATION/Block 5 Week 4"
                createdirectory(directory_name)
                return directory_name
            
            elif current_datetime == sunday_times[17]:
                directory_name = "C:/Users/skyla/OneDrive/Documents/PDF DOCUMENTATION/Block 5 Week 5"
                createdirectory(directory_name)
                return directory_name
            
            elif current_datetime == sunday_times[18]:
                directory_name = "C:/Users/skyla/OneDrive/Documents/PDF DOCUMENTATION/Block 5 Week 6"
                createdirectory(directory_name)
                return directory_name
            
            elif current_datetime == "2025-04-19 16:15:00":
                directory_name = "C:/Users/skyla/OneDrive/Documents/PDF DOCUMENTATION/Test"
                createdirectory(directory_name)
                return directory_name
                
    
                
    
        
    def check_music_files(self, entry, name):
        for audio_extension in audio_extensions:
            if name.endswith(audio_extension) or name.endswith(audio_extension.upper()):
                dest = dest_dir_music
                move(dest, entry, name)
                logging.info(f"Moved video file: {name}")
    def check_pdf_files(self, entry, name, directory_name):
        for document_extension in document_extensions:
            if name.endswith(document_extension) or name.endswith(document_extension.upper()):
                dest = directory_name
                move(dest, entry, name)
                logging.info(F"Moved document file: {name}")
    def check_image_files(self, entry, name):
        for image_extension in image_extensions:
            if name.endswith(image_extension) or name.endswith(image_extension.upper()):
                dest = dest_dir_image
                move(dest, entry, name)
                logging.info(F"Moved image file: {name}")
    def check_video_files(self, entry, name):
        for video_extension in video_extensions:
            if name.endswith(video_extension) or name.endswith(video_extension.upper()):
                dest = dest_dir_video
                move(dest, entry, name)
                logging.info(F"Moved video file: {name}")
        
def createdirectory(directory_name):
        try:
            os.mkdir(directory_name)
            print(f"Directory '{directory_name}' created successfully.")
        except FileExistsError:
            print(f"Directory '{directory_name}' already exists.")
        except PermissionError:
            print(f"Permission denied: Unable to create '{directory_name}'.")
        except Exception as e:
            print(f"An error occurred: {e}") 



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    
    # Start watchdog observer
    event_handler = MoveHandler()
    observer = Observer()
    observer.schedule(event_handler, source_dir, recursive=True)
    observer.start()

    # Start background thread for scheduled directory creation
    def schedule_directory_creation(handler):
        while True:
            new_dir = handler.create_pdf()
            if new_dir:
                handler.directory_name = new_dir
            time.sleep(1)

    thread = threading.Thread(target=schedule_directory_creation, args=(event_handler,))
    thread.daemon = True
    thread.start()

    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()        
            
