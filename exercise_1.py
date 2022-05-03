### 평균 계산하기
print("연습하기1")
kor = float(input("당신의 국어 성적은? "))
eng = float(input("당신의 영어 성적은? "))
math = float(input("당신의 수학 성적은? "))

avg = (kor + eng + math) / 3
print("3개 과목의 평균은 ", avg, "입니다.")
print("*" * 50)

### 이름 나누어서 반복 출력
print("연습하기2")
name = input("이름 3글자를 입력하세요; ")

print(name[0] * 5)
print(name[1] * 5)
print(name[2] * 5)
print("*" * 50)

### 이름, 소속기관, 나이 출력하기
print("연습하기3")
name = input("당신의 이름을 입력하세요; ")

belong = input("당신의 소속기관을 입력하세요; ")

birthyear = int(input("당신의 출생연도를 입력하세요; "))

print("당신의 이름은 ", name)
print(belong, "에 소속되어 있으시군요.")
print("당신의 나이는 ", 2022-birthyear, "세, 맞죠?")
