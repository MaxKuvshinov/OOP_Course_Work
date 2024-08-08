import requests
from src.hh_abstract import GetVacancies


class VacanciesAPI(GetVacancies):
    """Класс для получения данных по API"""
    def __init__(self):
        self.url = "https://api.hh.ru/vacancies"
        self.headers = {"User-Agent": "HH-User-Agent"}
        self.params = self.params = {"text": "", "per_page": "", "only_with_salary": True}

    def get_response(self, keyword, per_page):
        self.params["text"] = keyword
        self.params["per_page"] = per_page
        return requests.get(self.url, params=self.params)

    def get_vacancies(self, keyword, per_page):
        return self.get_response(keyword, per_page).json()["items"]
