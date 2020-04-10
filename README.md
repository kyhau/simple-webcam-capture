# simple-cameraman

Simple python script for capturing an image from a webcam using [OpenCV 2](http://opencv.org/). 

## Build and run

`Python 3.8`: [![Build Status](https://travis-ci.org/kyhau/simple-cameraman.svg?branch=master)](https://travis-ci.org/kyhau/simple-cameraman)

Linux

```bash
sudo apt-get update && sudo apt-get install -y libsm6 libxext6 libxrender1

virtualenv env
. env/bin/activate
python -m pip install -e .
cameraman
```

Windows

```cmd
virtualenv env
env\Scripts\activate
python -m pip install -e .
cameraman
```
