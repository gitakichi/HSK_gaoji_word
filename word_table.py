import json #必ず必要
from pypinyin import pinyin, lazy_pinyin, Style


with open('word.txt',mode='r',encoding="utf-8") as f:
    lines = f.read().splitlines()
    #print(lines[0:10])

    lines_len = len(lines)
    pinyin_lines = [0] * lines_len
    to_write = ""

    i = 0
    while i<lines_len:
    #while i<lines_len[0:10]:
        result = pinyin(lines[i])
        result2 = ""
        for cur in result:
            result2 = result2 + cur[0]
        #print(result2)
        #pinyin_lines[i] = result2
        to_write = to_write + "{0},{1},{2}\n".format(i+1,lines[i],result2)
        i = i + 1


with open('pinyin.txt',mode='w',encoding="utf-8") as f:
    #f.write('\n'.join(pinyin_lines))
    f.write(to_write)
