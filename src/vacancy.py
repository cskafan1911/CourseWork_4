class Vacancy:
    """
    Класс для работы с вакансиями
    """
    def __init__(self, vacancies_data):
        """
        Инициализация класса Vacancy
        :param vacancies_data: данные о вакансиях
        """
        self.validate_data = self.format_salary(vacancies_data)

    @staticmethod
    def format_salary(data):
        """
        Метод для обработки данных по зарплате в нужный формат
        :param data: Список вакансий
        :return: Список вакансий с отформатированной зарплатой
        """
        for data_list in data:
            for salary in data_list:
                if salary['Зарплата'] is None:
                    formatted_salary = 0
                elif isinstance(salary['Зарплата'], dict):
                    if isinstance(salary['Зарплата']['from'], int) and not isinstance(salary['Зарплата']["to"], int):
                        formatted_salary = salary['Зарплата']["from"]
                    elif not isinstance(salary['Зарплата']['from'], int) and isinstance(salary['Зарплата']["to"], int):
                        formatted_salary = salary['Зарплата']["to"]
                    elif not isinstance(salary['Зарплата']['from'], int) and not isinstance(salary['Зарплата']["to"],
                                                                                            int):
                        formatted_salary = 0
                    else:
                        formatted_salary = max(salary['Зарплата']['to'], salary['Зарплата']["from"])

                    if salary['Зарплата']['currency'] == 'USD':
                        formatted_salary *= 96.65
                    elif salary['Зарплата']['currency'] == 'EUR':
                        formatted_salary *= 103.09
                    elif salary['Зарплата']['currency'] == 'BYR':
                        formatted_salary *= 29.59

                elif isinstance(salary, list):
                    formatted_salary = max(salary['Зарплата'])

                salary['Зарплата'] = round(formatted_salary)

        return data
