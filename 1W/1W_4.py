from collections import Counter

dict_first = {'사과': 30, '배': 15, '감': 10, '포도': 10}
dict_second = {'사과': 5, '감': 25, '배': 15, '귤': 25}

def merge_dic(dict_first, dict_second):
    a = Counter(dict_first)
    b = Counter(dict_second)
    print(str((a + b).items())[12:])


merge_dic(dict_first, dict_second)