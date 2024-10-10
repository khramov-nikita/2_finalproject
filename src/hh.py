import os

import requests
import json
from abc import ABC, abstractmethod


path = os.path.dirname(__file__)
dump_path = os.path.join(path[:-3], "data", "result.json")


class Parser(ABC):
    """
    Абстрактный класс парсера
    """

    @abstractmethod
    def load_vacancies(self, keyword):
        pass


class HH(Parser):
    """
    Класс для работы с API HeadHunter
    """

    def __init__(self):
        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {"text": "", "page": 0, "per_page": 100}
        self.__vacancies = []
        # super().__init__(file_worker)

    def load_vacancies(self, keyword):
        """
        Метод для выгрузки вакансий
        """
        self.__params["text"] = keyword

        while self.__params.get("page") != 2:
            response = requests.get(self.__url, headers=self.__headers, params=self.__params)
            vacancies = response.json()["items"]
            self.__vacancies.extend(vacancies)
            self.__params["page"] += 1

    @property
    def vacancies(self):
        return self.__vacancies


if __name__ == "__main__":
    processor = HH()
    processor.load_vacancies("Python developer")
    with open(dump_path, "w", encoding="utf-16") as f:
        json.dump(processor.vacancies, f, ensure_ascii=False, indent=4)
