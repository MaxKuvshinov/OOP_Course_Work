import json
from typing import Dict, List

from src.save_file import Save


class JsonSave(Save):
    """Класс, который сохраняет, перезаписывает и удаляет данные из JSON - файла"""

    def __init__(self, filename: str):
        super().__init__(filename)

    def save_to_file(self, vacancies: List[Dict]) -> None:
        """Метод, который сохраняет данные в файл"""
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(vacancies, file, ensure_ascii=False, indent=4)

    def read_from_file(self) -> List[Dict]:
        """Метод, который читает данные из файла"""
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def del_from_file(self) -> None:
        """Метод, который удаляет данные из файла"""
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump([], file, ensure_ascii=False, indent=4)
