# IMPORTANT
# this file must be in the properly formatted story file inorder to work
# proper format is Story\scene_whatever_name\Whatever_clips.wav


import os
import engine.sounds as s


class Playback:

    @staticmethod
    def playback():
        soundmanager = s.SoundManager()
	# iterates over all the scene files in the story file
        for scene in os.listdir(os.getcwd()):
            sounds = []
	    
	    # used to skip the playback.py file itself
            if '.py' in scene:
                continue
            for file in os.listdir(os.getcwd() + "\\" + scene):
                sounds.append(file)
            cliparray = soundmanager.open_saved_audio(sounds, os.getcwd() + "\\" + scene)
            clip = soundmanager.concatenate_audio(cliparray)
            soundmanager.play_saved(clip)


Playback.playback()
