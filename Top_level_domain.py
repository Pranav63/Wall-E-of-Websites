from tld import get_tld 

def get_topLevelDomain(url):
	domain_name=get_tld(url)
	return domain_name
	print("Fetched the Domain name")
