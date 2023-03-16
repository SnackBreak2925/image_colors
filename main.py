import pandas as pd
import extcolors
from colormap import rgb2hex
from PIL import Image
from handler import Handler


def main():
    # сколько цветов найти на картинке. Можно дать пользователю выбирать от 1 до 15
    KolColor=11

    # сайт, откуда брала https: // towardsdatascience.com / image - color - extraction -with-python - in -4 - steps - 8d9370d9216e
    # именно png, потому что jpg не поддерживает отсутствие цвета (белого короче нет)
    input_name = "dog1.png"
    img = Image.open(input_name)
    img,resize_name = Handler.Handler(img,input_name)
    img.save(resize_name)  # сохраняем туда же

    # цвета из картинки извлекаем extcolors.extract_from_path(img_url, tolerance=12, limit=12)
    # tolerance- группировка по цветам(0-не группировать,100-слить все в 1 цвет), limit-сколько цветов забираем(можно убрать)
    img_url = resize_name
    colors_x = extcolors.extract_from_path(img_url, tolerance=10,limit=KolColor)
    df_color = Handler.ColorsInHex(colors_x)
    print(df_color)

if __name__ == '__main__':
    main()

