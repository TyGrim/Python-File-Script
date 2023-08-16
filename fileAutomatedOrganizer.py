from os.path import splitext, exists, join
from os import scandir, rename 
from shutil import move


import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

#local folders to monitor
source_dir = "/Users/ithai/Downloads"
destination_dir_music = "/Users/ithai/Music"
destination_dir_videos = "/Users/ithai/Movies"
destination_dir_images = "/Users/ithai/Pictures"
destination_dir_documents = "/Users/ithai/Documents/"

#supported file types
video_extensions = [".avi", ".avchd", ".flv", ".mov", ".mp2", ".mp4", ".mp4v", ".m4v", ".mpe", ".mpeg", ".mpg", ".mpv", ".ogg", ".qt", ".swf", ".webm", ".wmv"]
audio_extensions = [".aac", ".flac", ".m4a", ".mp3", ".wav", ".wma"]
image_extensions = [".ai", ".arw", ".bmp", ".cr2", ".dib", ".eps", ".gif", ".heic", ".heif", ".ico", ".ind", ".indd", ".indt", ".j2k", ".jpf", ".jpf", ".jpe", ".jpeg", ".jfif", ".jfi", ".jif", ".jp2", ".jpm", ".jpx", ".jpe", ".jpg", ".k25", ".mj2", ".nrw", ".png", ".psd", ".raw", ".svg", ".svgz", ".tif", ".tiff", ".webp"]
document_extensions = [".doc", ".docx", ".odt", ".pdf", ".ppt", ".pptx", ".xls", ".xlsx"]

def change_filename(dest, name):
    filename, extension = splitext(name) 
    counter = 1
    
    while exists(f"{dest}/{name}"):
        name = f"{filename}({str(counter)}){extension}"
        counter =+ 1

    return name

class FileHandler(LoggingEventHandler):
    def on_modified(self, event):
        with scandir(source_dir) as entries:
            for entry in entries:
                name = entry.name
                self.check_audio_files(entry, name)
                self.check_video_files(entry, name)
                self.check_image_files(entry, name)
                self.check_document_files(entry, name)

def check_audio_files(self, entry, name):
    for audio_extension in audio_extensions:
        if name.endswith(audio_extension) or name.endwith(audio_extension.upper()):
            dest = destination_dir_music

def check_video_files(self, entry, name):
    for video_extension in video_extensions:
        if name.endswith(video_extension) or name.endswith(video_extension.upper()):
            dest = destination_dir_videos

def check_image_files(self, entry, name):
    for image_extension in image_extensions:
        if name.endwith(image_extension) or name.endswith(image_extension.upper()):
            dest = destination_dir_images

def check_document_files(self, entry, name):
    for document_extension in document_extensions:
        if name.endswith(document_extension) or name.endswith(document_extension.upper()):
            dest = destination_dir_documents


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = source_dir
    event_handler = FileHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while observer.isAlive():
            observer.join(1)
    finally:
        observer.stop()
        observer.join()