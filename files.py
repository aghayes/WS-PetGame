import re
from scene import *
import os
import shutil

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
<<<<<<< HEAD
            # if there is no [[header]] we simply add the line to the scene array which is just a bunch of json
            # we add the necessary { and } here so that the .ntv file is cleaner visually
=======
>>>>>>> 7711ba3e3fe52e8f34d5e2470f685f39caad440e
            scene.append('{'+line+'}')

    def get_scenes(self):
        return self.scenes


class FileManagement:

    @staticmethod
    def makescenefile(folder_name, file_name_array):
        # gets the current path and appends the folder_name to create total_path so we can move files inside it
        cur_path = os.getcwd()
        total_path = cur_path + "\\" + folder_name

        try:
            os.mkdir(total_path)
        except FileExistsError as e:
            pass

        # for every file in the file_name_array move it to the directory we created
        for file_name in file_name_array:
            file_path = cur_path + "\\" + file_name
            new_file_path = total_path + "\\" + file_name

            shutil.move(file_path, new_file_path)

    @staticmethod
    def makestoryfile(folder_name, file_name_array):
        # gets the current path and appends the folder_name to create total_path so we can move files inside it
        cur_path = os.getcwd()
        total_path = cur_path + "\\" + folder_name

        try:
            os.mkdir(total_path)
        except FileExistsError as e:
            pass

        # for every directory in the file_name_array move it to the directory we created then remove the old directories
        for file_name in file_name_array:
            file_path = cur_path + "\\" + file_name
            new_file_path = total_path + "\\" + file_name

            shutil.copytree(file_path, new_file_path)
            shutil.rmtree(file_path, new_file_path)
