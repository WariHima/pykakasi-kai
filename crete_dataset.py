import pykakasi
import mojimoji
import re

import alkana
from alkana.data import data as ALPHA_DICT 

def add_yomi(text):
 
    #アルファベットと数字を半角に正規化
    text = mojimoji.zen_to_han(text, kana=False)

    kks = pykakasi.kakasi()
    result = kks.convert(text)

    split_text = []
    split_kata = []

    for item in result:
        split_text.append( item["orig"] )
        split_kata.append( item["kana"] )
    # 漢字
    KANJI = r"\u4E00-\u9FFF\u3400-\u4DBF\u3005"

    EIJI_PATTERN = re.compile(r"[A-Za-z]+")
    KANJI_PATTERN = re.compile(r"["+KANJI+r"]")

    ALPHA_DATA = ALPHA_DICT.keys()

    for i in range(0, len(split_text)):
        word = split_text[i]
        # 漢字が入っている場合
        if KANJI_PATTERN.match(word):
            kana = split_kata[i]
            split_text[i] = "{" + word + "/" + kana + "}"

        # 2文字以上の英字(英単語の場合)
        elif len(word) >= 2 and EIJI_PATTERN.fullmatch(word):

            if word in ALPHA_DATA:

                split_text[i] = "{" + word + "/" + alkana.get_kana(word)  + "}"
                #print(split_text[i])

    return "".join(split_text)