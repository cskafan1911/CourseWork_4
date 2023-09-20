import json
import os
from csv import DictReader, DictWriter
from abc import ABC, abstractmethod
from config import FILENAME


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
    def read_file(self):
        """
        Метод для чтения файла
        """
        pass


class JSONManager(FileManager):
    """
    Класс для работы с файлами формата json
    """

    def __init__(self):
        self.__filename = FILENAME + ".json"

    def save_file(self, data):
        """
        Метод сохраняет список вакансий в файл формата JSON
        """

        if os.path.exists(self.__filename):
            with open(self.__filename, 'r', encoding='utf-8') as file:
                vacancy_data = json.load(file)
        else:
            vacancy_data = []

        vacancy_data.append(data)

        with open(self.__filename, 'w', encoding='utf-8') as file:
            json.dump(vacancy_data, file, ensure_ascii=False, indent=2)

    def read_file(self):
        """
        Метод для чтения файла
        """
        with open(self.__filename, 'r', encoding='utf-8') as json_file:
            json_data = json.load(json_file)

        return json_data


class CSVManager(FileManager):
    """
    Класс для работы с файлами формата CSV
    """

    def __init__(self):
        self.__filename = FILENAME + ".csv"

    def save_file(self, data):
        """
        Метод сохраняет данные в файл нужного формата
        :param data: Данные для сохранения
        """
        reader = [value for value in data]
        headers = [key for key in data[0].keys()]

        if os.path.exists(self.__filename):
            with open(self.__filename, 'a',  encoding='utf-8-sig') as file:
                writer = DictWriter(file, fieldnames=headers)
                for line in reader:
                    writer.writerow(line)

        else:
            with open(self.__filename, 'w', encoding='utf-8-sig') as file:
                writer = DictWriter(file, fieldnames=headers)
                writer.writeheader()
                for line in reader:
                    writer.writerow(line)

    def read_file(self):
        """
        Метод для чтения файла
        """

        with open(self.__filename, 'r', encoding='utf-8-sig') as file:
            reader = DictReader(file)
            vacancies_list = []
            for line in reader:
                vacancies_list.append(line)

        return vacancies_list
