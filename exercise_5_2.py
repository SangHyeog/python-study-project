## 연습문제 3
## 1
## "*" 순차적으로 점점 많이 출력
print("연습문제 3 #1")
i = 0
for i in range(1, 11):
    print("*" * i)

print("=" * 50)

## 2
## "*" 순차적으로 점점 적게 출력
print("연습문제 3 #2")
i = 0
for i in range(10, 0, -1):
    print("*" * i)

print("=" * 50)

## 연습문제 4
print("연습문제 4")
count = 0
name = input("영문 이름을 입력하세요: ")
for ch in name:
    if ch != " ":
        count = count + 1
    print(ch)

print("글자 수 : ", count)
print("=" * 50)
