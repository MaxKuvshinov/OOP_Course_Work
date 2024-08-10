from typing import Dict, Optional


class Vacancy:
    """Класс предоставляющий данные о вакансиях"""

    def __init__(
        self,
        name: str,
        alternate_url: str,
        salary_from: Optional[int],
        salary_to: Optional[int],
        requirement: Optional[str],
    ):
        self.name = name
        self.alternate_url = alternate_url
        self.salary_from = salary_from or 0
        self.salary_to = salary_to or 0
        self.requirement = requirement

    def __str__(self) -> str:
        """Строковое представление о вакансиях"""
        return (
            f"Название вакансии: {self.name}\n"
            f"Ссылка на данную вакансию: {self.alternate_url}\n"
            f"Заработная плата от: {self.salary_from} до {self.salary_to}\n"
            f"Описание вакансии: {self.requirement}"
        )

    def __lt__(self, other: "Vacancy") -> bool:
        """Сравнение по заработной плате"""
        return self.salary_from < other.salary_from

    @classmethod
    def from_hh_dict(cls, data: Dict) -> "Vacancy":
        """Создание экземпляр Vacancy из словаря"""

        salary = data.get("salary", {})
        return cls(
            data["name"],
            data["alternate_url"],
            salary.get("from", 0),
            salary.get("to", 0),
            data["snippet"].get("requirement"),
        )

    def to_dict(self) -> Dict:
        """Преобразование в словарь."""
        return {
            "name": self.name,
            "alternate_url": self.alternate_url,
            "salary_from": self.salary_from,
            "salary_to": self.salary_to,
            "requirement": self.requirement,
        }
