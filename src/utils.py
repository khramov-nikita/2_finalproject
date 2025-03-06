import json
import os


path = os.path.dirname(__file__)
vacancies_path = os.path.join(path[:-3], "data", "vacancies.json")
vacancies_formated_path = os.path.join(path[:-3], "data", "vacancies_formated.json")


def reformat_json(json_path, formated):
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    with open(formated, "w", encoding="utf-16") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    reformat_json(vacancies_path, vacancies_formated_path)
