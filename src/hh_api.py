from typing import Dict, List

import requests
from src.hh_abstract import GetVacancies


class VacanciesAPI(GetVacancies):
    """Класс для получения данных по API"""

    def __init__(self):
        self.url = "https://api.hh.ru/vacancies"
        self.headers = {"User-Agent": "HH-User-Agent"}
        self.params = self.params = {"text": "", "per_page": "", "only_with_salary": True}

    def get_response(self, keyword: str, per_page: int) -> requests.Response:
        """Получение ответа от API."""
        self.params.update({"text": keyword, "per_page": per_page})
        try:
            response = requests.get(self.url, params=self.params, headers=self.headers)
            response.raise_for_status()
            return response
        except requests.RequestException as e:
            print(f"Ошибка получения данных из API: {e}")
            return None

    def get_vacancies(self, keyword: str, per_page: int) -> List[Dict]:
        """Получение данных о вакансиях из ответа API."""
        response = self.get_response(keyword, per_page)
        if response:
            return response.json().get("items", [])
        return []
