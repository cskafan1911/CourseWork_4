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

    @staticmethod
    def format_salary(salary):
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

            if salary['currency'] == 'USD':
                formatted_salary *= 96.65
            elif salary['currency'] == 'EUR':
                formatted_salary *= 103.09
            elif salary['currency'] == 'BYR':
                formatted_salary *= 29.59

        else:
            formatted_salary = max(salary)

        return round(formatted_salary)

    @property
    def salary(self):

        return self.__salary
