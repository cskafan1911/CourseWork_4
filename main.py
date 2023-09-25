from src.file_manager import JSONManager, CSVManager
from src.job_search import HeadHunterAPI, SuperJobAPI
from src.vacancy import Vacancy


def user_interaction():
    """
    Функция для взаимодействия с пользователем
    """
    # Экземпляр класса для поиска вакансий на HeadHunter API
    hh_api = HeadHunterAPI()
    # Экземпляр класса для поиска вакансий на SuperJob API
    sj_api = SuperJobAPI()
    # Список экземпляров класса Vacancy
    vacancies_list = []

    platforms = int(input(f"Выберите сайт(ы) для поиска вакансий:\n"
                          f"1 - HeadHunter; 2 - SuperJob; 3 - HeadHunter и SuperJob\n"
                          f"Введите число: "))
    search_query = str(input(f"Введите ключевое слово для поиска вакансий на сайте(ах):\n"))
    top_n = int(input(f"Введите количество вакансий для вывода в ТОП-N по зарплате:\nN = "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий:\n").split()
    file_format = int(input(f"Введите формат файла для записи вакансий:\n"
                            f"1 - JSON; 2 - CSV\n"
                            f"Введите число: "))
    if platforms == 1:
        vacancies = hh_api.get_vacancies(search_query)
    elif platforms == 2:
        vacancies = sj_api.get_vacancies(search_query)
    else:
        vacancies = hh_api.get_vacancies(search_query) + sj_api.get_vacancies(search_query)

    if file_format == 2:
        vacancies_file = CSVManager()
    else:
        vacancies_file = JSONManager()

    vacancies_file.save_file(vacancies)
    for vacancy in vacancies_file.read_file():
        vacancies_list.append(Vacancy(vacancy))

    filtered_vacancies = Vacancy.filter_vacancies(vacancies_list, filter_words)

    if not filtered_vacancies:
        print("Нет вакансий, соответствующих заданным критериям.")
        return

    sorted_vacancies = Vacancy.sorted_vacancies(filtered_vacancies)
    top_n_vacancies = Vacancy.get_top_vacancies(sorted_vacancies, top_n)
    for vacancy in top_n_vacancies:
        print(vacancy.get_vacancy())


if __name__ == "__main__":
    user_interaction()
