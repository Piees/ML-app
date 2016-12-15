import requests
import sys
import config

if config.url == "url":
    sys.exit("Set your url in config.py")

url = config.url


def sendpic(picpath):
    files = {'files': open(picpath, 'rb')}
    r = requests.post(url, files=files)
    return r.text.split('I tensorflow/examples/label_image/main.cc:206] ')[1].split(' (')[0] + \
        " " + \
        r.text.split('I tensorflow/examples/label_image/main.cc:206] ')[1].split('0.')[-1][:2] + \
        "%"
