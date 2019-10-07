import json


class Scene:


    def __init__(self, json_string_array):
        self.events = []
        scene_info = {}
        # parse json from json_string
        for string in json_string_array:
            scene_info.update(json.loads(string))
        # initialize values from the json scene_info
        self.header = scene_info["header"]

        # iterates through all values in the scene scene_info and appends the event array to self.event.
        # events are of the form event[0] is a sound clip file path, event[1] is the description in present [2] in past
        # You need to call SoundManager.open_audio(array_of_file_paths_to_open) and then take those and call
        # SoundManager.concatenate_audio(array_of_sound_objects_from_OpenAudio_to_be_joined) then
        # SoundManager.play(Concatenated_sound, clip_number_for_export)
        for key in scene_info:
            # used to skip the header key
            if key == 'header':
                continue
            else:
                self.events.append(scene_info[key])
