import requests
import sys
import config
'''
To test:
run with file that you want classified as argument
ex. python send.py pic.jpg
'''

if config.url == "url":
    sys.exit("Set your url in config.py")

url = config.url
files = {'files': open(sys.argv[1], 'rb')}
r = requests.post(url, files=files)

for x in r.text.split('I tensorflow/examples/label_image/main.cc:206] ')[1:]:
    print x
