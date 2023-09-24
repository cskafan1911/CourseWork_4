class Vacancy:
    """
    Класс для работы с вакансиями
    """
    def __init__(self, vacancies_data: dict):
        """
        Инициализация класса Vacancy
        :param vacancies_data: данные о вакансиях
        """
        self.__vacancy = vacancies_data
        self.__vacancy_name = self.__vacancy['Вакансия']
        self.__city = self.__vacancy['Город']
        self.__url = self.__vacancy['Ссылка']
        self.__salary = self.format_salary(self.__vacancy['Зарплата'])
        self.__description = self.format_description(self.__vacancy['Описание'])

    def format_salary(self, salary):
        """
        Метод для обработки данных по зарплате
        :param salary: данные по зарплате
        :return: отредактированная зарплата
        """
        if salary is None:
            formatted_salary = 0
        elif isinstance(salary, dict):
            if isinstance(salary['from'], int) and not isinstance(salary["to"], int):
                formatted_salary = salary["from"]
            elif not isinstance(salary['from'], int) and isinstance(salary["to"], int):
                formatted_salary = salary["to"]
            elif not isinstance(salary['from'], int) and not isinstance(salary["to"], int):
                formatted_salary = 0
            else:
                formatted_salary = max(salary['to'], salary["from"])

            formatted_salary = self.currency_transfer(salary['currency'], formatted_salary)

        else:
            formatted_salary = max(salary)

        return round(formatted_salary)

    def format_description(self, description):
        """
        Метод обработки данных об описании вакансии
        :param description: Описание вакансии
        :return: Отредактированное описание
        """
        if description is None:

            return "Описание отсутствует"

        return description

    def currency_transfer(self, currency, quantity):
        """
        Метод конвертирует валюту в рубли
        :return: Сумма в рублях
        """
        if currency == 'USD':
            quantity *= 96.65
        elif currency == 'EUR':
            quantity *= 103.09
        elif currency == 'BYR':
            quantity *= 29.59
        elif currency == 'KZT':
            quantity *= 0.203

        return quantity

    @property
    def salary(self):

        return self.__salary

    @staticmethod
    def sorted_vacancies(data: list) -> list:
        """
        Сортирует список вакансий по зарплате
        :param data: Список вакансий
        :return: Отсортированный список вакансий
        """
        data = sorted(data, key=lambda Vacancy: Vacancy.salary, reverse=True)

        return data

    @staticmethod
    def filter_vacancies(vacancies, filter_words):
        """
        Фильтрует список вакансий по ключевым словам, указанным пользователем
        :param vacancies: Список вакансий
        :param filter_words: Ключевые слова
        :return: Отфильтрованный список вакансий по ключевым словам
        """
        filtered_vacancies = []

        for vacancy in vacancies:

            for word in filter_words:
                if word in vacancy.__description:
                    filtered_vacancies.append(vacancy)
            else:
                continue

        return filtered_vacancies

    @staticmethod
    def get_top_vacancies(vacancies, top_n):
        """
        Возвращает топ вакансий по зарплате
        :return: Топ N вакансий по зарплате
        """
        top_n_vacancies = []
        for vacancy in vacancies:
            if top_n > 0:
                top_n_vacancies.append(vacancy)
                top_n -= 1

        return top_n_vacancies

    def get_vacancy(self):
        """
        Выводит на экран информации о вакансиях
        :return: Информация о вакансии
        """
        return (f"\n{self.__vacancy_name}\n{self.__city}\n{self.__salary} рублей\n{self.__url}\n{self.__description}\n"
                f"________________________________________")
