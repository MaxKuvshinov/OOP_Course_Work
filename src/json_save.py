from src.save_file import Save
import json


class JsonSave(Save):
    def __init__(self, filename):
        super().__init__(filename)


    def write_to_file(self):
        pass

    def get_data(self):
        pass

    def del_from_file(self):
        pass