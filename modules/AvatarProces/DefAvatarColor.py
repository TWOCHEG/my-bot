import os
from random import sample
from PIL import Image
import requests
from FluffBot import config


def randName(gif=False) -> str:
    numbers = "1234567890"
    abc = "qwertyuiopasdfghjklzxcvbnm"
    title_abc = "QWERTYUIOPASDFGHJKLZXCVBNM"
    combinations = numbers + abc + title_abc
    if gif:
        ras = '.gif'
    else:
        ras = '.png'
    return config.AvatarTemp + "".join(sample(combinations, 15)) + ras  # сохранение файла аватара участника для вывода цвета


def process_avatar(member):  # тут начинается вывод цвета
    file_in = randName(False)
    avatar = member.display_avatar
    response = requests.get(avatar)

    with open(file_in, "wb") as file:
        file.write(response.content)

    img = Image.open(file_in)
    obj_for_count = img.load()

    f = open(file_in, "rb")
    img_for_size = Image.open(f)

    sq = [0, 0, 0]
    count = img_for_size.size[0] * img_for_size.size[1]

    width = img_for_size.size[0]
    height = img_for_size.size[1]

    for i in range(width):
        for j in range(height):
            sq[0] += obj_for_count[i, j][0]
            sq[1] += obj_for_count[i, j][1]
            sq[2] += obj_for_count[i, j][2]

    out = [0, 0, 0]

    out[0] = int(sq[0] / count)
    out[1] = int(sq[1] / count)
    out[2] = int(sq[2] / count)

    hexed = '0x' + format(out[0], 'x') + format(out[1], 'x') + format(out[2], 'x')  # тут заканчивается вывод цвета

    color = int(hexed, 0)  # вывод цвета в hex для дискорда

    f.close()

    os.remove(file_in)  # удаление файла чтоб не мешался

    return color

