#! Python3
# mapit.py launches a map in the browser using the command line and clipboard

import webbrowser, sys
import pyperclip

# 1) Get address from command line
# 2) Store address in the clipboard
# 3) Launch Google maps with address from clipboard


# 1) Get address from command line
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
