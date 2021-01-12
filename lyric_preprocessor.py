import os
import math
import re
import numpy as np
import sys
import pickle
import random
import pandas as pd

folder = './lyrics'
new_folder = './lyrics_processed'
notes = '[0-9’!１２３４５６７８９０"#$%&\'()（）*+,-/:;<=>?@，。?★、…【】●《》＊;「」？“”‘’！：[\\]^_`{|}~‧.,/;:\']+'

for song in os.listdir(folder):
    
    try:
        with open(os.path.join(folder, song), 'r') as file:
            file = file.read()
    #         print(file)
            file = re.sub("更多更詳盡歌詞 在 ※ Mojim.com　魔鏡歌詞網", "", file)
            file = re.sub(u"\\（.*?）|\\{.*?}|\\[.*?]|\\【.*?】|\\感謝.*?歌詞", "", file)
            file = re.sub(notes, '', file)
            with open(os.path.join(new_folder, song), 'w+') as newfile:
                newfile.write(file)
            
#             print(file)

            
    except:
        print(song, '壞掉了！！')
        
# print(cnt)