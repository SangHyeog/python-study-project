# prime number 여부 확인

num = int(input("input a positive integer: "))

prime_yes = True

for i in range(2, num):
    if num % i == 0:
        prime_yes = False
        break

if prime_yes == True:
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")
