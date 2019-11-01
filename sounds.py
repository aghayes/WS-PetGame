from pydub import *
from pydub.playback import *
<<<<<<< HEAD
import sounddevice
import scipy.io.wavfile
import os
import speech_recognition
=======

>>>>>>> 7711ba3e3fe52e8f34d5e2470f685f39caad440e


<<<<<<< HEAD
class SoundManager:
=======
    file_paths = []
    audio_clips = []
>>>>>>> 7711ba3e3fe52e8f34d5e2470f685f39caad440e

    def open_audio(self, file_path_array):
        self.file_paths = file_path_array

        for path in self.file_paths:
            extension = path.split('.')[1]
            self.audio_clips.append(AudioSegment.from_file(path, extension))

        return self.audio_clips

    def concatenate_audio(self, audio_clip_array):
        final_clip = 0
        for clip in audio_clip_array:
            final_clip = final_clip + clip
        return final_clip

    @staticmethod
    def play(audio_clip, clip_number):
        play(audio_clip)
        audio_clip.export("clip{}.mp3".format(clip_number), 'mp3')
<<<<<<< HEAD

    # this is the basic idea of the beep function but I need to find the actual file and add the path and extension
    # @staticmethod
    # def beep():
    #     audio_clip = AudioSegment.from_file("beep path", 'beep extension')
    #     play(audio_clip)

    @staticmethod
    def record_audio(record_length, output_file_path):
        fs = 44100
        # records audio from the mic for the duration of record_length in seconds
        #
        # the dtype='int32' sets the datatype which ensures that the scipy.io writes it as as pcm wav file
        # if you don't include it then the speech recognition won't open the file because it only reads pcm wav files
        recording = sounddevice.rec(int(record_length*fs), fs, channels=2, dtype='int32')
        sounddevice.wait()
        scipy.io.wavfile.write(output_file_path, fs, recording)

    @staticmethod
    def recognize_speech(file_name):
        # set up a recognizer using the speech_recognition library
        r = speech_recognition.Recognizer()
        # creates the file path from the total path and the file_name
        file = os.path.join(os.path.dirname(os.path.realpath(__file__)), file_name)
        # opens the audio file to the audio type that is needed by the recognizer
        with speech_recognition.AudioFile(file) as source:
            audio = r.record(source)
        # uses the recognize_sphinx part of the library which requires pocketsphinx but works offline
        # returns a string
        try:
            return r.recognize_sphinx(audio)
        except speech_recognition.UnknownValueError as e:
            return 'failed to recognize audio'
=======
>>>>>>> 7711ba3e3fe52e8f34d5e2470f685f39caad440e
