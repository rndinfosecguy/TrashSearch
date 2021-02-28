# TrashSearch
Searching the TrashPanda OSINT bot API to check if your email address was leaked or not

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

usage: TrashSearch.py [-h] -v VALUE [-s SOURCES]

Searching the TrashPanda OSINT bot API to check if your email/domain was
leaked

optional arguments:
  -h, --help            show this help message and exit
  -v VALUE, --value VALUE
                        email address or domain to check for leaks
  -s SOURCES, --sources SOURCES
                        data sources to search [g = ghostbin.co, p =
                        pastebin.com, z = 0paste.com]. You can combine
                        sources. example: '-s gz'. default = gpz

example usage: python3 TrashSearch.py -v info@example.com -s gz
```

## Hint
This tool just tells you if your email address was identified by the TrashPanda OSINT bot or not. It will not tell you the identified password corresponding to the submitted email address.

## Parameters
- -v: email address to check for leaks
- -s: data sources to search [g = ghostbin.co, p = pastebin.com, z = 0paste.com]

## Example Usage
```console
python3 TrashSearch.py -v info@example.com -s gz
```
