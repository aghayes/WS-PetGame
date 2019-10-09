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
# s_answer = input(":")
# if s_answer == question1:
#     print("good job")
# else:
#     print("sorry")
print("record your answer!")
sound_manager.record_audio(5, 'answer1.wav')

new_array = sound_manager.open_audio([scenes[1].events[1][0], scenes[1].events[0][0]])
clip2 = sound_manager.concatenate_audio(new_array)
sound_manager.play(clip2, '2')

question2 = question_box.order([scenes[1].events[1], scenes[1].events[0]])
s_answer = input(":")
if s_answer == question2:
    print("good job")
else:
    print("sorry")
