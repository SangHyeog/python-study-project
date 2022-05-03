## 연습문제 4
print("연습문제 4")

countnum = 0
count = 1
sum = 0

while countnum <= 0:
    countnum = int(input("양(+)의 정수를 몇개 입력 받을까요?"))

while count <= countnum:
    num = float(input("숫자를 입력하세요: "))
    count = count+1
    sum = sum + num
print("입력받은 수의 평균은 = ", sum/countnum)
print("="*50)

## 연습문제 5
print("연습문제 5")

fn = "??"
num = 0

while num < 5 and fn != "김" and fn != "최" and fn != "이":
    name = input("이름을 입력하세요: ")
    fn = name[0]
    num = num + 1
    
print("="*50)


print("="*50)


