# TrashSearch
Searching the TrashPanda OSINT bot API to check if your email/domain or password was leaked.

[![Anurag's GitHub stats](https://github-readme-stats.vercel.app/api?username=rndinfosecguy)](https://github.com/anuraghazra/github-readme-stats)

```console
$ python3 TrashSearch.py -h

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

usage: TrashSearch.py [-h] [-m MODE] -v VALUE [-s SOURCES]

Searching the TrashPanda OSINT bot API to check if your email/domain or
password was leaked. To avoid abuse the email/domain search does not
disclose passwords and the password search does not disclose the corresponding
email/domain.

optional arguments:
  -h, --help            show this help message and exit
  -m MODE, --mode MODE  Select mode [0 = email/domain search, 1 = password
                        search] default = 0
  -v VALUE, --value VALUE
                        email/domain or password to check for leaks
  -s SOURCES, --sources SOURCES
                        data sources to search [g = ghostbin.co, p =
                        pastebin.com, z = 0paste.com]. You can combine
                        sources. example: '-s gz'. default = gpz

example usage: python3 TrashSearch.py -v info@example.com -s gz
```

## Intro and Configuration
This tool tells you if your email/domain or password was identified by the TrashPanda OSINT bot.

The tool works out of the box with anonymous credentials provided inside the auth.conf file. To avoid abuse the anonymous email/domain search does not disclose passwords and the password search does not disclose the corresponding email/domain.

auth.conf:
```
username=anonymous
password=Uh324)nwh64AL
```

If you are a whitehat researcher and I granted you access to the TrashPanda API, you can subsitute the anonymous credentials inside auth.conf with your login information to get raw leak data when using this tool.

You are a whitehat researcher but I did not grant you access to the TrashPanda API so far? Visit https://got-hacked.wtf/ for more information

## Parameters
- m: mode to use [0 = email/domain search, 1 = password search]
- v: depends on the mode what kind of value is expected here. Mode 0 expects an email/domain and mode 1 expects a password.
- s: data sources to search [g = ghostbin.co, p = pastebin.com, z = 0paste.com]. You can combine data sources.

## Example Usage
```console
python3 TrashSearch.py -v info@example.com -s gz
python3 TrashSearch.py -m 1 -v 123456
```
