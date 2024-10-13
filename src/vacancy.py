from abc import ABC, abstractmethod
import json


class Item(ABC):
    """
    Абстрактный метод для вакансии
    """

    @abstractmethod
    def to_dict(self):
        pass

    @abstractmethod
    def to_json(self):
        pass


class Processor(ABC):
    """
    Абстрактный метод для процессора вакансий
    """

    @abstractmethod
    def add_vacancy(self, *args):
        pass


class Vacancy(Item):
    """
    Класс для репрезентации вакансии
    """

    __slots__ = ("name", "link", "pay", "area", "description")

    def __init__(self, name, link, pay, area, description):
        self.name = name
        self.link = link
        self.pay = pay
        self.area = area
        self.description = description

    def to_dict(self):
        return {
            "name": self.name,
            "link": self.link,
            "pay": self.pay,
            "area": self.area,
            "description": self.description,
        }

    def to_json(self):
        return json.dumps(self.to_dict())


class VacanciesProcessor(Processor):

    __slots__ = "vacancies"

    def __init__(self, vacancies: None | list = None):
        self.__vacancies = vacancies if vacancies else []

    def create_vacancies(self, hh_data):
        for vacancy in hh_data:
            if isinstance(vacancy["salary"], dict):
                salary = vacancy["salary"]
            else:
                salary = "Не указано"
            self.add_vacancy(
                Vacancy(
                    vacancy["name"],
                    vacancy["alternate_url"],
                    salary,
                    vacancy["area"],
                    f'Обязанности: {vacancy["snippet"]["requirement"]}\n'
                    f'Требования: {vacancy["snippet"]["responsibility"]}',
                )
            )

    def vacancy_to_list(self):
        result = []
        for vacancy in self.__vacancies:
            result.append(vacancy.to_dict())
        return result

    def add_vacancy(self, *args: Vacancy):
        for arg in args:
            if isinstance(arg, Vacancy):
                self.__vacancies.append(arg)
            else:
                raise TypeError

    def __str__(self):
        result_list = []
        for vacancy in self.__vacancies:
            if isinstance(vacancy.pay, dict):
                result_list.append(
                    f'{vacancy.name: ^60}\n{vacancy.description}\n'
                    f'Зарплата: {vacancy.pay["from"]} {vacancy.pay["currency"]}\n\n'
                )
            else:
                result_list.append(f"{vacancy.name: ^60}\n{vacancy.description}\nЗарплата: {vacancy.pay}\n\n")
        return "".join(result_list)


if __name__ == "__main__":
    pass
