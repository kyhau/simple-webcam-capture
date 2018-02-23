# simple-cameraman

Simple python script for capturing an image from a webcam using [OpenCV 2](http://opencv.org/). 

## Build and run

`Python 2.7, Python 3.6`: [![Build Status](https://travis-ci.org/kyhau/simple-cameraman.svg?branch=master)](https://travis-ci.org/kyhau/simple-cameraman)

Linux

```bash
apt-get update && apt-get install -y libsm6 libxext6

virtualenv env
. env/bin/activate
python -m pip install -r requirements.txt
cameraman
```

Windows

```cmd
virtualenv env
env\Scripts\activate
python -m pip install -e .
cameraman
```
