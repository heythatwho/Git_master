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
					new_name=filename
					# split_name = filename.split(".")
					file_exists = os.path.isfile(folder_destination + "/" + new_name)
					while file_exists:
						i +=1
						new_name = os.path.splitext(folder_to_track + "/" + new_name)[0] + str(i) + os.path.splitext(folder_to_track + "/" + new_name)[1] # filename + str(i)
						new_name = new_name.split("/")[4]
						file_exists = os.path.isfile(folder_destination + "/" + new_name)


					src = folder_to_track + "/" + filename
					new_name = folder_destination + "/" + new_name
					os.rename(src, new_name)
				except Exception:
					print(filename)


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









