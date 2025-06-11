from bs4 import BeautifulSoup  # импортируем библиотеку BeautifulSoup
import requests  # импортируем библиотеку requests


def parse():
    url = 'https://omgtu.ru/general_information/the-structure/the-department-of-university.php'  # передаем необходимы URL адрес
    page = requests.get(url)  # отправляем запрос методом Get на данный адрес и получаем ответ в переменную
    print(page.status_code)  # смотрим ответ
    soup = BeautifulSoup(page.text, "html.parser")  # передаем страницу в bs4

    block = soup.findAll('div', id='pagecontent')  # находим  контейнер с нужным классом
    description = ''
    for data in block:  # проходим циклом по содержимому контейнера
        if data.find('p'):  # находим тег <p>
            description = data.text  # записываем в переменную содержание тега

    print(description)

    # --- ДОБАВЛЕНО: извлечение списка кафедр и запись в файл ---
    departments = []
    for data in block:
        items = data.find_all('li')  # ищем все элементы списка
        for item in items:
            departments.append(item.text.strip())

    with open("departments.txt", "w", encoding="utf-8") as file:
        for dept in departments:
            file.write(dept + "\n")


parse()
