# 연습문제 2
print("연습문제 2")

count = 0
message = input("메시지를 입력하세요: ")

for ch in message:
    if ch == "a":
        count = count + 1
print("a 개수 : ", count)
print("=" * 50)

# 연습문제 3
print("연습문제 3")

print("구구단 중 몇단까지 출력할까요?")
num = int(input("숫자를 입력하세요: "))

for i in range(2, num+1):
    print(i, "단")
    for j in range(1, 10):
        print("  ", i, "*", j, "=", i*j)

print("=" * 50)


a=0
for i in range(10):
    a = a + 1
    for j in range(5):
        a = a + 2
print(a)
