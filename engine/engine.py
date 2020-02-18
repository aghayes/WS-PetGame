import files, sounds, questions
import threading
import tkinter
from tkinter import ttk
import time
import os

question_box = questions.Questions()
sound_manager = sounds.SoundManager()
global ntv
ntv = "example.ntv"
question = ('', '')
prompt = 'Press enter to start.'


class Update:
    def __init__(self, master):
        self.master = master
        self.frame = tkinter.Frame
        # gives the text some padding
        self.master.configure(padx=50, pady=50)
        # an array to hold .ntv files for tkinter
        options = []
        # used to parse path stuff until we get to the narrative file and then find all .ntv files.
        path = os.getcwd()
        final_path = ''
        for dir in path.split("\\"):
            if 'engine' in dir:
                continue
            else:
                final_path += dir + "\\"
        final_path += 'narrative\\'
        for file in os.listdir(final_path):
            print(file[-4:])
            if file[-4:] == '.ntv':
                options.append(file)
        self.selected_ntv = tkinter.StringVar(master)
        self.selected_ntv.set(options[0])
        self.enter = tkinter.OptionMenu(master, self.selected_ntv, options)
        self.enter.pack()
        # sets up the labels we will use note question is a tuple of the form (question_text, answer)
        self.label = tkinter.Label(master, text=question[0])
        self.prompt = tkinter.Label(master, text=prompt)

    def run(self):
        while True:
            # sets the value of prompt and label and then packs them into the frame
            global question
            global prompt
            self.label['text'] = question[0]
            self.label.pack()
            self.prompt['text'] = prompt
            self.prompt.pack()

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
            if question[2] == 0:
                if speech_from_answer:
                    prompt = "Good job it was the " + question[1] + "."
                else:
                    prompt = "Good try, but actually it was the " + question[1] + "."
            elif question[2] == 1:
                if speech_from_answer:
                    prompt = "Good job it was " + question[1] + "."
                else:
                    prompt = "Good try, but actually it was " + question[1] + "."

            # nulls question out so that it will not show in the tkinter window
            time.sleep(3)
            question = ('', '')
        files.FileManagement.makescenefile(scene.header,
                                           ['clip1.wav', scene.header + "_" + scene.question_type + "_answer.wav"])
        time.sleep(3)

        story.append(scene.header)

    files.FileManagement.makestoryfile(ntv_name.split(".")[0], story)


def close():
    # kills the program, there is probably a cleaner way but I don't know it
    os._exit(0)


def return_key(event):
    # this grabs the entry box and updates it to whatever a user entered
    global ntv
    ntv = update.selected_ntv.get()
    update.enter.destroy()
    print(ntv)
    # creates a separate thread that runs the engine function so that it can run while the root.mainloop is running
    global engineThread
    engineThread = threading.Thread(target=general_engine, args=([ntv]))
    engineThread.start()
    global question
    question = ("Listen to the story please.", "")


root = tkinter.Tk()
# makes it so that the close button on the tkinter window also stops the engine thread
root.protocol("WM_DELETE_WINDOW", close)
style = ttk.Style()
style.theme_use('clam')
update = Update(root)
# creates a separate thread that runs the update.run function so that other stuff can happen while the
# root.mainloop is still running
global updateThread
updateThread = threading.Thread(target=update.run)
updateThread.start()

root.bind("<Return>", return_key)


# tkinter mainloop
root.mainloop()

