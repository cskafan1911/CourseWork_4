import json
import os
from abc import ABC, abstractmethod
from config import URL_HH, URL_SJ

import requests


class JobSearchAPI(ABC):
    """
    Абстрактный класс для работы с API сайтов с вакансиями.
    """

    @abstractmethod
    def get_vacancies(self, job_title: str) -> list:
        """
        Метод получает информацию с API о вакансии по ключевому слову
        """
        pass

    @abstractmethod
    def format_vacancies(self, vacancies_data: list) -> list:
        """
        Метод приводит данные о вакансиях к нужному формату
        :param vacancies_data: Информация о вакансиях
        :return: отформатированный список вакансий
        """
        pass


class HeadHunterAPI(JobSearchAPI):
    """
    Класс для работы с API сайта HeadHunter.
    """

    def __init__(self):
        """
        Инициализатор класса HeadHunterAPI
        """
        self.formatted_vacancies = []
        self.job_title = ''

    def get_vacancies(self, job_title):
        """
        Метод получает информацию с API о вакансии по ключевому слову
        """
        self.job_title = job_title
        params = {'text': job_title, "per_page": 15}
        response = requests.get(URL_HH, params, verify=False)
        data = response.content.decode(encoding='utf-8')
        vacancies = json.loads(data)

        return self.format_vacancies(vacancies)

    def format_vacancies(self, vacancies_data):
        """
        Метод приводит данные о вакансиях к нужному формату:
        {'Вакансия': ...,
        'Город': ...,
        'Ссылка': ...,
        'Зарплата': {...},
        'Описание': ...}
        :param vacancies_data: Информация о вакансиях
        :return: отформатированный список вакансий
        """

        for vacancy in vacancies_data['items']:
            vacancy_dict = {
                'Вакансия': vacancy['name'],
                'Город': vacancy['area']['name'],
                'Ссылка': vacancy['alternate_url'],
                'Зарплата': vacancy['salary'],
                'Описание': vacancy['snippet']['requirement']
            }
            self.formatted_vacancies.append(vacancy_dict)

        return self.formatted_vacancies


class SuperJobAPI(JobSearchAPI):
    """
    Класс для работы с API сайта SuperJob.
    """
    API_KEY = os.getenv('SuperJob_API')

    headers = {'X-Api-App-Id': API_KEY}

    def __init__(self):
        """
        Инициализатор класса SuperJobAPI
        """
        self.job_title = ''
        self.formatted_vacancies = []

    def get_vacancies(self, job_title):
        """
        Метод получает информацию с API о вакансии по ключевому слову
        """

        self.job_title = job_title
        params = {'keyword': self.job_title, 'count': 15}
        response = requests.get(URL_SJ, headers=self.headers, params=params)
        data = response.content.decode(encoding="utf-8")
        vacancies = json.loads(data)

        return self.format_vacancies(vacancies)

    def format_vacancies(self, vacancies_data):
        """
        Метод приводит данные о вакансиях к нужному формату:
        {'Вакансия': ...,
        'Город': ...,
        'Ссылка': ...,
        'Зарплата': [..., ...],
        'Описание': ...}
        :param vacancies_data: Информация о вакансиях
        :return: отформатированный список вакансий
        """

        for vacancy in vacancies_data['objects']:
            vacancy_dict = {
                'Вакансия': vacancy['profession'],
                'Город': vacancy['town']['title'],
                'Ссылка': vacancy['link'],
                'Зарплата': [vacancy['payment_from'], vacancy['payment_to']],
                'Описание': vacancy['candidat']
            }
            self.formatted_vacancies.append(vacancy_dict)

        return self.formatted_vacancies
