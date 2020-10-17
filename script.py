#!/usr/bin/env python3

import os

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def get_average_grade(path):
    if not os.path.exists(path):
        return None
    with open("my_grades.txt", "r") as file:

        data = file.readlines()
        grades = []
        average = 0.0
        for line in data:
            if ":" in line:
                l = line.split(":")
                grade = float(l[1])
                grades.append(grade)
        if not grades:
            return float("0.0")
        else:
            for grade in grades:
                average += grade

            average = average / len(grades)
            return average

def merge_list(a, b):
    new_l = []
    dif_len = len(a) - len(b)
    if len(a) == 0 or len(b) == 0:
        return []
    #a ist länger als b
    if dif_len > 0:
        for i in range(dif_len):
            b.append(b[-1])
    elif dif_len < 0:
        for i in range(-dif_len):
            a.append(a[-1])
    #for i in range(max(len(a), len(b))):
        #new_l.append((a[i],b[i]))
    new_l = list(zip(a,b))

    return new_l

def invert(d):
    inv_d = {}
    for key, value in d.items():
        if value in inv_d:
            inv_d[value].append(key)
            inv_d[value].sort()
        else:
            inv_d[value] = [key]

    return inv_d

def analyze(posts):

    tags = []
    tag_dic = {}
    for post in posts:
        l = post.split()
        for word in l:
            if "#" in word and word != "#":
                index_hash = word.find("#")
                print (index_hash)

                if word[index_hash+1].isalpha():
                    tag = ""
                    for char in word[index_hash+1:]:
                        if not char.isalpha() and not char.isdigit():
                            break
                        else:
                            tag = tag + char
                    tags.append(tag)
    for tag in tags:
        if tag in tag_dic:
            tag_dic[tag] += 1
        else:
            tag_dic[tag] = 1

    return tags

def analyze_2(posts):
    tags = {}

    for post in posts:

        tag = None

        for char in post:

            if tag != None and not (char.isalpha() or char.isdigit()):

                if len(tag) >= 1 and not tag[0].isdigit():

                    if tag in tags.keys():
                        tags[tag] += 1
                    else:
                        tags[tag] = 1

                tag = None

            if char == "#":

                tag = ""

                continue #Jumps back to the next iteration of the for-loop

            elif (char.isalpha() or char.isdigit()) and tag != None:

                tag += char

        if tag != None:
            if len(tag) >= 1 and not tag[0].isdigit():

                if tag in tags.keys():
                    tags[tag] += 1
                else:
                    tags[tag] = 1

    return tags

def compress(data):
    tpl = ((), [])
    l = []
    l_allvalues= []
    l_keys = []
    if not data:
        return tpl
    if data == [{}]:
        return ((), [()])
    for dic in data:

        if not l_keys:
            l_keys = tuple(sorted(dic.keys()))


        l_values = l.copy()
        for key in l_keys:
            value = dic[key]

            l_values.append(value)

        l_allvalues.append(tuple(l_values))

    print(l_allvalues)
    print(l_keys)
    l.append(l_keys)
    l.append(l_allvalues)
    return tuple(l)
















datasa = [{"a": 1, "b": 2, "c": 3},{"a": 4, "c": 6, "b": 5}]
data = [
            {"a": 1, "b": 2, "c": 3},
            {"a": 9, "c": 7, "b": 8}
        ]
print(compress(data))

datas = [{}]
#print(compress(datas))

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
#print(get_average_grade("my_grades.txt"))




