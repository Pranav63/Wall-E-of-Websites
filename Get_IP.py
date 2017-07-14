# METHOD 1 - Using the host 'url' terminal command , getting the output google.com has address 123.23.34.45 
#            keeping the marker after has address | and printing everything after address.


import os 

def ip_address(url):
	command = "host "+url
	process = os.popen(command)
	result = str(process.read())
	marker = result.find('has address')+12
	return result[marker:].splitlines()[0]

'''
# METHOD 2 - Using socket module's gethostbyname function
from socket import gethostbyname

def get_ip(url):
	ip=gethostbyname(url)
	return ip 
	print("There goes the IP")
'''
ip_address("https://www.raghavdua.com")
