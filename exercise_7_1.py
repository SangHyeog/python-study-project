#연습문제 1
print("연습문제 1")

input_str = input("문자열 입력 : ")
l = len(input_str)
index = 0

while index < l:
    print("s[0", index+1, "]=", input_str[0:index+1])
    index=index+1
    
print("=" * 50)

#연습문제 2
print("연습문제 2")

input_str = input("문자열 입력 : ")
input_find = input("찾아 바꿀 문자 : ")
find_length = len(input_find)

index = input_str.find(input_find)

if index == -1:
    print("바꿀 문자가 없네요.")
else:
    beforeStr = input_str[0:index]
    changeStr = input_str[index:index+find_length].upper()
    afterStr = input_str[index+find_length:]
    result = beforeStr + changeStr + afterStr
    print(result)

print("=" * 50)

#연습문제 3
print("연습문제 3")

input_str = input("문자열 입력 : ")

swap_str = input_str.swapcase()
l = len(swap_str)

index = 0
upperCount = 0
lowerCount = 0
etcCount = 0

while index < l:
    if swap_str[index].islower():
        lowerCount += 1
    elif swap_str[index].isupper():
        upperCount += 1
    else:
        etcCount += 1
    index += 1

print("대문자 갯수는 : ", upperCount)
print("소문자 갯수는 : ", lowerCount)
print("대소문자가 아닌 갯수는 : ", etcCount)
print("=" * 50)
