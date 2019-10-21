import re
from scene import *


class ParseJson:

    scenes = []

    def __init__(self, file_path):

        file = open(file_path, 'r')
        # creates an array which will hole the content of a whole scene
        scene = []
        for line in file:
            # regex that catches [[headers]] in each line if the [[header]] exists it creates a new scene object using
            # the scene array and then appends it to the scenes array
            if re.search("\\[{2}.*\\]{2}", line):
                self.scenes.append(Scene(scene))
                scene = []
                continue
            # if there is no [[header]] we simply add the line to the scene array which is just a bunch of json
            # we add the necessary { and } here so that the .nar file is cleaner visually
            scene.append('{'+line+'}')

    def get_scenes(self):
        return self.scenes
