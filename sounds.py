from pydub import *
from pydub.playback import *


class SoundManager:

    file_paths = []
    audio_clips = []

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
