<p align="center">
<br>
<img src="https://raw.githubusercontent.com/coci/duckiter/main/assets/logo.png">
</p>   

# Duckiter
Duckiter will Automatically dockerize your Django projects.

### Requirements :

    - python version : python version 3.6 or upper version
    - OS : 
        - linux
        - MacOS
        - windows ( drop support )
    - docker engine installed in your machine and already run through the usage of package


### Installation :
clone project:
```
pip install duckiter
```


### Usage :
Duckiter has two individual steps:
    1- initialize Dockerfile
    2- build image from created Dockerfile

#### To initialize Dockerfile (step 1) :
in terminal hit to your project directory ( where manage.py is in root ):
```
duckiter --init
```
This will create Dockerfile and config.cfg in the root of the project, and you can manipulate those files before Duckiter creates an image.
If you are ok with our configurations, you can just pass '-build' to immediately build the image right after creating the Dockerfile.
```
duckiter --init -build
```
#### To build image (step 2) :
To build an image from the Dockerfile that has been created in the last step, you need enter:
```
duckiter main.py -build
```
this will look for config.cfg in project directory and then build the image.

## Troubleshooting :

- if you get blow error while your docker engine is already run :

```
[ WARNNING !!!! ] It seems your docker engine doesn't run, please run the Docker engine.
```

​		you can fix this issue , just enter these commands :

```
$ sudo groupadd docker
$ sudo usermod -aG docker $USER
$ newgrp docker
```

now problem fixed and you can run command again.



- if you got error like :

  ```
  duckiter : command not found
  ```

  you can fix this issue by adding your python package directory into you PATH.

  

### Contribution :

feel free to contribute to this project, but first contact me about the idea :)