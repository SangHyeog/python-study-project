fn = "??"
num = 0

while num > 5 or fn == "김" or fn == "최" or fn == "이":
    name = input("이름을 입력하세요: ")
    fn = name[0]
    num = num + 1
print("="*50)
