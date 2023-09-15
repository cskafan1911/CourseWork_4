from abc import ABC


class JobSearchAPI(ABC):
    """
    Абстрактный класс для работы с API сайтов с вакансиями.
    """
    pass


class HeadHunterAPI(JobSearchAPI):
    """
    Класс для работы с API сайта HeadHunter.
    """
    pass


class SuperJobAPI(JobSearchAPI):
    """
    Класс для работы с API сайта SuperJob.
    """
    pass

