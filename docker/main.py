from flask import Flask
app = Flask(__name__)
import subprocess
from flask import request


@app.route('/', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        f = request.files['files']
        f.save('tempphoto.jpg')
        #        subprocess.Popen("echo 'sup'", stdout=subprocess.PIPE, shell=True)
        subprocess.Popen(
            "docker cp tempphoto.jpg goofy_austin:/tf_files/temp/tempphoto.jpg",
            stdout=subprocess.PIPE,
            shell=True)
        #		return subprocess.Popen("docker exec zen_murdock python /mlapp/label_image.py /mlapp/tempphoto.jpg", stdout=subprocess.PIPE, shell=True).communicate()[0]
        proc = subprocess.Popen(
            "docker exec goofy_austin \
            /tensorflow/bazel-bin/tensorflow/examples/label_image/label_image \
            --graph=/tf_files/retrained_graph.pb \
            --labels=/tf_files/retrained_labels.txt --output_layer=final_result \
            --image=/tf_files/temp/tempphoto.jpg > process.txt",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True).communicate()[1]
        return proc
    else:
        return 'Post failed'


'''
result = subprocess.Popen(
    "docker exec goofy_austin \
    /tensorflow/bazel-bin/tensorflow/examples/label_image/label_image \
    --graph=/tf_files/retrained_graph.pb \
    --labels=/tf_files/retrained_labels.txt --output_layer=final_result \
    --image=/tf_files/temp/tempphoto.jpg",
    stdout=subprocess.PIPE,
    shell=True).communicate()[0]
print result
'''

if __name__ == '__main__':
    #    app.run(debug=True,host='0.0.0.0')
    app.run(host='0.0.0.0')
