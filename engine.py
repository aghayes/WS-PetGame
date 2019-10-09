import questions
import sounds
import files

question_box = questions.Questions()
sound_manager = sounds.SoundManager()

scenes = files.ParseJson('example.nar').get_scenes()

clip_array = sound_manager.open_audio([scenes[0].events[0][0], scenes[0].events[1][0]])
clip = sound_manager.concatenate_audio(clip_array)
sound_manager.play(clip, '1')

question1 = question_box.order([scenes[0].events[0], scenes[0].events[1]])
print("Record your answer!")
sound_manager.record_audio(7, 'answer1.wav')
print("Good job.")

new_array = sound_manager.open_audio([scenes[1].events[1][0], scenes[1].events[0][0]])
clip2 = sound_manager.concatenate_audio(new_array)
sound_manager.play(clip2, '2')

question2 = question_box.order([scenes[1].events[1], scenes[1].events[0]])
print("Record your answer!")
sound_manager.record_audio(7, 'answer2.wav')
print("Good job.")
