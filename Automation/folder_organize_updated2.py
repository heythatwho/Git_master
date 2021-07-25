# purpose
# track desktop, if new file is added then move
# move files
# run in the background
# system for the file organization
    # --folders for each file type category (eg.images, video,audio, text.etc)
    # --within folders we need to organize by date
    # create subfolders with date as name something like:
    # 2019, 8.september, day? or file?

# need to find all file types to check what file has been added

from watchdog.observers import Observer
import time
import datetime 
from watchdog.events import FileSystemEventHandler
import os
import json
import shutil

class MyHandler(FileSystemEventHandler):
    # i = 1
    def on_modified(self,event):
        for filename in os.listdir(folder_to_track):
            i=1
            if filename !="issacmiao":
                try:
                    # split_name = filename.split(".")
                    # extension = str(os.path.splitext(folder_to_track + "/" + filename)[1])
                    new_name = filename
                    extension = "noname"
                    try:
                        extension = str(os.path.splitext(folder_to_track + "/" + filename)[1]) #check the end
                        path = extensions_folders[extension]
                    except Exception:
                        extension = "noname"
                    file_exists = os.path.isfile(extensions_folders[extension] + "/" + new_name)
                    while file_exists:
                        i +=1
                        new_name = os.path.splitext(folder_to_track + "/" + new_name)[0] + str(i) + os.path.splitext(folder_to_track + "/" + new_name)[1] # filename + str(i)
                        new_name = new_name.split("/")[4]
                        file_exists = os.path.isfile(extensions_folders[extension] + "/" + new_name)
                    src = folder_to_track + "/" + filename

                    year = datetime.datetime.year
                    month = datetime.datetime.month

                    folder_destination_path = extensions_folders[extension]

                    year_exists = False
                    month_exists = False
                    for folder_name in os.listdir(extensions_folders[extension]):
                        if folder_name == str(year):
                            folder_destination_path = extensions_folders[extension] + "/" +folder_name
                            year_exists = True
                            if str(month) == folder_month:
                                folder_destination_path = extensions_folders[extension] + "/" + str(year) + "/" + str(month)
                                month_exists = True
                    if not year_exists:
                        os.mkdir(extensions_folders[extension] + "/" + str(year))
                        folder_destination_path = extensions_folders[extension] + "/" + str(year)
                    if not month_exists:
                        os.mkdir(extensions_folders[extension] + "/" + str(year) + "/" + str(month))

                    new_name = extensions_folders[extension] + "/" + new_name
                    os.rename(src, new_name)
                except Exception:
                    print(filename)

extensions_folders = {
    # No name
    'noname':  '/Users/issacmiao/Desktop/issacmiao/other/uncategorized',
    # audio
    '.aif':    '/Users/issacmiao/Desktop/issacmiao/media/audio',
    '.cda':    '/Users/issacmiao/Desktop/issacmiao/media/audio',
    '.mid':    '/Users/issacmiao/Desktop/issacmiao/media/audio',
    '.midi':   '/Users/issacmiao/Desktop/issacmiao/media/audio',
    '.mp3':    '/Users/issacmiao/Desktop/issacmiao/media/audio',
    '.mpa':    '/Users/issacmiao/Desktop/issacmiao/media/audio',
    '.ogg':    '/Users/issacmiao/Desktop/issacmiao/media/audio',
    '.wav':    '/Users/issacmiao/Desktop/issacmiao/media/audio',
    '.wma':    '/Users/issacmiao/Desktop/issacmiao/media/audio',
    '.wpl':    '/Users/issacmiao/Desktop/issacmiao/media/audio',
    '.m3u':    '/Users/issacmiao/Desktop/issacmiao/media/audio',
    # text
    '.txt':    '/Users/issacmiao/Desktop/issacmiao/text/text_files',
    '.doc':    '/Users/issacmiao/Desktop/issacmiao/text/microsoft/word',
    '.docx':   '/Users/issacmiao/Desktop/issacmiao/text/microsoft/word',
    '.ppt':   '/Users/issacmiao/Desktop/issacmiao/text/microsoft/powerpoint',
    '.pptx':   '/Users/issacmiao/Desktop/issacmiao/text/microsoft/powerpoint',
    '.odt ':   '/Users/issacmiao/Desktop/issacmiao/text/text_files',
    '.pdf':    '/Users/issacmiao/Desktop/issacmiao/text/pdf',
    '.rtf':    '/Users/issacmiao/Desktop/issacmiao/text/text_files',
    '.tex':    '/Users/issacmiao/Desktop/issacmiao/text/text_files',
    '.wks ':   '/Users/issacmiao/Desktop/issacmiao/text/text_files',
    '.wps':    '/Users/issacmiao/Desktop/issacmiao/text/text_files',
    '.wpd':    '/Users/issacmiao/Desktop/issacmiao/text/text_files',
    # video
    '.3g2':    '/Users/issacmiao/Desktop/issacmiao/media/video',
    '.3gp':    '/Users/issacmiao/Desktop/issacmiao/media/video',
    '.avi':    '/Users/issacmiao/Desktop/issacmiao/media/video',
    '.flv':    '/Users/issacmiao/Desktop/issacmiao/media/video',
    '.h264':   '/Users/issacmiao/Desktop/issacmiao/media/video',
    '.m4v':    '/Users/issacmiao/Desktop/issacmiao/media/video',
    '.mkv':    '/Users/issacmiao/Desktop/issacmiao/media/video',
    '.mov':    '/Users/issacmiao/Desktop/issacmiao/media/video',
    '.mp4':    '/Users/issacmiao/Desktop/issacmiao/media/video',
    '.mpg':    '/Users/issacmiao/Desktop/issacmiao/media/video',
    '.mpeg':   '/Users/issacmiao/Desktop/issacmiao/media/video',
    '.rm':     '/Users/issacmiao/Desktop/issacmiao/media/video',
    '.swf':    '/Users/issacmiao/Desktop/issacmiao/media/video',
    '.vob':    '/Users/issacmiao/Desktop/issacmiao/media/video',
    '.wmv':    '/Users/issacmiao/Desktop/issacmiao/media/video',
    # images
    '.ai':     '/Users/issacmiao/Desktop/issacmiao/media/images',
    '.bmp':    '/Users/issacmiao/Desktop/issacmiao/media/images',
    '.gif':    '/Users/issacmiao/Desktop/issacmiao/media/images',
    '.jpg':    '/Users/issacmiao/Desktop/issacmiao/media/images',
    '.jpeg':   '/Users/issacmiao/Desktop/issacmiao/media/images',
    '.png':    '/Users/issacmiao/Desktop/issacmiao/media/images',
    '.ps':     '/Users/issacmiao/Desktop/issacmiao/media/images',
    '.psd':    '/Users/issacmiao/Desktop/issacmiao/media/images',
    '.svg':    '/Users/issacmiao/Desktop/issacmiao/media/images',
    '.tif':    '/Users/issacmiao/Desktop/issacmiao/media/images',
    '.tiff':   '/Users/issacmiao/Desktop/issacmiao/media/images',
    '.cr2':    '/Users/issacmiao/Desktop/issacmiao/media/images',
    # internet
    '.asp':    '/Users/issacmiao/Desktop/issacmiao/other/internet',
    '.aspx':   '/Users/issacmiao/Desktop/issacmiao/other/internet',
    '.cer':    '/Users/issacmiao/Desktop/issacmiao/other/internet',
    '.cfm':    '/Users/issacmiao/Desktop/issacmiao/other/internet',
    '.cgi':    '/Users/issacmiao/Desktop/issacmiao/other/internet',
    '.pl':     '/Users/issacmiao/Desktop/issacmiao/other/internet',
    '.css':    '/Users/issacmiao/Desktop/issacmiao/other/internet',
    '.htm':    '/Users/issacmiao/Desktop/issacmiao/other/internet',
    '.js':     '/Users/issacmiao/Desktop/issacmiao/other/internet',
    '.jsp':    '/Users/issacmiao/Desktop/issacmiao/other/internet',
    '.part':   '/Users/issacmiao/Desktop/issacmiao/other/internet',
    '.php':    '/Users/issacmiao/Desktop/issacmiao/other/internet',
    '.rss':    '/Users/issacmiao/Desktop/issacmiao/other/internet',
    '.xhtml':  '/Users/issacmiao/Desktop/issacmiao/other/internet',
    '.html':   '/Users/issacmiao/Desktop/issacmiao/other/internet',
    # compressed
    '.7z':     '/Users/issacmiao/Desktop/issacmiao/other/compressed',
    '.arj':    '/Users/issacmiao/Desktop/issacmiao/other/compressed',
    '.deb':    '/Users/issacmiao/Desktop/issacmiao/other/compressed',
    '.pkg':    '/Users/issacmiao/Desktop/issacmiao/other/compressed',
    '.rar':    '/Users/issacmiao/Desktop/issacmiao/other/compressed',
    '.rpm':    '/Users/issacmiao/Desktop/issacmiao/other/compressed',
    '.tar.gz': '/Users/issacmiao/Desktop/issacmiao/other/compressed',
    '.z':      '/Users/issacmiao/Desktop/issacmiao/other/compressed',
    '.zip':    '/Users/issacmiao/Desktop/issacmiao/other/compressed',
    # disc
    '.bin':    '/Users/issacmiao/Desktop/issacmiao/other/disc',
    '.dmg':    '/Users/issacmiao/Desktop/issacmiao/other/disc',
    '.iso':    '/Users/issacmiao/Desktop/issacmiao/other/disc',
    '.toast':  '/Users/issacmiao/Desktop/issacmiao/other/disc',
    '.vcd':    '/Users/issacmiao/Desktop/issacmiao/other/disc',
     # calendars
    ".ics":    "/Users/issacmiao/Desktop/issacmiao/calendars",   
    # data
    '.csv':    '/Users/issacmiao/Desktop/issacmiao/programming/database',
    '.dat':    '/Users/issacmiao/Desktop/issacmiao/programming/database',
    '.db':     '/Users/issacmiao/Desktop/issacmiao/programming/database',
    '.dbf':    '/Users/issacmiao/Desktop/issacmiao/programming/database',
    '.log':    '/Users/issacmiao/Desktop/issacmiao/programming/database',
    '.mdb':    '/Users/issacmiao/Desktop/issacmiao/programming/database',
    '.sav':    '/Users/issacmiao/Desktop/issacmiao/programming/database',
    '.sql':    '/Users/issacmiao/Desktop/issacmiao/programming/database',
    '.tar':    '/Users/issacmiao/Desktop/issacmiao/programming/database',
    '.xml':    '/Users/issacmiao/Desktop/issacmiao/programming/database',
    '.json':   '/Users/issacmiao/Desktop/issacmiao/programming/database',
    # executables
    '.apk':    '/Users/issacmiao/Desktop/issacmiao/other/executables',
    '.bat':    '/Users/issacmiao/Desktop/issacmiao/other/executables',
    '.com':    '/Users/issacmiao/Desktop/issacmiao/other/executables',
    '.exe':    '/Users/issacmiao/Desktop/issacmiao/other/executables',
    '.gadget': '/Users/issacmiao/Desktop/issacmiao/other/executables',
    '.jar':    '/Users/issacmiao/Desktop/issacmiao/other/executables',
    '.wsf':    '/Users/issacmiao/Desktop/issacmiao/other/executables',
    # fonts
    '.fnt':    '/Users/issacmiao/Desktop/issacmiao/other/fonts',
    '.fon':    '/Users/issacmiao/Desktop/issacmiao/other/fonts',
    '.otf':    '/Users/issacmiao/Desktop/issacmiao/other/fonts',
    '.ttf':    '/Users/issacmiao/Desktop/issacmiao/other/fonts',
    # calendars
    ".ics":    "/Users/issacmiao/Desktop/issacmiao/calendars",
    # presentations
    '.key':    '/Users/issacmiao/Desktop/issacmiao/text/presentations',
    '.odp':    '/Users/issacmiao/Desktop/issacmiao/text/presentations',
    '.pps':    '/Users/issacmiao/Desktop/issacmiao/text/presentations',
    # '.ppt':    '/Users/issacmiao/Desktop/issacmiao/text/presentations',
    # '.pptx':   '/Users/issacmiao/Desktop/issacmiao/text/presentations',
    # programming
    '.c':      '/Users/issacmiao/Desktop/issacmiao/programming/c&c++',
    '.class':  '/Users/issacmiao/Desktop/issacmiao/programming/java',
    '.java':   '/Users/issacmiao/Desktop/issacmiao/programming/java',
    '.py':     '/Users/issacmiao/Desktop/issacmiao/programming/python',
    '.sh':     '/Users/issacmiao/Desktop/issacmiao/programming/shell',
    '.h':      '/Users/issacmiao/Desktop/issacmiao/programming/c&c++',
    # spreadsheets
    '.ods':    '/Users/issacmiao/Desktop/issacmiao/text/microsoft/excel',
    '.xlr':    '/Users/issacmiao/Desktop/issacmiao/text/microsoft/excel',
    '.xls':    '/Users/issacmiao/Desktop/issacmiao/text/microsoft/excel',
    '.xlsx':   '/Users/issacmiao/Desktop/issacmiao/text/microsoft/excel',
    # system
    '.bak':    '/Users/issacmiao/Desktop/issacmiao/text/other/system',
    '.cab':    '/Users/issacmiao/Desktop/issacmiao/text/other/system',
    '.cfg':    '/Users/issacmiao/Desktop/issacmiao/text/other/system',
    '.cpl':    '/Users/issacmiao/Desktop/issacmiao/text/other/system',
    '.cur':    '/Users/issacmiao/Desktop/issacmiao/text/other/system',
    '.dll':    '/Users/issacmiao/Desktop/issacmiao/text/other/system',
    '.dmp':    '/Users/issacmiao/Desktop/issacmiao/text/other/system',
    '.drv':    '/Users/issacmiao/Desktop/issacmiao/text/other/system',
    '.icns':   '/Users/issacmiao/Desktop/issacmiao/text/other/system',
    '.ico':    '/Users/issacmiao/Desktop/issacmiao/text/other/system',
    '.ini':    '/Users/issacmiao/Desktop/issacmiao/text/other/system',
    '.lnk':    '/Users/issacmiao/Desktop/issacmiao/text/other/system',
    '.msi':    '/Users/issacmiao/Desktop/issacmiao/text/other/system',
    '.sys':    '/Users/issacmiao/Desktop/issacmiao/text/other/system',
    '.tmp':    '/Users/issacmiao/Desktop/issacmiao/text/other/system'
        }

folder_to_track = "/Users/issacmiao/Desktop"
folder_destination="/Users/issacmiao/Desktop/issacmiao"
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










