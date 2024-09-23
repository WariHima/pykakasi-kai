from pathlib import Path
import re
import argparse

del_kana = True

def clean_imedic(path_str:str,out_path_str:str):
    __KANA_PATTERN = re.compile(r"[ぁ-わをん]+")


    text = Path(path_str).read_text(encoding="shift_jis")

    split_text = text.split("\n")

    new_split_text = []
    for word in split_text:
        new_split_text.append(word.split("\t"))
    
    if del_kana:

        dellist = []

        for i in range(0, len(new_split_text)):

            if __KANA_PATTERN.fullmatch( new_split_text[i][0] ):
                dellist.append[i]

        for i in dellist:
            new_split_text.pop(i)

    for i in range(0, len(new_split_text)):
        new_split_text[i] = "　".join(new_split_text)

    new_text = "\n".join(new_split_text)



    Path(out_path_str).write_text(new_text, encoding="utf-8")


def clean_mozcdic(path_str:str,out_path_str:str):
    __KANJI_PATTERN = re.compile(r"[\u4E00-\u9FFF\u3400-\u4DBF\u3005]")
     

    text = Path(path_str).read_text(encoding="utf-8")

    split_text = text.split("\n")

    new_split_text = []
    for word in split_text:
        new_split_text.append(word.split("\t"))
    
    if del_kana:

        kanji_list = []

        for i in range(0, len(new_split_text)):
            if len(new_split_text[i]) == 5:    
                if __KANJI_PATTERN.match( new_split_text[i][4] ):
                    kanji_list.append(new_split_text[i])

                    
        new_split_text = kanji_list

    new_text = []
    for i in range(0, len(new_split_text)):
        if len(new_split_text[i]) == 5:    
            word = str(new_split_text[i][0]) +" "+ str(new_split_text[i][4])
            new_text.append(word)

    new_text = "\n".join(new_text)

    Path(out_path_str).write_text(new_text, encoding="utf-8")

def clean_mzime(path_str:str,out_path_str:str):
    __KANJI_PATTERN = re.compile(r"[\u4E00-\u9FFF\u3400-\u4DBF\u3005]")
     

    text = Path(path_str).read_text(encoding="utf-8")

    split_text = text.split("\n")
    #print(split_text)

    new_split_text = []
    for word in split_text:
        if word != "":
            if word[0] != ";":
                new_split_text.append(word.split("\t"))
    
    if del_kana:

        kanji_list = []

        for i in range(0, len(new_split_text)):   
            if len(new_split_text[i]) >= 3:
                if __KANJI_PATTERN.match( new_split_text[i][2] ):
                    kanji_list.append(new_split_text[i])
                    
        new_split_text = kanji_list

    new_text = []
    for i in range(0, len(new_split_text)):
        if len(new_split_text[i]) >= 3:    
            word = str(new_split_text[i][0]) +" "+ str(new_split_text[i][2])
            new_text.append(word)

    new_text = "\n".join(new_text)

    Path(out_path_str).write_text(new_text, encoding="utf-8")

def main(args):
    assert args.mode != "ime" or "mozc" or "mzime" , "mode is not 'mozc' or 'ime' ,mzime'"
    if args.mode == "ime":
        clean_imedic(args.input_file,args.output_file)
    elif args.mode == "mozc":
        clean_mozcdic(args.input_file,args.output_file)
    elif args.mode == "mzime":
        clean_mzime(args.input_file,args.output_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_file", type=str, required=True)
    parser.add_argument("--output_file", type=str, required=True)
    parser.add_argument("--mode", type=str, required=True)

    args = parser.parse_args()
    main(args)
