import os

os.system('wget -q -O - archive.kali.org/archive-key.asc | apt-key add')
os.system('apt-get update')
os.system('pip install appJar')
os.system('pip install selenium')
os.system('pip install youtube-dl')
os.system('pip install ffprobe')
os.system('apt-get install libav-tools')
os.system('wget https://github.com/mozilla/geckodriver/releases/download/v0.18.0/geckodriver-v0.18.0-linux64.tar.gz')
os.system('tar -xvzf geckodriver-v0.18.0-linux64.tar.gz')
os.system('mv geckodriver /usr/bin/')
