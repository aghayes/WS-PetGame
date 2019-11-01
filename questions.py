import random
import pyttsx3


class Questions:

    def __init__(self):

        self.engine = pyttsx3.init()
        rate = self.engine.getProperty('rate')
        self.engine.setProperty('rate', rate-50)

        self.question = ''
        self.answer = ''

    def check(self, answer, question):
        question_answer = question[1]

        if question_answer in answer:
            return True
        else:
            return False

<<<<<<< HEAD
    def order(self, ordered_events):
        # takes two random events from the ordered list and saves them to event_choices
=======
>>>>>>> 7711ba3e3fe52e8f34d5e2470f685f39caad440e
        event_choices = random.sample(ordered_events, 2)
        random.shuffle(event_choices)
        first_index = ordered_events.index(event_choices[0])
        second_index = ordered_events.index(event_choices[1])
<<<<<<< HEAD
        # asks the question
        self.question = "Did the " + event_choices[0][1] + " before or after the " + event_choices[1][2]
        self.engine.say(self.question)
=======
        self.engine.say("Did the " + event_choices[0][1] + " before or after the " + event_choices[1][2])
>>>>>>> 7711ba3e3fe52e8f34d5e2470f685f39caad440e
        self.engine.runAndWait()
        if first_index > second_index:
            self.answer = "after"
        else:
            self.answer = "before"
        return (self.question,self.answer)
