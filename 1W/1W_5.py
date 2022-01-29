inputs = "cat32dog16cow5"

def find_string(inputs):
    new = ""
    for i in inputs:
        if not i.isdigit():
            new += i
        else:
            new += " "
    return list(new.split())


string_list = find_string(inputs)
print(string_list)