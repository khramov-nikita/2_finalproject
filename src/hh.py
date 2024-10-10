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
        self.url = "https://api.hh.ru/vacancies"
        self.headers = {"User-Agent": "HH-User-Agent"}
        self.params = {"text": "", "page": 0, "per_page": 100}
        self.vacancies = []
        # super().__init__(file_worker)

    def load_vacancies(self, keyword):
        """
        Метод для выгрузки вакансий
        """
        self.params["text"] = keyword

        while self.params.get("page") != 2:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()["items"]
            self.vacancies.extend(vacancies)
            self.params["page"] += 1


if __name__ == "__main__":
    processor = HH()
    processor.load_vacancies("Python developer")
    with open(dump_path, "w", encoding="utf-16") as f:
        json.dump(processor.vacancies, f, ensure_ascii=False, indent=4)
