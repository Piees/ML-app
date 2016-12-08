import requests
import sys

#url = "http://127.0.0.1:5000/"
url = "http://10.0.0.124:5000/"
files = {'files': open(sys.argv[1], 'rb')}
r = requests.post(url, files=files)
#print r.text

for x in r.text.split('I tensorflow/examples/label_image/main.cc:206] ')[1:]:
    print x
