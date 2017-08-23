import webbrowser, sys, pyperclip

'''
First task: open a web link using webbrowser library
Example usage: 
python scraping.py The Marylander Apartment Homes, Baltimore Maryland, Saint Paul Street, Baltimore, MD
'''

if len(sys.argv) > 1:
	#Use join to make multiple strings into 1 string
	address = ' '.join(sys.argv[1:])
else:
	#Use pyperclip to get address from clipboard
	address = pyperclip.paste()
webbrowser.open('https://www.google.com/maps/place/' + address)