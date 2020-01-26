import files, sounds, questions
import threading
import tkinter
from tkinter import ttk
import time
import random
import os

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

    def run(self):
        while True:
            # sets the value of prompt and label and then packs them into the frame
            global question
            self.label['text'] = question[0]
            self.label.pack()
            self.prompt['text'] = prompt
            self.prompt.pack()


# question_type determines what type of question is asked or you can pass "random" to ask a random question
def tkinterprocedure(scene, question_type):
    audio_array = scene.getallaudio()
    clip_array = sound_manager.open_audio(audio_array)
    clip = sound_manager.concatenate_audio(clip_array)
    sound_manager.play(clip, '1')

    global question
    if question_type == "random":
        pick = random.randint(0, 1)
        if pick == 0:
            question = question_box.order(scene.getallevents())
        if pick == 1:
            question = question_box.who(scene.getallevents())
    elif question_type == "who":
        question = question_box.who(scene.getallevents())
    elif question_type == "order":
        question = question_box.order(scene.getallevents())

    global prompt
    prompt = "Record your answer!"
    answer_path = "answer.wav"
    sound_manager.record_audio(7, answer_path)

    speech_from_answer = sound_manager.recognize_speech(answer_path, question[1])
    print(question[1])
    print(speech_from_answer)
    if speech_from_answer:
        prompt = "good job"
    else:
        prompt = "good try"


def pressed(event):
    # creates a separate thread that runs the update.run function so that other stuff can happen while the root.mainloop is
    # still running
    global updateThread
    updateThread = threading.Thread(target=update.run)
    updateThread.start()

    # creates a separate thread that runs the engine function so that it can run while the root.mainloop is running
    global engineThread
    ntv = "example.ntv"
    engineThread = threading.Thread(target=general_engine, args=([ntv]))
    engineThread.start()

# todo figure out how to kill the thread in a good way
# def kill(event):
#     global updateThread
#     updateThread.kill()
#     global engineThread
#     engineThread.kill()


def general_engine(ntv_name):
    scenes = files.ParseJson(ntv_name).get_scenes()
    story = []

    for scene in scenes:
        clip_array = []
        clip_array = sound_manager.open_audio(scene.getallaudio())

        clip = 0
        clip = sound_manager.concatenate_audio(clip_array)
        sound_manager.play(clip, '1')

        # global variable are used here to allow things to be read between threads correctly I should probably fix that
        # at some point but I don't want to dig into the possible solutions right now
        if scene.header == "exposition":
            continue
        else:
            global question
            question = question_box.select_question(scene.question_type, scene.getallevents())

            global prompt
            prompt = "Record your answer!"
            sound_manager.record_audio(6, scene.header + "_" + scene.question_type + "_answer.wav")

            speech_from_answer = sound_manager.recognize_speech(scene.header + "_" + scene.question_type + "_answer.wav",
                                                                question[1])
            print(question[1])
            print(speech_from_answer)
            if speech_from_answer:
                prompt = "Good job it was the " + question[1] + "."
            else:
                prompt = "Good try, but actually it was the " + question[1] + "."

            # nulls question out so that it will not show in the tkinter window
            time.sleep(3)
            question = ('', '')
        files.FileManagement.makescenefile(scene.header,
                                           ['clip1.mp3', scene.header + "_" + scene.question_type + "_answer.wav"])
        time.sleep(3)

        story.append(scene.header)

    files.FileManagement.makestoryfile(ntv_name.split(".")[0], story)


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
    speech_from_answer = sound_manager.recognize_speech('answer1.wav', question[1])
    print(question[1])
    print(speech_from_answer)
    if speech_from_answer:
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

    speech_from_answer = sound_manager.recognize_speech('answer2.wav', question[1])
    print(question[1])
    print(speech_from_answer)
    if speech_from_answer:
        prompt = "good job"
    else:
        prompt = "good try"

    question = ('', '')
    files.FileManagement.makescenefile("scene 2", ['clip2.mp3', 'answer2.wav'])
    time.sleep(3)

    files.FileManagement.makestoryfile("story", ['scene 1', 'scene 2'])


def close():
    # kills the program, there is probably a cleaner way but I don't know it
    os._exit(0)


root = tkinter.Tk()
# makes it so that the close button on the tkinter window also stops the engine thread
root.protocol("WM_DELETE_WINDOW", close)
style = ttk.Style()
style.theme_use('clam')
update = Update(root)

root.bind("<Left>", pressed)


# tkinter mainloop
root.mainloop()

