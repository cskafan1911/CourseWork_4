import json
import os
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
        self.formatted_vacancies = []
        self.job_title = ''

    def get_vacancies(self, job_title):
        """
        Метод сохраняет список вакансий полученный по API
        """
        self.job_title = job_title
        params = {'text': job_title, "per_page": 10}
        response = requests.get(self.URL, params, verify=False)
        data = response.content.decode(encoding='utf-8')
        vacancies = json.loads(data)

        return self.format_vacancies(vacancies)

    def format_vacancies(self, vacancies_data):
        """
        Метод получает данные о вакансиях и приводит к нужному формату
        :param vacancies_data: Информация о вакансиях
        :return: отформатированный список вакансий
        """

        for vacancy in vacancies_data['items']:
            vacancy_dict = {
                'Вакансия': vacancy['name'],
                'Город': vacancy['area']['name'],
                'Ссылка': vacancy['alternate_url'],
                'Зарплата': self.format_salary(vacancy['salary']),
                'Описание': vacancy['snippet']['requirement']
            }
            self.formatted_vacancies.append(vacancy_dict)

        return self.formatted_vacancies

    @staticmethod
    def format_salary(salary):
        """
        Изменяет отображение зарплаты в нужный формат
        :param salary: зарплата полученная с сайта
        :return: отформатированная зарплата
        """
        if salary is None:
            formatted_salary = 0
        else:
            if isinstance(salary['from'], int) and not isinstance(salary["to"], int):
                formatted_salary = salary["from"]
            elif not isinstance(salary['from'], int) and isinstance(salary["to"], int):
                formatted_salary = salary["to"]
            elif not isinstance(salary['from'], int) and not isinstance(salary["to"], int):
                formatted_salary = 0
            else:
                formatted_salary = salary['to'] - salary["from"]

            if salary['currency'] == 'USD':
                formatted_salary *= 96.65
            elif salary['currency'] == 'EUR':
                formatted_salary *= 103.09
            elif salary['currency'] == 'BYR':
                formatted_salary *= 29.59

        return round(formatted_salary)


class SuperJobAPI(JobSearchAPI):
    """
    Класс для работы с API сайта SuperJob.
    """
    API_KEY = os.getenv('SuperJob_API')
    URL = 'https://api.superjob.ru/2.0/vacancies/'

    headers = {'X-Api-App-Id': API_KEY}

    def __init__(self):
        """
        Инициализатор класса SuperJobAPI
        """
        self.job_title = ''
        self.formatted_vacancies = []

    def get_vacancies(self, job_title):
        """
        Метод сохраняет список вакансий полученный по API
        """

        self.job_title = job_title
        params = {'keyword': self.job_title, 'count': 10}
        response = requests.get(self.URL, headers=self.headers, params=params)
        data = response.content.decode(encoding="utf-8")
        vacancies = json.loads(data)

        return self.format_vacancies(vacancies)

    def format_vacancies(self, vacancies_data):
        """
        Метод получает данные о вакансиях и приводит к нужному формату
        :param vacancies_data: Информация о вакансиях
        :return: отформатированный список вакансий
        """

        for vacancy in vacancies_data['objects']:
            vacancy_dict = {
                'Вакансия': vacancy['profession'],
                'Город': vacancy['town']['title'],
                'Ссылка': vacancy['link'],
                'Зарплата': f"{vacancy['payment_from']} - {vacancy['payment_to']} {vacancy['currency']}",
                'Описание': vacancy['candidat']
            }
            self.formatted_vacancies.append(vacancy_dict)

        return self.formatted_vacancies
