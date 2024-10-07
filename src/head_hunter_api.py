from abc import ABC, abstractmethod
import requests


class ApiGetter(ABC):

    """"Абстрактный класс для подключения к API и получения данных"""

    @abstractmethod
    def connect_to_api(self):
        pass

    @abstractmethod
    def get_data(self):
        pass


class HeadHunterApi(ApiGetter):

    """Клас для работы с API запросами на Head Hunter"""

    def connect_to_api(self):
        pass

    def get_data(self):
        pass
