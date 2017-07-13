
# Robots.txt determines that which pages of a website can a crawler crawl or not . 
# It sees for the url if it ends with "/" .If it does not , it adds "/" and then opens the robots.txt file
# makes the encoding to Unicode Transformation format & reads data

import urllib.requests 
import io 

def robot_file(url):
	if url.endswith("/"):
		path = url
	else:
		path = url + "/"

	req = urllib.request.urlopen(path + "robots.txt",data=NONE)
	output = io.TextIOWrapper(req , encoding="UTF-8")
	return output.read()
	print("Robots.txt is ready .")

