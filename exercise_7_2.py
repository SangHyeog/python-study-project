#연습문제 1
print("연습문제 1")

num = int(input("List element 개수 입력: "))
newList = []
tempList = [0]

for i in range(num):
    print(i,"번째")
    t = input("추가할 element 입력: ")
    tempList = [t]
    newList = newList + tempList
          
print(newList)
    
print("=" * 50)

#연습문제 2
print("연습문제 2")

gugudanList = [[0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0]]

for i in range(2, 17):
    for j in range(1, 10):
        gugudanList[i-2][j-1] = i*j
print(gugudanList)

print("=" * 50)

#method 활용하기 2
print("method 활용하기 2")

f1 = ["apple", "blueberry", "melon", "tomato"]
f2 = ["strawberry", "lemon", "banana"]
f3 = f1 + f2
print(f3)

#remove element with its first char "b"
index = len(f3)
i = 0

while i < index:
    if f3[i][0] == "b":
        f3.remove(f3[i])
        i = i - 1
        index = index - 1
    i = i + 1

print("remove all 'b' elements = ", f3)


print("=" * 50)
