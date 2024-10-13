from abc import ABC, abstractmethod
import json


class Saver(ABC):

    def add(self, vacancy):
        pass

    def delete(self):
        pass


class VacancySaver(Saver):

    def __init__(self, path):
        self.path = path

    def add(self, vacancy):
        with open(self.path, "a") as file:
            file.write(vacancy + "\n")

    def delete(self):
        with open(self.path, "w") as file:
            file.write("")
