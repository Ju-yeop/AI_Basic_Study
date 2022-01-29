sentence = "way a is there will a is there Where"

def reverse_sentence(sentence):
    new_st = ""
    ls = sentence.split()
    for i in range(len(ls)-1, -1, -1):
        new_st += ls[i] + " "
    return new_st


print(reverse_sentence(sentence))