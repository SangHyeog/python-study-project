#연습문제1
print("연습문제1")
import random

def random_picker(lists, number):
    for i in range(number):
        print(random.choice(lists))

num_list = [3,1,7,11,25,5,4,9]

random_picker(num_list, 3)

print("=" * 50)

#연습문제2
print("연습문제2")
import random

def gen_random(a, b):
    r = random.randrange(a,b)
    c = chr(65 + r)
    print(r, c)

for i in range(10):
    gen_random(i+1, i+10)

print("=" * 50)
