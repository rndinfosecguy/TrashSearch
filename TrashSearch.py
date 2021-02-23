import requests
import sys
import argparse

descr = """

,--------.                      ,--.      ,---.                              ,--.
'--.  .--',--.--. ,--,--. ,---. |  ,---. '   .-'  ,---.  ,--,--.,--.--. ,---.|  ,---.
   |  |   |  .--'' ,-.  |(  .-' |  .-.  |`.  `-. | .-. :' ,-.  ||  .--'| .--'|  .-.  |
   |  |   |  |   \ '-'  |.-'  `)|  | |  |.-'    |\   --.\ '-'  ||  |   \ `--.|  | |  |
   `--'   `--'    `--`--'`----' `--' `--'`-----'  `----' `--`--'`--'    `---'`--' `--'

"""

print(descr)
parser = argparse.ArgumentParser(description="Searching the TrashPanda OSINT bot API to check if your email address was leaked or not", epilog="example usage: python3 " + sys.argv[0] + " -v info@example.com -s gz")
parser.add_argument("-v", "--value", help="email address to check for leaks", required=True)
parser.add_argument("-s", "--sources", help="data sources to search [g = ghostbin.co, p = pastebin.com, z = 0paste.com]. You can combine sources. example: '-s gz'. default = gpz", required=True, default="gpz")
args = parser.parse_args()

try:
	print("[*] Searching for leaks in TrashPanda OSINT bot API...")
	r =requests.get("http://api.got-hacked.wtf:7230/pwned?v=" + requests.utils.quote(args.value) + "&s=" + requests.utils.quote(args.sources) + "&l=1")
	if r.text == "True":
		print("[+] Oh no! The email address was pwned =X_X=")
	else:
		print("[+] Good news! Could not find the email address =^_^=")
except:
	print("[-] Unable to reach API")
