import questions
import sounds
import files
import threading
import tkinter
import time
import datetime

question_box = questions.Questions()
sound_manager = sounds.SoundManager()
question = ('Listen to the story please.', '')
prompt = ''


class Update:
    def __init__(self, master):
        self.master = master
        self.frame = tkinter.Frame
        # gives the text some padding
        self.master.configure(padx=50, pady=50)
        # sets up the labels we will use note question is a tuple of the form (question_text, answer)
        self.label = tkinter.Label(master, text=question[0])
        self.prompt = tkinter.Label(master, text=prompt)

<<<<<<< HEAD
    def run(self):
        while True:
            # sets the value of prompt and label and then packs them into the frame
            self.label['text'] = question[0]
            self.label.pack()
            self.prompt['text'] = prompt
            self.prompt.pack()


def engine():
    scenes = files.ParseJson('example.ntv').get_scenes()

    clip_array = sound_manager.open_audio([scenes[0].geteventaudio(0), scenes[0].geteventaudio(1),
                                           scenes[0].geteventaudio(2)])
    clip = sound_manager.concatenate_audio(clip_array)
    sound_manager.play(clip, '1')

    # make sure to set question as a global variable so that it will be read between threads correctly, same with prompt
    global question
    question = question_box.order(scenes[0].getallevents())
    global prompt
    prompt = "Record your answer!"
    sound_manager.record_audio(7, 'answer1.wav')

    # pass whatever file name you used in sound_manager.record_audio, make sure it is a pcm wav file
    speech_from_answer = sound_manager.recognize_speech('answer1.wav')
    print(speech_from_answer)
    if question_box.check(answer=speech_from_answer, question=question):
        prompt = "good job"
    else:
        prompt = "good try"

    # nulls question out so that it will not show in the tkinter window
    question = ('', '')
    files.FileManagement.makescenefile("scene 1", ['clip1.mp3', 'answer1.wav'])
    time.sleep(3)

    new_array = sound_manager.open_audio([scenes[1].events[1][0], scenes[1].events[0][0]])
    clip2 = sound_manager.concatenate_audio(new_array)
    sound_manager.play(clip2, '2')

    question = question_box.order(scenes[1].getallevents())
    prompt = "Record your answer!"
    sound_manager.record_audio(7, 'answer2.wav')

    speech_from_answer = sound_manager.recognize_speech('answer2.wav')
    print(speech_from_answer)
    if question_box.check(speech_from_answer, question):
        prompt = "good job"
    else:
        prompt = "good try"

    question = ('', '')
    files.FileManagement.makescenefile("scene 2", ['clip2.mp3', 'answer2.wav'])
    time.sleep(3)

    files.FileManagement.makestoryfile("story", ['scene 1', 'scene 2'])


root = tkinter.Tk()
update = Update(root)

# creates a separate thread that runs the update.run function so that other stuff can happen while the root.mainloop is
# still running
updateThread = threading.Thread(target=update.run)
updateThread.start()

# creates a separate thread that runs the engine function so that it can run while the root.mainloop is running
engineThread = threading.Thread(target=engine)
engineThread.start()

# tkinter mainloop
root.mainloop()
=======
question1 = question_box.order([scenes[0].events[0], scenes[0].events[1]])
s_answer = input(":")
if s_answer == question1:
    print("good job")
else:
    print("sorry")
new_array = sound_manager.open_audio([scenes[1].events[1][0], scenes[1].events[0][0]])
clip2 = sound_manager.concatenate_audio(new_array)
sound_manager.play(clip2, '2')
question2 = question_box.order([scenes[1].events[1], scenes[1].events[0]])
s_answer = input(":")
if s_answer == question2:
    print("good job")
else:
    print("sorry")
>>>>>>> 7711ba3e3fe52e8f34d5e2470f685f39caad440e
