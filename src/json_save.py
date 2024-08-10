from src.save_file import Save
import json
from typing import List, Dict


class JsonSave(Save):
    def __init__(self, filename: str):
        super().__init__(filename)

    def save_to_file(self, vacancies: List[Dict]) -> None:
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(vacancies, file, ensure_ascii=False, indent=4)

    def read_from_file(self) -> List[Dict]:
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def del_from_file(self) -> None:
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump([], file, ensure_ascii=False, indent=4)
