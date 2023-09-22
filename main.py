from src.file_manager import JSONManager, CSVManager
from src.job_search import HeadHunterAPI, SuperJobAPI
from src.vacancy import Vacancy


# Экземпляр класса для поиска вакансий на HeadHunter API
hh_api = HeadHunterAPI()
# Экземпляр класса для поиска вакансий на SuperJob API
sj_api = SuperJobAPI()
# Список вакансий полученных с SuperJob
hh_vacancies = hh_api.get_vacancies('user_request')
# Список вакансий полученных с HeadHunter
sj_vacancies = sj_api.get_vacancies('user_request')
# Экземпляр класса JSONManager для HeadHunter
hh_json = JSONManager()
# Экземпляр класса JSONManager для SuperJob
sj_json = JSONManager()
# Экземпляр класса CSVManager для HeadHunter
hh_csv = CSVManager()
# Экземпляр класса CSVManager для SuperJob
sj_csv = CSVManager()


def user_interaction():
    """
    Функция для взаимодействия с пользователем
    """
    platforms = int(input(f"Выберите сайт(ы) для поиска вакансий:\n"
                          f"1 - HeadHunter; 2 - SuperJob; 3 - HeadHunter и SuperJob\n"
                          f"Введите число: "))
    search_query = str(input(f"Введите ключевое слово для поиска вакансий на сайте(ах):\n"))
    top_n = int(input(f"Введите количество вакансий для вывода в ТОП-N по зарплате:\nN = "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий:\n").split()


if __name__ == "__main__":
    user_interaction()
