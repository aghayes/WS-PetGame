import random
import pyttsx3


class Questions:

    def __init__(self):

        self.engine = pyttsx3.init()
        rate = self.engine.getProperty('rate')
        self.engine.setProperty('rate', rate-50)

        self.answer = ''

    def order(self, ordered_events):

        event_choices = random.sample(ordered_events, 2)
        print(event_choices)
        for i in range(random.randint(0, 10)):
            random.shuffle(event_choices)
        print(event_choices)

        first_index = ordered_events.index(event_choices[0])
        second_index = ordered_events.index(event_choices[1])
        self.engine.say("Did the " + event_choices[0][1] + " before or after the " + event_choices[1][2])
        self.engine.runAndWait()
        if first_index > second_index:
            self.answer = "after"
        else:
            self.answer = "before"
        return self.answer
