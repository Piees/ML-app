from flask import Flask
app = Flask(__name__)
import subprocess
from flask import request

@app.route('/', methods= ['GET', 'POST'])
def test():
	if request.method == 'POST':
		f = request.files['files']
		f.save('tempphoto.jpg')
		subprocess.Popen("echo 'sup'", stdout=subprocess.PIPE, shell=True)
		subprocess.Popen("docker cp testphoto.jpg zen_murdock:/mlapp/tempphoto.jpg", stdout=subprocess.PIPE, shell=True)
		return subprocess.Popen("docker exec zen_murdock python /mlapp/label_image.py /mlapp/tempphoto.jpg", stdout=subprocess.PIPE, shell=True).communicate()[0]
	else:
		return 'Post failed'


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
