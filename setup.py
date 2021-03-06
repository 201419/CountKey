"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['main.py']
VERSION = '1.0.0'
DATA_FILES = []
OPTIONS = {
    'iconfile': 'icon.png',
    'packages': ['rumps', 'pynput'],
}

setup(
    app=APP,
    name='CountKey',
    author="YangShu",
    author_email="yangshu1109@gmail.com",
    version=VERSION,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
    install_requires=['rumps', 'pynput']
)
