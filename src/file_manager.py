import json
from abc import ABC, abstractmethod

from src.vacancy import Vacancy


class FileManager(ABC):
    """
    Абстрактный класс для работы с файлами
    """
    @abstractmethod
    def save_file(self, data):
        """
        Метод сохраняет данные в файл нужного формата
        :param data: Данные для сохранения
        """
        pass

    @abstractmethod
    def read_file(self, filename):
        """
        Метод для чтения файла
        :param filename: имя файла для чтения
        """
        pass


class JSONManager(FileManager):
    """
    Класс для работы с файлами формата json
    """
    def save_file(self, data):
        """
        Метод сохраняет список вакансий в файл формата JSON
        """
        with open('files_witn_vacancies/HH_vacancies.json', 'w', encoding='utf-8') as json_file:
            json.dump(self.verified_vacancies, json_file, ensure_ascii=False, indent=2)


class CSVManager(FileManager):
    """
    Класс для работы с файлами формата CSV
    """