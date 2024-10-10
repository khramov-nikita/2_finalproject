from abc import ABC, abstractmethod
import json


class Item(ABC):

    @abstractmethod
    def to_dict(self):
        pass

    @abstractmethod
    def to_json(self):
        pass


class Processor(ABC):

    @abstractmethod
    def add_vacancy(self, *args):
        pass


class Vacancy(Item):

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

    def add_vacancy(self, *args: Vacancy):
        for arg in args:
            if issubclass(arg.__class__, Vacancy):
                self.__vacancies.append(arg)
            else:
                raise TypeError

    def __str__(self):
        result_list = []
        for vacancy in self.__vacancies:
            result_list.append(f"{vacancy.name}: {vacancy.description}\n")
        return "".join(result_list)


if __name__ == "__main__":
    vacancy_1 = Vacancy("1", "2", "3", "4", "5")
    vacancy_2 = Vacancy("6", "7", "8", "9", "0")
    data = VacanciesProcessor()
    data.add_vacancy(vacancy_1)
    data.add_vacancy(vacancy_2)
    print(vacancy_1.to_json())
    print(vacancy_2.to_dict())
    print(data)

