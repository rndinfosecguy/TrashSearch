# TrashSearch
Searching the TrashPanda OSINT bot API to check if your email address was leaked or not

## Hint
This tool just tells you if your email address was identified by the TrashPanda OSINT bot or not. It will not tell you the identified password corresponding to the submitted email address.

## Parameters
- -v: email address to check for leaks
- -s: data sources to search [g = ghostbin.co, p = pastebin.com, z = 0paste.com]

## Example Usage
```console
python3 TrashSearch.py -v info@example.com -s gz
```
