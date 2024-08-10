from abc import ABC, abstractmethod
from typing import List, Dict


class Save(ABC):
    def __init__(self, filename: str):
        self.filename = filename

    @abstractmethod
    def save_to_file(self, vacancies: List[Dict]) -> None:
        pass

    @abstractmethod
    def read_from_file(self) -> List[Dict]:
        pass

    @abstractmethod
    def del_from_file(self) -> None:
        pass

