import os
import engine.sounds as s


class Playback:

    @staticmethod
    def playback():
        soundmanager = s.SoundManager()
        for scene in os.listdir(os.getcwd()):
            sounds = []

            if '.py' in scene:
                continue
            for file in os.listdir(os.getcwd() + "\\" + scene):
                sounds.append(file)
            cliparray = soundmanager.open_saved_audio(sounds, os.getcwd() + "\\" + scene)
            clip = soundmanager.concatenate_audio(cliparray)
            soundmanager.play_saved(clip)


Playback.playback()
