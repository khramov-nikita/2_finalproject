from src.hh import HH
from src.vacancy import Vacancy, VacanciesProcessor


def main():
    hh = HH()
    hh.load_vacancies("python developer")
    data = hh.vacancies
    processor = VacanciesProcessor()
    processor.create_vacancies(data)
    print(processor)


if __name__ == "__main__":
    main()
