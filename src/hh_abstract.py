from abc import ABC, abstractmethod


class GetVacancies(ABC):
    """Абстрактный метод для работы с API"""

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_response(self, keyword, per_page):
        pass

    @abstractmethod
    def get_vacancies(self, keyword, per_page):
        pass
