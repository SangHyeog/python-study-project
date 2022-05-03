from datetime import date

def cal_birthday(month, day):
    today = date.today()
    birthday = date(today.year, month, day)
    due = birthday - today
    if due.days < 0:
        next_birthday = date(today.year + 1, birthday.month, birthday.day)
        due = next_birthday - today

print("생일까지 남은 날짜는 : ", due.days)

import math
import cmath

def deter(a, b, c):
    return math.pow(b, 2) - 4*a*c

def roots_formula(a, b, c):
    if deter(a, b, c) >= 0:
        root01 = (-b + math.sqrt(deter(a,b,c)))/(2*a)
        root02 = (-b - math.sqrt(deter(a,b,c)))/(2*a)
    else:
        root01_real = -b/(2*a)
        root01_imag = (math.sqrt(math.fabs(deter(a,b,c))))/(2*a)
        root02_real = -b/(2*a)
        root02_imag = (math.sqrt(math.fabs(deter(a,b,c))))/(2*a)
        root01 = root01_real + root01_imag * 1j
        root02 = root02_real - root02_imag * 1j

    return [root01, root02]
