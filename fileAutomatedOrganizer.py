from os import scandir 


import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

#local folders to monitor
source_dir = "/Users/ithai/Downloads"
destination_dir_music = "/Users/ithai/Music"
destination_dir_video = "/Users/ithai/Movies"
destination_dir_images = "/Users/ithai/Pictures"
destination_dir_documents = "/Users/ithai/Documents/"

#supported file types
video_extensions = [".avi", ".avchd", ".flv", ".mov", ".mp2", ".mp4", ".mp4v", ".m4v", ".mpe", ".mpeg", ".mpg", ".mpv", ".ogg", ".qt", ".swf", ".webm", ".wmv"]
audio_extensions = [".aac", ".flac", ".m4a", ".mp3", ".wav", ".wma"]
image_extensions = [".ai", ".arw", ".bmp", ".cr2", ".dib", ".eps", ".gif", ".heic", ".heif", ".ico", ".ind", ".indd", ".indt", ".j2k", ".jpf", ".jpf", ".jpe", ".jpeg", ".jfif", ".jfi", ".jif", ".jp2", ".jpm", ".jpx", ".jpe", ".jpg", ".k25", ".mj2", ".nrw", ".png", ".psd", ".raw", ".svg", ".svgz", ".tif", ".tiff", ".webp"]
document_extensions = [".doc", ".docx", ".odt", ".pdf", ".ppt", ".pptx", ".xls", ".xlsx"]






if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = source_dir
    event_handler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while observer.isAlive():
            observer.join(1)
    finally:
        observer.stop()
        observer.join()