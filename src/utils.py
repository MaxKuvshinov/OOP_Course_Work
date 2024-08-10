from config import VACANCIES_PATH_JSON
from src.hh_api import VacanciesAPI
from src.vacancy import Vacancy
from src.json_save import JsonSave


def user_interaction() -> None:

    keyword = input("Введите название интересующей вас профессии: ").lower()
    per_page = int(input("Какое количество профессий вывести: "))

    head_hunter_api = VacanciesAPI()
    vacancies = head_hunter_api.get_vacancies(keyword, per_page)
    vacancies = [Vacancy.from_hh_dict(vacancy) for vacancy in vacancies]
    vacancies = sorted(vacancies, reverse=True)

    print("Топ выбранных вакансии с HeadHunter по заработной плате: \n")
    for i in sorted(vacancies, reverse=True):
        print(i)

    vacancies = [vacancy.to_dict() for vacancy in vacancies]
    saver = JsonSave(VACANCIES_PATH_JSON)

    saver.save_to_file(vacancies)
    saver.read_from_file()
    print("Данные записаны в json-файл")