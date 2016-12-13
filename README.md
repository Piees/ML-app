# ML-app

## Docker-API

### How to build:
requirements:
* Docker
* Python, with requests and flask

`this means code in terminal`
1. `docker run -it piees/mldock:v1`
2. `exit`
3. `docker ps -a` Note the container name
4. `docker start <container name>`
Your docker container is now running with the classifier inside
5. change dockercontainer variable in docker/config.py to container name
6. `python docker/main.py`


## App

### How to build to android:
requirements:
* Buildozer
* Python, with plyer, kivy and requests

`this means code in terminal`
1. `buildozer init`
2. in buildozer.spec change change requirements to: requirements = kivy,plyer,requests
3. `buildozer android debug deploy run`
You can now find the .apk in the bin folder
