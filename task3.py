import requests

def get_holidays(country_code):
    api_url = f"https://date.nager.at/api/v3/publicholidays/2023/{country_code}"

    try:
        response = requests.get(api_url)
        holidays_data = response.json()

        if response.status_code == 200:
            if holidays_data:
                print(f"Праздник в {country_code} в 2023 году.")
                for holiday in holidays_data:
                    print(f"{holiday['date']} - {holiday['name']}")
                    print(f"Локальое название {holiday['localName']}")
            else:
                print(f"Нет данных о праздниках в {country_code}")
        else:
            print(f"Ошибка {response.status_code}. Не удалось получить данные")
    except Exception as e:
        print(e)



get_holidays("ZW")


