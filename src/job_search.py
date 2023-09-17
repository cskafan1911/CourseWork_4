import json
from abc import ABC, abstractmethod

import requests


class JobSearchAPI(ABC):
    """
    Абстрактный класс для работы с API сайтов с вакансиями.
    """

    @abstractmethod
    def get_vacancies(self, job_title):
        """
        Метод возвращает информацию о вакансии по ключевому слову
        """
        pass

    @abstractmethod
    def format_vacancies(self, vacancies_data):
        """
        Метод получает данные о вакансиях и приводит к нужному формату
        :param vacancies_data: Информация о вакансиях
        :return: отформатированный список вакансий
        """
        pass


class HeadHunterAPI(JobSearchAPI):
    """
    Класс для работы с API сайта HeadHunter.
    """
    URL = "https://api.hh.ru/vacancies"

    def __init__(self):
        """
        Инициализатор класса HeadHunterAPI
        """
        self.vacancies = None
        self.job_title = None

    def get_vacancies(self, job_title):
        """
        Метод сохраняет список вакансий полученный по API
        """
        self.job_title = job_title
        params = {'text': job_title, "per_page": 50}
        response = requests.get(self.URL, params, verify=False)
        data = response.content.decode(encoding='utf-8')
        self.vacancies = json.loads(data)

        return self.vacancies

    def format_vacancies(self, vacancies_data):
        """
        Метод получает данные о вакансиях и приводит к нужному формату
        :param vacancies_data: Информация о вакансиях
        :return: отформатированный список вакансий
        """
        pass



class SuperJobAPI(JobSearchAPI):
    """
    Класс для работы с API сайта SuperJob.
    """
    pass
