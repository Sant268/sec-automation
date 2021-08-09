import requests
import sys
sub_list = open("./wordlist.txt").read()
subdomains = sub_list.splitlines()	
for s in subdomains:
	sdm = f"http://{s}.{sys.argv[1]}"	
	try:
		requests.get(sdm)	
	except requests.ConnectionError:
		pass
	else
		print("Valid Domain: ",sdm)
