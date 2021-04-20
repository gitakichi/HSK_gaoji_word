import json

with open('japanese.txt',mode='r',encoding="utf-8") as f:
    lines = f.read().splitlines()
    word_list = []
    
    for line in lines:
        cell = line.split(",")
        work = {}
        work["id"] = cell[0]
        work["zh"] = cell[1]
        work["pinyin"] = cell[2]
        work["ja"] = cell[3] 

        word_list.append(work)

json_str = json.dumps(word_list, ensure_ascii=False)

with open('word.js',mode='w',encoding="utf-8") as f:
    f.write("var word={};\n".format(json_str))