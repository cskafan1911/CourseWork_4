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

    def format_salary(self, salary: dict | list | None) -> int:
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

    @staticmethod
    def format_description(description: str) -> str:
        """
        Метод обработки данных об описании вакансии
        :param description: Описание вакансии
        :return: Отредактированное описание
        """
        if description is None:

            return "Описание отсутствует"

        return description

    @staticmethod
    def currency_transfer(currency: str, quantity: int) -> float:
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

    @staticmethod
    def sorted_vacancies(vacancies_list: list) -> list:
        """
        Сортирует список вакансий по зарплате
        :param vacancies_list: Список вакансий
        :return: Отсортированный список вакансий
        """
        sorted_list_vacancies = sorted(vacancies_list, key=lambda Vacancy: Vacancy.__salary, reverse=True)

        return sorted_list_vacancies

    @staticmethod
    def filter_vacancies(vacancies: list, filter_words: list) -> list:
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
    def get_top_vacancies(vacancies: list, top_n: int) -> list:
        """
        Возвращает топ вакансий по зарплате
        :param vacancies: Список вакансий
        :param top_n: Число выводимых вакансий
        :return: Топ N вакансий по зарплате
        """
        top_n_vacancies = []
        for vacancy in vacancies:
            if top_n > 0:
                top_n_vacancies.append(vacancy)
                top_n -= 1

        return top_n_vacancies

    def get_vacancy(self) -> str:
        """
        Выводит на экран информации о вакансиях
        :return: Информация о вакансии
        """
        return (f"\n{self.__vacancy_name}\n{self.__city}\n{self.__salary} рублей\n{self.__url}\n{self.__description}\n"
                f"________________________________________")

    def __str__(self) -> str:
        """
        Метод для возвращения строкового представления объекта.
        :return: строковое представление объекта
        """
        result = (f"Вакансия: {self.__vacancy}\n"
                  f"Город: {self.__city}\n"
                  f"Зарплата: {self.__salary}\n"
                  f"Ссылка: {self.__url}")

        return result
