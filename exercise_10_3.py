#연습문제 1
print("연습문제 1")
def mult3(n):
    if n == 1:
        return 3
    else:
        for i in range(1, n):
            return 3*n

for i in range(1, 10):
    print(mult3(i))

print("=" * 50)

#연습문제 2
print("연습문제 2")
def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

for i in range(1, 15):
    print(fibo(i))

print("=" * 50)
