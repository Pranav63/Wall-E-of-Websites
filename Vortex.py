from general import * 
from Top_level_domain import * 
from Get_IP import * 
from Port_Scan import * 
from robotsTXT import * 
from Whois_Command import * 

Center_Direc="Websites"
directory_create(Center_Direc)

def info(name , url):
	domain = get_topLevelDomain(url)
	ip = get_ip(url)
	port = nmap_scan(ip) # The ip is segregated in the previous step . Pretty sweet 
	robot = robot_file(url)
	whoo = whois(domain) # It takes the imput only the TLD of the website name
	report(name , url, domain , ip , port , robot , whoo)


def report(name , url, domain , ip , port , robot , whoo):
	projects_directory = Center_Direc + "/" + name
	directory_create(projects_directory)       # IT symbolises a direc within a direc like home/pranav
  	write(projects_directory + "/url.txt" + url)
  	write(projects_directory + "/Domain_name.txt" + domain)
  	write(projects_directory + "/Ip_Address.txt" + ip)
  	write(projects_directory + "/Ports_Active.txt" + port)
  	write(projects_directory + "/Robots.txt" + robot)
  	write(projects_directory + "/Whois.txt" + whoo)

info('RDua','https://www.raghavdua.com')
