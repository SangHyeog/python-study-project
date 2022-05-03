#연습문제 1
print("연습문제1")

str = input("문장을 입력: ")
split_list = str.split()

del_word = input("제거할 단어를 입력: ")
split_list.remove(del_word)

add_word = input("추가할 단어를 입력:")
split_list.insert(2, add_word)

delimiter = ' '
str = delimiter.join(split_list)
print(str)

print("=" * 50)

#연습문제 3
print("연습문제3")

list01 = ["apple", "banana", "quiz", "hi", "bye"]
list02 = ["Korea", "hi", "LOL", "Python", "apple"]

for i in range(len(list01)):
    if list01[i] in list02:
        list02.remove(list01[i])

list03 = list01 + list02
print("List01 : ", list01)
print("List02 : ", list02)
print("List03 : ", list03)

list03.sort()
print("정렬 후:", list03)

print("=" * 50)

#연습문제 4
print("연습문제4")
from copy import*

numList = [1,3,5,7,9]
numShallow = numList
numDeep = deepcopy(numList)

print("numList = ", numList)
print("numShallow = ", numShallow)
print("numDeep = ", numDeep)

numShallow.append(99)
numDeep.append(111)

print("after appending", "="*20)
print("numList = ", numList)
print("numShallow = ", numShallow)
print("numDeep = ", numDeep)

print("=" * 50)
