import requests
from bs4 import BeautifulSoup

url = "https://omgtu.ru/general_information/the-structure/the-department-of-university.php"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")

    departments = soup.find_all("a")[1:]
    departments_list = [department.text for department in departments]

    with open("omgtu_departments.txt", "w", encoding="utf-8") as file:
        for department in departments_list:
            file.write(department + "\n")

    print(f"Список кафедр успешно записан в файл omgtu_departments.txt")
else:
    print("Ошибка при запросе к странице")
