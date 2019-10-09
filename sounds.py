from pydub import *
from pydub.playback import *
import sounddevice
import scipy.io.wavfile

class SoundManager:


    @staticmethod
    def open_audio(file_path_array):
        file_paths = file_path_array
        audio_clips = []
        for path in file_paths:
            extension = path.split('.')[1]
            audio_clips.append(AudioSegment.from_file(path, extension))

        return audio_clips

    @staticmethod
    def concatenate_audio(audio_clip_array):
        final_clip = 0
        for clip in audio_clip_array:
            final_clip = final_clip + clip
        return final_clip

    @staticmethod
    def play(audio_clip, clip_number):
        play(audio_clip)
        audio_clip.export("clip{}.mp3".format(clip_number), 'mp3')

    @staticmethod
    def record_audio(record_length, output_file_path):
        fs = 44100
        recording = sounddevice.rec(int(record_length*fs), fs, channels=2)
        sounddevice.wait()
        scipy.io.wavfile.write(output_file_path, fs, recording)
