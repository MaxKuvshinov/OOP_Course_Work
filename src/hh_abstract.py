from abc import ABC, abstractmethod
from typing import List, Dict
import requests


class GetVacancies(ABC):
    """Абстрактный метод для работы с API"""

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_response(self, keyword: str, per_page: int) -> requests.Response:
        pass

    @abstractmethod
    def get_vacancies(self, keyword: str, per_page: int) -> List[Dict]:
        pass
