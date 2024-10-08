from abc import ABC, abstractmethod
import json


class Item(ABC):

    @abstractmethod
    def to_dict(self):
        pass

    @abstractmethod
    def to_json(self):
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


if __name__ == "__main__":
    vacancy = Vacancy("1", "2", "3", "4", "5")
    print(vacancy.to_json())
    print(vacancy.to_dict())
