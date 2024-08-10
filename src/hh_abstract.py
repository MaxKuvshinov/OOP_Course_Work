from abc import ABC, abstractmethod
from typing import Dict, List

import requests


class GetVacancies(ABC):
    """Абстрактный класс для работы с API"""

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_response(self, keyword: str, per_page: int) -> requests.Response:
        """Получение ответа от API."""
        pass

    @abstractmethod
    def get_vacancies(self, keyword: str, per_page: int) -> List[Dict]:
        """Получение данных о вакансиях"""
        pass
