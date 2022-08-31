from re import S
# Import Libraries
from pytube import Youtube
import pytube
import os

def main():
    # Create a variable
    video_url = input('eNTER yOUTUBE video URL:')

    if os.name == 'nt':
        #getcwd() returns current working directory of a process
        path = os.getcwdb() + '\\'
    else:
        path = os.getcwdb() + '/'

    #Video Extraction 
    name = pytube.extract.video_id(video_url)
    Youtube(video_url).streams.filter(only_audio=True).first().download(filename = name)
    location = path + name + '.mp4'
    renametomp3 = path + name + '.mp3'

    # if os is windows, os.name returns 'nt'
    if os.name == 'nt':
        os.system('ren {0} {1}'.format(location, renametomp3))
    else:
        os.system('mv {0} {1}'.format(location, renametomp3))


if __name__ == '__main__':
    main()