import requests
from PIL import Image
from io import BytesIO

def get_cat_image(tag=None):
    base_url = "https://kartinki.pics/pics/uploads/posts/2022-08/1661424567_7-kartinkin-net-p-sad-izyashchnikh-slov-oboi-krasivo-10.jpg"
    if tag:
        url = f"{base_url}/{tag}" #https://cataas.com/cat/funny
    else:
        url = base_url #https://cataas.com/cat

    response = requests.get(url)
    if response.status_code == 200:
        image_data = response.content
        image = Image.open(BytesIO(image_data))
        image.show()
    else:
        print(f"Ошибка {response.status_code}. Не удалось получить фотку кота")


#get_cat_image("funny")
get_cat_image()