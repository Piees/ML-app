from flask import Flask
app = Flask(__name__)
import subprocess
from flask import request
import config
import sys

if config.dockercontainer == "dockercontainer":
    sys.exit("Set your docker container in config.py")


@app.route('/', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':

        # saves the file sent
        f = request.files['files']
        f.save('tempphoto.jpg')

        # moves the saved file into the docker container
        subprocess.Popen(
            "docker cp tempphoto.jpg {}:/tf_files/temp/tempphoto.jpg".format(
                config.dockercontainer),
            stdout=subprocess.PIPE,
            shell=True)

        # runs the classifier on the file
        proc = subprocess.Popen(
            "docker exec {} \
            /tensorflow/bazel-bin/tensorflow/examples/label_image/label_image \
            --graph=/tf_files/retrained_graph.pb \
            --labels=/tf_files/retrained_labels.txt --output_layer=final_result \
            --image=/tf_files/temp/tempphoto.jpg"
            .format(config.dockercontainer),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True).communicate()[1]

        return proc
    else:
        return 'Post failed'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
