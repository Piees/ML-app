import requests
import sys

#url = "http://127.0.0.1:5000/"
url = "http://46.101.200.118:5000/"


def sendpic(picpath):
    files = {'files': open(picpath, 'rb')}
    r = requests.post(url, files=files)
    return r.text.split('I tensorflow/examples/label_image/main.cc:206] ')[1].split(' (')[0] + \
        " " + \
        r.text.split('I tensorflow/examples/label_image/main.cc:206] ')[1].split('0.')[-1][:2] + \
        "%"
