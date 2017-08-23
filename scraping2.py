import webbrowser, sys

'''
Second task: open multiple tabs using webbrowser library
Example usage: 
python scraping.py http://www.quora.com http://www.twitter.com http://www.facebook.com
'''
if len(sys.argv) > 1:
 for a in sys.argv[1:]:
 	webbrowser.open(a)
