import os 

def whois(url):
	command = "whois"+ url 
	process = os.popen(command)
	output  = str(process.read())
	return output 
	print("Whois is figured ! Get it ?")