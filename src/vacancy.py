class Vacancy:
    """Класс предоставляющий данные о вакансиях"""
    def __init__(self, name, alternate_url, salary_from, salary_to, requirement):
        self.name = name
        self.alternate_url = alternate_url
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.requirement = requirement

    def __str__(self):
        return (
            f"Название вакансии: {self.name}\n"
            f"Ссылка на данную вакансию: {self.alternate_url}\n"
            f"Заработная плата от: {self.salary_from} до {self.salary_to}\n"
            f"Описание вакансии: {self.requirement}"
        )

    def __lt__(self, other):
        return self.salary_from < self.salary_to

    def __gt__(self, other):
        return self.salary_from > self.salary_to

    @classmethod
    def vacancy_dict(cls, data):
        vacancies = []
        for item in data:
            name = item["name"],
            url = item["alternate_url"],
            salary_from = item["salary"]["from"],
            salary_to = item["salary"]["to"],
            requirement = item["snippet"]["requirement"]
            vacancy = cls(
                name=name,
                url=url,
                salary_from=salary_from,
                salary_to=salary_to,
                requirement=requirement
            )
            vacancies.append(vacancy)
        return vacancies

