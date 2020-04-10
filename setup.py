from setuptools import setup, find_packages
import os

# Makes setup work inside of a virtualenv
use_system_lib = True
if os.environ.get("BUILD_LIB") == "1":
    use_system_lib = False

base_dir = os.path.dirname(__file__)

__author__ = "Kay Hau"
__email__ = "virtualda@gmail.com"

__title__ = "simplecameraman"
__version__ = "0.1.0.dev0"
__summary__ = "Simple python script for capturing an image from a webcam."
__uri__ = "https://github.com/kyhau/simple-cameraman"

__requirements__ = [
    "opencv-python>=3.4.0.12",
    "numpy>=1.11.3+mkl"
]

with open(os.path.join(base_dir, "README.md")) as f:
    long_description = f.read()

setup(
    name=__title__,
    version=__version__,
    description=__summary__,
    long_description=long_description,
    packages=find_packages(exclude=["tests"]),
    author=__author__,
    author_email=__email__,
    url=__uri__,
    zip_safe=False,
    install_requires=__requirements__,
    data_files=[
        ("", ["ReleaseNotes.md"]),
    ],
    entry_points={
        "console_scripts": [
            "cameraman = simplecameraman.cameraman:main"
        ]
    },
)
