import random
import pyttsx3


class Questions:

    def __init__(self):
	# sets up the the text to speech engine that is used
	# to speak the questions
        self.engine = pyttsx3.init()
        rate = self.engine.getProperty('rate')
        self.engine.setProperty('rate', rate-50)

        self.question = ''
        self.answer = ''

    @staticmethod
    def check(answer, question):
        question_answer = question[1]

        if question_answer in answer:
            return True
        else:
            return False

    # function that prevents the engine from having to hold the
    # logic that takes a question_type into a fucntion call
    def select_question(self, question_type, events):
        if question_type == "who":
            return self.who(events)
        elif question_type == "order":
            return self.order(events)

    def who(self, events):
        # randomly picks an event from the choices
        event_choice = random.sample(events, 1)

        # asks the question
        self.question = event_choice[0][3] + "?"
        self.engine.say(self.question)
        self.engine.runAndWait()

        # returns the answer
        self.answer = event_choice[0][4]
        return (self.question, self.answer, 0)

    def order(self, ordered_events):
        # takes two random events from the ordered list and saves them to event_choices

        event_choices = random.sample(ordered_events, 2)
        random.shuffle(event_choices)
        first_index = ordered_events.index(event_choices[0])
        second_index = ordered_events.index(event_choices[1])

        # asks the question
        self.question = "Did the " + event_choices[0][1] + " before or after the " + event_choices[1][2]
        self.engine.say(self.question)

        self.engine.runAndWait()
        if first_index > second_index:
            self.answer = "after"
        else:
            self.answer = "before"
        return (self.question, self.answer, 1)
