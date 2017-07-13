import os 

def nmap_scan(options,ip):
	command = "nmap" + options + " " + ip
	process = os.popen(command)
	output  = str(process.read())
	return output
	print("Through with an nmap scan") 
