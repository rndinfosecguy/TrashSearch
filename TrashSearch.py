import time
from threading import Thread
import colorama
from colorama import Fore, Style
import requests
import sys
import argparse
from base64 import b64encode

loadingdone = 0
loadingsymbol = " (╯°□°)╯"
circlesymbol = "|"

username = ""
password = ""
with open("auth.conf", "r") as f:
	tmpContent = f.readlines()
for line in tmpContent:
	line = line.strip()
	if "username" in line:
		username = line.split("username=")[1]
	if "password" in line:
		password = line.split("password=")[1]
userAndPass = username + ":" + password
userAndPass = b64encode(userAndPass.encode()).decode("ascii")

def loadingprogress():
	global circlesymbol
	global loadingsymbol
	while loadingdone == 0:
		print("[" + circlesymbol + "] Checking: " + loadingsymbol, end="\r")
		if loadingsymbol == " (╯°□°)╯":
			loadingsymbol = "╰(°□°╰) "
		elif loadingsymbol == "╰(°□°╰) ":
			loadingsymbol = " (╯°□°)╯"
		if circlesymbol == "|":
			circlesymbol = "/"
		elif circlesymbol == "/":
			circlesymbol = "-"
		elif circlesymbol == "-":
			circlesymbol = "\\"
		elif circlesymbol == "\\":
			circlesymbol = "|"
		time.sleep(1)

def checking():
	limit = ""
	if username == "anonymous":
		limit += "&l=1"
	if args.wildcard:
		if "@" in args.value:
			print(Fore.YELLOW + "[#] Wildcard mode is only available when performing a domain search. Ignoring -w/--wildcard switch." + Style.RESET_ALL)
		else:
			print(Fore.GREEN + "[+] Wildcard mode enabled." + Style.RESET_ALL)
			limit += "&w"
	r =requests.get("http://api.got-hacked.wtf:7230/pwned?v=" + requests.utils.quote(args.value) + "&s=" + requests.utils.quote(args.sources) + limit, headers={"Authorization":"Basic " + userAndPass})
	if r.status_code != 401:
		if username == "anonymous":
			if r.text == "True":
				print(Fore.RED + "[+] Oh no! The email/domain you submitted was pwned =X_X=" + Style.RESET_ALL)
			else:
				print(Fore.GREEN + "[+] Good news! Could not find the email/domain you submitted =^_^=" + Style.RESET_ALL)
		else:
			if r.text == "False":
				print(Fore.GREEN + "[+] Good news! Could not find the email/domain you submitted =^_^=" + Style.RESET_ALL)
			else:
				print("                                      ")
				responseContent = r.text.strip()
				responseContent = responseContent.split(")(")
				for item in responseContent:
					item = item.split(",")
					uitem = item[0].split("'")[1]
					ditem = item[1].split("'")[1]
					pitem = item[2].split("'")[1]
					print(Fore.YELLOW + "\t" + uitem + "@" + ditem + ":" + pitem + Style.RESET_ALL)
	else:
		print(Fore.RED + "[-] UNAUTHORIZED! Does your auth.conf file contain valid credentials? (default=anonymous:Uh324)nwh64AL)" + Style.RESET_ALL)

	print()
	print("[*] Wanna see some stats? http://stats.got-hacked.wtf:6780/")
	print("[*] You are a security researcher and need more information? https://got-hacked.wtf/")
	global loadingdone
	loadingdone = 1

def checkingpassword():
	if args.wildcard:
		print(Fore.YELLOW + "[#] Wildcard mode is only available when performing a domain search. Ignoring -w/--wildcard switch." + Style.RESET_ALL)

	authenticated = 1
	if "z" in args.sources:
		r =requests.get("http://api.got-hacked.wtf:7230/pwd?v=" + requests.utils.quote(args.value) + "&s=z", headers={"Authorization":"Basic " + userAndPass})
		if r.status_code != 401:
			if r.text == "0":
				print(Fore.GREEN + "[+] Good news! Could not find the password you submitted on 0paste.com =^_^=" + Style.RESET_ALL)
			else:
				print(Fore.RED + "[+] Oh no! The password you submitted was pwned and published on 0paste.com " + r.text.strip()  + " times =X_X=" + Style.RESET_ALL)
		else:
			authenticated = 0
	if "g" in args.sources:
		r =requests.get("http://api.got-hacked.wtf:7230/pwd?v=" + requests.utils.quote(args.value) + "&s=g", headers={"Authorization":"Basic " + userAndPass})
		if r.status_code != 401:
			if r.text == "0":
				print(Fore.GREEN + "[+] Good news! Could not find the password you submitted on ghostbin.co =^_^=" + Style.RESET_ALL)
			else:
				print(Fore.RED + "[+] Oh no! The password you submitted was pwned and published on ghostbin.co " + r.text.strip()  + " times =X_X=" + Style.RESET_ALL)
		else:
			authenticated = 0
	if "p" in args.sources:
		r =requests.get("http://api.got-hacked.wtf:7230/pwd?v=" + requests.utils.quote(args.value) + "&s=p", headers={"Authorization":"Basic " + userAndPass})
		if r.status_code != 401:
			if r.text == "0":
				print(Fore.GREEN + "[+] Good news! Could not find the password you submitted on pastebin.com =^_^=" + Style.RESET_ALL)
			else:
				print(Fore.RED + "[+] Oh no! The password you submitted was pwned and published on pastebin.com " + r.text.strip()  + " times =X_X=" + Style.RESET_ALL)
		else:
			authenticated = 0
	if authenticated == 0:
		print(Fore.RED + "[-] UNAUTHORIZED! Does your auth.conf file contain valid credentials? (default=anonymous:Uh324)nwh64AL)" + Style.RESET_ALL)
	print()
	print("[*] Wanna see some stats? http://stats.got-hacked.wtf:6780/")
	print("[*] You are a security researcher and need more information? https://got-hacked.wtf/")
	global loadingdone
	loadingdone = 1

descr = """
MMMMMMMMMMMMMMMMMMMMMMMMNKXNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNXKNMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMNo..';cxXMMMMMMMMMMMMMMMMMMMMMMMMMMMWKdc;'..lNMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMK,      ;0XXWMMMWNXK0XNWX0KXNWMMMMNNk'      '0MMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMO.      .xo,dkoc;'dkocccdkoc',:okxcko       .kMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMM0'      .ox'                     .:k:       .OMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMX:                                          ;KMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMk.                                        .xWMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMWx.                                      .dWMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMM0'                  ..                  .OMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMx.      ...                    ...       dWMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMNl .':oxO0K0Oko,            'lxO0K0Okoc,. cNMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMNkd0NMMMMMWXNWMNo.        .lXMWNXWMMMMMN0dxNMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXo';xNMK,        '0MWk;'lXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXo;xXWWx.        .dWWXx;lXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNWMWO,  .:llc.  .kWMWNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNd.   :KWWXc   .dXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN0o,  ....cxxl....  'oONWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMXkxxdl:'.     ..........     .':lodxkXMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMXd'                                'oXMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXkc'                          .:xXWMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMWWWWWWWWWNKkoc,..              ..,:okKNWWWWWWWWWMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMWWNXK00OOkkxxddooollllccc:;,,,,,,,,,,,,,,,,;:ccclllloooddxxkkOO0KKXNWMMMMMMMMMMMM
MMMMMMMMMMMMMMMWWWWWWNNNNNNXXXXXXXXKKKKKKKKKKKKKKKKKKKKKKKXXXXXXXXXNNNNNNWWWWWWMMMMMMMMMMMMMM
"""

print(descr)
parser = argparse.ArgumentParser(description="Searching the TrashPanda OSINT bot API to check if your email/domain or password was leaked." + Fore.YELLOW + " To avoid abuse (when running as anonymous user) the email/domain search does not disclose passwords and the password search does not disclose the corresponding email/domain." + Style.RESET_ALL, epilog="example usage: python3 " + sys.argv[0] + " -v info@example.com -s gz")
parser.add_argument("-m", "--mode", help="Select mode [0 = email/domain search, 1 = password search] default = 0", default="0")
parser.add_argument("-v", "--value", help="email/domain or password to check for leaks", required=True)
parser.add_argument("-w", "--wildcard", help="Enables wildcard mode when searching a domain. Adds a wildcard in front of the target domain (e.g.: *example.com) to also check for subdomains.", action="store_true")
parser.add_argument("-s", "--sources", help="Data sources to search [g = ghostbin.co, p = pastebin.com, z = 0paste.com]. You can combine sources. example: '-s gz'. default = gpz", default="gpz")
args = parser.parse_args()

try:
	print()
	print("[+] Loaded API authentication details for " + Fore.BLUE + username + Style.RESET_ALL)
	datasources = ""
	if "g" in args.sources:
		datasources += "[ghostbin.co] "
	if "z" in args.sources:
		datasources += "[0paste.com] "
	if "p" in args.sources:
		datasources += "[pastebin.com]"
	print("[+] Selected data sources: " + datasources)
	print("[*] Searching for leaks in TrashPanda OSINT bot API...")
	t = Thread(target=loadingprogress)
	t.start()
	if args.mode == "0":
		t2 = Thread(target=checking)
		t2.start()
	elif args.mode == "1":
		if ("p" in args.sources or "z" in args.sources or "g" in args.sources) and args.mode == "1":
			t2 = Thread(target=checkingpassword)
			t2.start()
		else:
			loadingdone = 1
			print(Fore.RED + "[-] No valid source selected [valid: g = ghostbin.co, p = pastebin.com, z = 0paste.com]")
	else:
		loadingdone = 1
		print(Fore.RED + "[-] No valid mode selected!")
except:
	print("[-] Unable to reach API")

