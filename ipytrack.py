import requests
import time
print("")
print("")
print("====================================================")
print("█ █▀█ █▄█ ▀█▀ █▀█ ▄▀█ █▀▀ █▄▀")
print("█ █▀▀ ░█░ ░█░ █▀▄ █▀█ █▄▄ █░█")
print ("===================================================")
print("")
print("")
print("options:")

print("------------------------")
print("[1] Track Me")
print("[2] Track IP")
print("------------------------")
print("")
ch = input("choose ->  ")
if  ch == "1":
	url1 = "https://ipinfo.io/"
	res1 = requests.get(url1)
	data1 = res1.json()
	
	ip = data1['ip']
	con = data1['country']
	reg = data1['region']
	cit = data1['city']
	loc = data1['loc']
	tz = data1['timezone']
	map = f"https://google.com/maps?q={loc}"
	print("")
	print(".......[ Your Public IP Information .....................")
	print("")
	print(f"[+] IP  :  {ip}")
	print(f"[+] country  :  {con}")
	print(f"[+] region  :  {reg}")
	print(f"[+] city  :  {cit}")
	print(f"[+] location  :  {loc}")
	print(f"[+] time zone   :  {tz}")
	print(f"[=] Google maps URL  :  {map}")
	print("..........................................................")
    
elif ch == "2":
	ip2 = input("Enter Public IP: ")
	url2 = f"https://ipinfo.io/{ip2}"
	res2 = requests.get(url2)
	data2 = res2.json()
	ipq = data2['ip']
	con2 = data2['country']
	reg2 = data2['region']
	cit2 = data2['city']
	loc2 = data2['loc']
	tz2 = data2['timezone']
	map2 = f"https://google.com/maps?q={loc2}"
	print("")
	print("........[ This IP Information ] ..........................")
	print("")
	print(f"[+] IP  :  {ipq}")
	print(f"[+] country  :  {con2}")
	print(f"[+] region  :  {reg2}")
	print(f"[+] city  :  {cit2}")
	print(f"[+] location  :  {loc2}")
	print(f"[+] time zone   :  {tz2}")
	print(f"[=] Google maps URL  :  {map2}")
	print("..........................................................")
else:
    print("")
    print("[!] Invalid Choice!")