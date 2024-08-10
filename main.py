from config import VACANCIES_PATH_JSON
from src.json_save import JsonSave
from src.utils import user_interaction


def main() -> None:
    """Главная функция для запуска основной программы."""
    while True:
        print(
            "Здравствуйте!\n"
            "Для получения данных из файла нажмите - 1\n"
            "Удалить данные из файла нажмите - 2\n"
            "Чтобы выйти, нажмите - 3\n"
        )

        user_input = input("Ваш выбор: ")

        if user_input == "1":
            user_interaction()
            break
        elif user_input == "2":
            deleter = JsonSave(VACANCIES_PATH_JSON)
            deleter.del_from_file()
            print("Данные из файла успешно удалены!")
            break
        elif user_input == "3":
            print("Выход из программы. До свидания!")
            break
        else:
            print("Неверный ввод. Пожалуйста, попробуйте снова.")


if __name__ == "__main__":
    main()
