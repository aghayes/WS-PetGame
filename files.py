import re
from scene import *


class ParseJson:

    scenes = []

    def __init__(self, file_path):

        file = open(file_path, 'r')
        scene = []
        for line in file:
            if re.search("\\[{2}.*\\]{2}", line):
                self.scenes.append(Scene(scene))
                scene = []
                continue
            scene.append('{'+line+'}')

    def get_scenes(self):
        return self.scenes
