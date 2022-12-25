import os
from moviepy.editor import VideoFileClip

def convert_to_mp3(filename):
    clip = VideoFileClip(filename)
    clip2 = (filename)
    #print('STRING-' + clip2 + " -\n") used for debugging
    clip.audio.write_audiofile(filename[:-4] + ".mp3")
    os.remove(clip2)
    clip.close()
