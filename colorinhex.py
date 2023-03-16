import pandas as pd
from colormap import rgb2hex

# не робит
class ColorsInHex(object):
    @staticmethod
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