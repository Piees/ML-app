import requests
import sys

url = "http://127.0.0.1:5000/"
files = {'files': open(sys.argv[1], 'rb')}
r = requests.post(url, files=files)
print r.text

