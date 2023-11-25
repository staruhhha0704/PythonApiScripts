#Доступные ссылки
#https://catfact.ninja/breeds
#https://catfact.ninja/fact
#https://catfact.ninja/facts

import requests

def requestBuilder(url):
    response = requests.get(url)

    # requests.post()
    # requests.put()
    # requests.delete()

    if response.status_code == 200:
        print("Преобразованные данные: ", response.json())
        data = response.json()
        print("Полученные данные")
        for key, value in data.items():
            print(f'Ключ - {key}, значение - {value}')
    else:
        print(f"Oshibka: {response.status_code} - {response.text}")


print("1-Хлеб")
print("2-Факт")
print("3-Факты")
try:
    inp = int(input("Daitr napisat"))
    if inp == 1:
        requestBuilder("https://catfact.ninja/breeds")
    elif inp == 2:
        requestBuilder("https://catfact.ninja/fact")
    elif inp == 3:
        requestBuilder("https://catfact.ninja/facts")
    else:
        print("Выбран неправилный путь")
except Exception:
    print(Exception.__name__)