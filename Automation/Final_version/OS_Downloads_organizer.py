from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os
import json
import shutil

class MyHandler(FileSystemEventHandler):
    def on_modified(self,event):
        for filename in os.listdir(folder_to_track):
            i=1
            if filename != "issacmiao_organizer":
                try:
                    extension = str(os.path.splitext(folder_to_track + "/" + filename)[1])
                    new_name = filename
                    # if extensions_folders[extension]=null:
                    #     extension=
                    file_exists = os.path.isfile(extensions_folders[extension] + "/" + new_name)
                    while file_exists:
                        i +=1
                        new_name = os.path.splitext(folder_to_track + "/" + new_name)[0] + str(i) + os.path.splitext(folder_to_track + "/" + new_name)[1] # filename + str(i)
                        new_name = new_name.split("/")[4]
                        file_exists = os.path.isfile(extensions_folders[extension] + "/" + new_name)
                    src = folder_to_track + "/" + filename
                    new_name = extensions_folders[extension] + "/" + new_name
                    os.rename(src, new_name)
                except Exception:
                    print(filename)

extensions_folders = {
    # No name
    # "noname":  "/Users/issacmiao/Downloads/issacmiao_organizer/other/uncategorized",
    # audio
    ".aif":    "/Users/issacmiao/Downloads/issacmiao_organizer/media/audio",
    ".cda":    "/Users/issacmiao/Downloads/issacmiao_organizer/media/audio",
    ".mid":    "/Users/issacmiao/Downloads/issacmiao_organizer/media/audio",
    ".midi":   "/Users/issacmiao/Downloads/issacmiao_organizer/media/audio",
    ".mp3":    "/Users/issacmiao/Downloads/issacmiao_organizer/media/audio",
    ".mpa":    "/Users/issacmiao/Downloads/issacmiao_organizer/media/audio",
    ".ogg":    "/Users/issacmiao/Downloads/issacmiao_organizer/media/audio",
    ".wav":    "/Users/issacmiao/Downloads/issacmiao_organizer/media/audio",
    ".wma":    "/Users/issacmiao/Downloads/issacmiao_organizer/media/audio",
    ".wpl":    "/Users/issacmiao/Downloads/issacmiao_organizer/media/audio",
    ".m3u":    "/Users/issacmiao/Downloads/issacmiao_organizer/media/audio",
    # text
    ".txt":    "/Users/issacmiao/Downloads/issacmiao_organizer/text/text_files",
    ".doc":    "/Users/issacmiao/Downloads/issacmiao_organizer/text/microsoft/word",
    ".docx":   "/Users/issacmiao/Downloads/issacmiao_organizer/text/microsoft/word",
    ".ppt":   "/Users/issacmiao/Downloads/issacmiao_organizer/text/microsoft/powerpoint",
    ".pptx":   "/Users/issacmiao/Downloads/issacmiao_organizer/text/microsoft/powerpoint",
    ".odt ":   "/Users/issacmiao/Downloads/issacmiao_organizer/text/text_files",
    ".pdf":    "/Users/issacmiao/Downloads/issacmiao_organizer/text/pdf",
    ".rtf":    "/Users/issacmiao/Downloads/issacmiao_organizer/text/text_files",
    ".tex":    "/Users/issacmiao/Downloads/issacmiao_organizer/text/text_files",
    ".wks ":   "/Users/issacmiao/Downloads/issacmiao_organizer/text/text_files",
    ".wps":    "/Users/issacmiao/Downloads/issacmiao_organizer/text/text_files",
    ".wpd":    "/Users/issacmiao/Downloads/issacmiao_organizer/text/text_files",
    # video
    ".3g2":    "/Users/issacmiao/Downloads/issacmiao_organizer/media/video",
    ".3gp":    "/Users/issacmiao/Downloads/issacmiao_organizer/media/video",
    ".avi":    "/Users/issacmiao/Downloads/issacmiao_organizer/media/video",
    ".flv":    "/Users/issacmiao/Downloads/issacmiao_organizer/media/video",
    ".h264":   "/Users/issacmiao/Downloads/issacmiao_organizer/media/video",
    ".m4v":    "/Users/issacmiao/Downloads/issacmiao_organizer/media/video",
    ".mkv":    "/Users/issacmiao/Downloads/issacmiao_organizer/media/video",
    ".mov":    "/Users/issacmiao/Downloads/issacmiao_organizer/media/video",
    ".mp4":    "/Users/issacmiao/Downloads/issacmiao_organizer/media/video",
    ".mpg":    "/Users/issacmiao/Downloads/issacmiao_organizer/media/video",
    ".mpeg":   "/Users/issacmiao/Downloads/issacmiao_organizer/media/video",
    ".rm":     "/Users/issacmiao/Downloads/issacmiao_organizer/media/video",
    ".swf":    "/Users/issacmiao/Downloads/issacmiao_organizer/media/video",
    ".vob":    "/Users/issacmiao/Downloads/issacmiao_organizer/media/video",
    ".wmv":    "/Users/issacmiao/Downloads/issacmiao_organizer/media/video",
    # images
    ".ai":     "/Users/issacmiao/Downloads/issacmiao_organizer/media/images",
    ".bmp":    "/Users/issacmiao/Downloads/issacmiao_organizer/media/images",
    ".gif":    "/Users/issacmiao/Downloads/issacmiao_organizer/media/images",
    ".jpg":    "/Users/issacmiao/Downloads/issacmiao_organizer/media/images",
    ".jpeg":   "/Users/issacmiao/Downloads/issacmiao_organizer/media/images",
    ".png":    "/Users/issacmiao/Downloads/issacmiao_organizer/media/images",
    ".ps":     "/Users/issacmiao/Downloads/issacmiao_organizer/media/images",
    ".psd":    "/Users/issacmiao/Downloads/issacmiao_organizer/media/images",
    ".svg":    "/Users/issacmiao/Downloads/issacmiao_organizer/media/images",
    ".tif":    "/Users/issacmiao/Downloads/issacmiao_organizer/media/images",
    ".tiff":   "/Users/issacmiao/Downloads/issacmiao_organizer/media/images",
    ".cr2":    "/Users/issacmiao/Downloads/issacmiao_organizer/media/images",
    # internet
    ".asp":    "/Users/issacmiao/Downloads/issacmiao_organizer/other/internet",
    ".aspx":   "/Users/issacmiao/Downloads/issacmiao_organizer/other/internet",
    ".cer":    "/Users/issacmiao/Downloads/issacmiao_organizer/other/internet",
    ".cfm":    "/Users/issacmiao/Downloads/issacmiao_organizer/other/internet",
    ".cgi":    "/Users/issacmiao/Downloads/issacmiao_organizer/other/internet",
    ".pl":     "/Users/issacmiao/Downloads/issacmiao_organizer/other/internet",
    ".css":    "/Users/issacmiao/Downloads/issacmiao_organizer/other/internet",
    ".htm":    "/Users/issacmiao/Downloads/issacmiao_organizer/other/internet",
    ".js":     "/Users/issacmiao/Downloads/issacmiao_organizer/other/internet",
    ".jsp":    "/Users/issacmiao/Downloads/issacmiao_organizer/other/internet",
    ".part":   "/Users/issacmiao/Downloads/issacmiao_organizer/other/internet",
    ".php":    "/Users/issacmiao/Downloads/issacmiao_organizer/other/internet",
    ".rss":    "/Users/issacmiao/Downloads/issacmiao_organizer/other/internet",
    ".xhtml":  "/Users/issacmiao/Downloads/issacmiao_organizer/other/internet",
    ".html":   "/Users/issacmiao/Downloads/issacmiao_organizer/other/internet",
    # compressed
    ".7z":     "/Users/issacmiao/Downloads/issacmiao_organizer/other/compressed",
    ".arj":    "/Users/issacmiao/Downloads/issacmiao_organizer/other/compressed",
    ".deb":    "/Users/issacmiao/Downloads/issacmiao_organizer/other/compressed",
    ".pkg":    "/Users/issacmiao/Downloads/issacmiao_organizer/other/compressed",
    ".rar":    "/Users/issacmiao/Downloads/issacmiao_organizer/other/compressed",
    ".rpm":    "/Users/issacmiao/Downloads/issacmiao_organizer/other/compressed",
    ".tar.gz": "/Users/issacmiao/Downloads/issacmiao_organizer/other/compressed",
    ".z":      "/Users/issacmiao/Downloads/issacmiao_organizer/other/compressed",
    ".zip":    "/Users/issacmiao/Downloads/issacmiao_organizer/other/compressed",
    # disc
    ".bin":    "/Users/issacmiao/Downloads/issacmiao_organizer/other/disc",
    # ".dmg":    "/Users/issacmiao/Downloads/issacmiao_organizer/other/disc",
    ".iso":    "/Users/issacmiao/Downloads/issacmiao_organizer/other/disc",
    ".toast":  "/Users/issacmiao/Downloads/issacmiao_organizer/other/disc",
    ".vcd":    "/Users/issacmiao/Downloads/issacmiao_organizer/other/disc",
    # data
    ".csv":    "/Users/issacmiao/Downloads/issacmiao_organizer/programming/database",
    ".dat":    "/Users/issacmiao/Downloads/issacmiao_organizer/programming/database",
    ".db":     "/Users/issacmiao/Downloads/issacmiao_organizer/programming/database",
    ".dbf":    "/Users/issacmiao/Downloads/issacmiao_organizer/programming/database",
    ".log":    "/Users/issacmiao/Downloads/issacmiao_organizer/programming/database",
    ".mdb":    "/Users/issacmiao/Downloads/issacmiao_organizer/programming/database",
    ".sav":    "/Users/issacmiao/Downloads/issacmiao_organizer/programming/database",
    ".sql":    "/Users/issacmiao/Downloads/issacmiao_organizer/programming/database",
    ".tar":    "/Users/issacmiao/Downloads/issacmiao_organizer/programming/database",
    ".xml":    "/Users/issacmiao/Downloads/issacmiao_organizer/programming/database",
    ".json":   "/Users/issacmiao/Downloads/issacmiao_organizer/programming/database",
    # executables
    ".apk":    "/Users/issacmiao/Downloads/issacmiao_organizer/other/executables",
    ".bat":    "/Users/issacmiao/Downloads/issacmiao_organizer/other/executables",
    ".com":    "/Users/issacmiao/Downloads/issacmiao_organizer/other/executables",
    ".exe":    "/Users/issacmiao/Downloads/issacmiao_organizer/other/executables",
    ".gadget": "/Users/issacmiao/Downloads/issacmiao_organizer/other/executables",
    ".jar":    "/Users/issacmiao/Downloads/issacmiao_organizer/other/executables",
    ".wsf":    "/Users/issacmiao/Downloads/issacmiao_organizer/other/executables",
    # calendars
    ".ics":    "/Users/issacmiao/Downloads/issacmiao_organizer/calendars",
    # fonts
    ".fnt":    "/Users/issacmiao/Downloads/issacmiao_organizer/other/fonts",
    ".fon":    "/Users/issacmiao/Downloads/issacmiao_organizer/other/fonts",
    ".otf":    "/Users/issacmiao/Downloads/issacmiao_organizer/other/fonts",
    ".ttf":    "/Users/issacmiao/Downloads/issacmiao_organizer/other/fonts",
    # presentations
    ".key":    "/Users/issacmiao/Downloads/issacmiao_organizer/text/presentations",
    ".odp":    "/Users/issacmiao/Downloads/issacmiao_organizer/text/presentations",
    ".pps":    "/Users/issacmiao/Downloads/issacmiao_organizer/text/presentations",
    # ".ppt":    "/Users/issacmiao/Downloads/issacmiao_organizer/text/presentations",
    # ".pptx":   "/Users/issacmiao/Downloads/issacmiao_organizer/text/presentations",
    # programming
    ".c":      "/Users/issacmiao/Downloads/issacmiao_organizer/programming/c&c++",
    ".class":  "/Users/issacmiao/Downloads/issacmiao_organizer/programming/java",
    ".java":   "/Users/issacmiao/Downloads/issacmiao_organizer/programming/java",
    ".py":     "/Users/issacmiao/Downloads/issacmiao_organizer/programming/python",
    ".sh":     "/Users/issacmiao/Downloads/issacmiao_organizer/programming/shell",
    ".h":      "/Users/issacmiao/Downloads/issacmiao_organizer/programming/c&c++",
    # spreadsheets
    ".ods":    "/Users/issacmiao/Downloads/issacmiao_organizer/text/microsoft/excel",
    ".xlr":    "/Users/issacmiao/Downloads/issacmiao_organizer/text/microsoft/excel",
    ".xls":    "/Users/issacmiao/Downloads/issacmiao_organizer/text/microsoft/excel",
    ".xlsx":   "/Users/issacmiao/Downloads/issacmiao_organizer/text/microsoft/excel",
    #Installation file
    ".dmg":   "/Users/issacmiao/Downloads/issacmiao_organizer/installation",
    # system
    ".bak":    "/Users/issacmiao/Downloads/issacmiao_organizer/text/other/system",
    ".cab":    "/Users/issacmiao/Downloads/issacmiao_organizer/text/other/system",
    ".cfg":    "/Users/issacmiao/Downloads/issacmiao_organizer/text/other/system",
    ".cpl":    "/Users/issacmiao/Downloads/issacmiao_organizer/text/other/system",
    ".cur":    "/Users/issacmiao/Downloads/issacmiao_organizer/text/other/system",
    ".dll":    "/Users/issacmiao/Downloads/issacmiao_organizer/text/other/system",
    ".dmp":    "/Users/issacmiao/Downloads/issacmiao_organizer/text/other/system",
    ".drv":    "/Users/issacmiao/Downloads/issacmiao_organizer/text/other/system",
    ".icns":   "/Users/issacmiao/Downloads/issacmiao_organizer/text/other/system",
    ".ico":    "/Users/issacmiao/Downloads/issacmiao_organizer/text/other/system",
    ".ini":    "/Users/issacmiao/Downloads/issacmiao_organizer/text/other/system",
    ".lnk":    "/Users/issacmiao/Downloads/issacmiao_organizer/text/other/system",
    ".msi":    "/Users/issacmiao/Downloads/issacmiao_organizer/text/other/system",
    ".sys":    "/Users/issacmiao/Downloads/issacmiao_organizer/text/other/system",
    ".tmp":    "/Users/issacmiao/Downloads/issacmiao_organizer/text/other/system"
        }

folder_to_track = "/Users/issacmiao/Downloads"
folder_destination="/Users/issacmiao/Downloads/issacmiao_organizer"
event_handler=MyHandler()
observer = Observer()
observer.schedule(event_handler,folder_to_track,recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()










