from abc import ABC, abstractmethod
from typing import Dict, List


class Save(ABC):
    """Абстрактный класс для работы с файлом"""

    def __init__(self, filename: str):
        self.filename = filename

    @abstractmethod
    def save_to_file(self, vacancies: List[Dict]) -> None:
        """Метод, который сохраняет данные в файл"""
        pass

    @abstractmethod
    def read_from_file(self) -> List[Dict]:
        """Метод, который читает данные из файла"""
        pass

    @abstractmethod
    def del_from_file(self) -> None:
        """Метод, который удаляет данные из файла"""
        pass
