import os 

# make separte directory for each website you scan
def directory_create(directory):
	if not os.path.exists(directory):
		os.makedirs(directory)

# write the data onto the file eg. IP address , ports , services , robots.txt data etc.
def file_write(path,data):
	files = open(path,'w')
	files.write(data)
	files.close()
