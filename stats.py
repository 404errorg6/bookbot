def word_count(string):
    w_list = string.split()
    length = len(w_list)
    return length

def char_count(string):
    dic = {}
    for char in string.lower():
        if char in dic:
            dic[char] += 1
        else:
            dic[char] = 1
    return dic
def sort(dic):
    list = []
    for char, count in dic.items():
        list.append({"char" : char , "count" : count})
    list.sort(key=lambda x: x["count"], reverse=True)
    return list
