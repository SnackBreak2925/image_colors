import pandas as pd
import extcolors
from colormap import rgb2hex
from PIL import Image

def ColorsInHex(input):
    colors_pre_list = str(input).replace('([(', '').split(', (')[0:-1]
    df_rgb = [i.split('), ')[0] + ')' for i in colors_pre_list]
    df_percent = [i.split('), ')[1].replace(')', '') for i in colors_pre_list]

    # переводим в HEX
    df_color_up = [rgb2hex(int(i.split(", ")[0].replace("(", "")),int(i.split(", ")[1]),
                               int(i.split(", ")[2].replace(")", ""))) for i in df_rgb]
    # номер цвета, его хекс и сколько он занимает места
    df = pd.DataFrame(zip(df_color_up, df_percent), columns=['c_code', 'occurence'])
    return df


def main():
    # сайт, откуда брала https: // towardsdatascience.com / image - color - extraction -with-python - in -4 - steps - 8d9370d9216e
    # именно png, потому что jpg не поддерживает отсутствие цвета (белого короче нет)
    input_name = "dog1.png"
    output_width = 800  # если вдруг картинка слишком большая, обрезаем ее.
    # Вообще проверку тут запихнуть (вдруг картинка уже маленькая)
    img = Image.open(input_name)
    wpercent = (output_width / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((output_width, hsize), Image.Resampling.LANCZOS)
    # сохраняем обрезанную картинку
    resize_name = 'resize_' + input_name  # новое имя: resize+старое имя
    img.save(resize_name)  # сохраняем туда же

    # цвета из картинки извлекаем extcolors.extract_from_path(img_url, tolerance=12, limit=12)
    # tolerance- группировка по цветам(0-не группировать,100-слить все в 1 цвет), limit-сколько цветов забираем(можно убрать)
    img_url = resize_name
    colors_x = extcolors.extract_from_path(img_url, tolerance=12, limit=12)
    df_color = ColorsInHex(colors_x)
    print(df_color)


if __name__ == '__main__':
    main()

