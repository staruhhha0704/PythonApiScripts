import requests

def get_dota_data(endpoint):
    base_url = "https://api.opendota.com/api/"
    api_url = f"{base_url}{endpoint}"

    try:
        response = requests.get(api_url)
        data = response.json()
        if response.status_code == 200:
            return data
        else:
            print("Ошибка")
            return None

    except Exception as e:
        print(e)
        return None


user_data = get_dota_data("players/46612097")
if user_data:
    print("Профиль пользователя")
    profile = user_data['profile']
    rank = user_data['leaderboard_rank']
    print(f"Игрок {profile['personaname']} - ранг {rank}")

match_data = get_dota_data("matches/74170846")
if match_data:
    print("KDA всех игроков в матче")
    for player in match_data['players']:
        assists = player['assists']
        deaths = player['deaths']
        kills = player['kills']
        if deaths == 0:
            KDA = kills + assists / 1
        else:
            KDA = kills + assists / deaths
        print(f'KDA игрока - {KDA}')