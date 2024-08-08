from abc import ABC, abstractmethod


class Save(ABC):
    def __init__(self, filename):
        self.filename = filename

    @abstractmethod
    def write_to_file(self):
        pass

    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def del_from_file(self):
        pass

