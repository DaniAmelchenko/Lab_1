import requests
from bs4 import BeautifulSoup

def get_departments():
    url = 'https://omgtu.ru/general_information/the-structure/the-department-of-university.php'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    department = []

    for link in soup.find_all('p'):
        text = link.get_text(strip=True)
        if text:
            department.append(text)

    with open('omgtu_departments.txt', 'w', encoding='utf-8') as file:
        for dept in department:
            file.write(dept + '\n')

    print(f'Сохранено {len(department)} кафедр в файл omgtu_departments.txt')


if __name__ == '__main__':
    get_departments()
