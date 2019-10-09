import random
import pyttsx3


class Questions:

    def __init__(self):

        # initialize engine for pyttsx3 which handles speech synth
        self.engine = pyttsx3.init()
        rate = self.engine.getProperty('rate')
        self.engine.setProperty('rate', rate-50)

        self.answer = ''

    def order(self, ordered_events):

        # takes two random events from the ordered list and saves them to event_choices
        event_choices = random.sample(ordered_events, 2)
        # shuffles the event_choices array a random number of times between 0 and 10 to create a good random order
        # for some reason simply calling random.shuffle didn't seem random.
        for i in range(random.randint(0, 10)):
            random.shuffle(event_choices)

        # checks where the events in event_choices where in the ordered list of events in order to get event chronology
        first_index = ordered_events.index(event_choices[0])
        second_index = ordered_events.index(event_choices[1])
        # asks the question
        self.engine.say("Did the " + event_choices[0][1] + " before or after the " + event_choices[1][2])
        self.engine.runAndWait()
        # checks the chronology and returns the answer based on it
        if first_index > second_index:
            self.answer = "after"
        else:
            self.answer = "before"
        return self.answer
