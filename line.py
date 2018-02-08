import os

os.system('wget -q -O - archive.kali.org/archive-key.asc | apt-key add')
os.system('apt-get update')
os.system('pip install appJar')
os.system('pip install youtube-dl')
os.system('pip install ffprobe')
os.system('apt-get install libav-tools')

