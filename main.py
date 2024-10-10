from src.hh import HH


def main():
    vacancies = HH()
    vacancies.load_vacancies("Python разработчик")
    print(vacancies.vacancies[:5])


if __name__ == "__main__":
    main()
