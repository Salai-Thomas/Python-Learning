import re,urllib
import urllib.request

web_url = "https://www.google.com"
u = urllib.request.urlopen(web_url)
text = str(u.read())
# print(text) #download google home page
title = re.findall("<title>.*</title>",text)
print(title)