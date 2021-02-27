import time
from threading import Thread
import colorama
from colorama import Fore, Style
import requests
import sys
import argparse

loadingdone = 0
loadingsymbol = " (╯°□°)╯"

def loadingprogress():
	global loadingsymbol
	while loadingdone == 0:
		print("[*] Checking: " + loadingsymbol, end="\r")
		if loadingsymbol == " (╯°□°)╯":
			loadingsymbol = "╰(°□°╰) "
		elif loadingsymbol == "╰(°□°╰) ":
			loadingsymbol = " (╯°□°)╯"
		time.sleep(1)

def checking():
	r =requests.get("http://api.got-hacked.wtf:7230/pwned?v=" + requests.utils.quote(args.value) + "&s=" + requests.utils.quote(args.sources) + "&l=1")
	if r.text == "True":
		print(Fore.RED + "[+] Oh no! The email address was pwned =X_X=")
	else:
		print(Fore.GREEN + "[+] Good news! Could not find the email address =^_^=")
	print(Style.RESET_ALL)
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
parser = argparse.ArgumentParser(description="Searching the TrashPanda OSINT bot API to check if your email address was leaked or not", epilog="example usage: python3 " + sys.argv[0] + " -v info@example.com -s gz")
parser.add_argument("-v", "--value", help="email address to check for leaks", required=True)
parser.add_argument("-s", "--sources", help="data sources to search [g = ghostbin.co, p = pastebin.com, z = 0paste.com]. You can combine sources. example: '-s gz'. default = gpz", required=True, default="gpz")
args = parser.parse_args()

try:
	print("[*] Searching for leaks in TrashPanda OSINT bot API...")
	t = Thread(target=loadingprogress)
	t.start()
	t2 = Thread(target=checking)
	t2.start()
except:
	print("[-] Unable to reach API")

