# 1111
n=int(input())
print(f'{n}%') # python format

# 1116: 사칙연산 계산기 만들기
a,b=input().split()
a=int(a)
b=int(b)
print(f'{a}+{b}={a+b}')
print(f'{a}-{b}={a-b}')
print(f'{a}*{b}={a*b}')
print(f'{a}/{b}={a//b}') # 몫을 가져오는 것이기 때문에, //를 이용한다

# 1117
a,b=input().split()
a=float(a)
b=float(b)
print(format(a*b,'.2f'))

# 1118: 삼각형 넓이 구하기
a,b=input().split()
a=int(a)
b=int(b)
print(format((a*b)/2, '.1f'))

# 1122: 초를 분과 초로 변환하기
second=int(input())
m=second//60
s=second%60
print(m, s)

# 1123: 섭씨 온도에서 화씨 온도로 변환하기
celsius_temp=int(input())
fahrenheit_temp=9/5*celsius_temp+32
print(format(fahrenheit_temp, '.3f'))

# 1125: 10진수에서 8진수와 16진수로 변환하기
n=int(input())
print(format(n,'o'), format(n,'X'))

# 1135: 조건에 맞는 숫자 출력하기
A1.
a,b=map(int, input().split())
def compare(a,b):
    if a>=b:
        return 1
    else:
        return 0
        
print(compare(a,b))

A2.
a,b=map(int, input().split())
if a>=b:
    print(1)
else:
    print(0)

# 1138: 0,1을 반대로 출력하기
A1.
n=int(input())
print(int(not n))

A2.
n=int(input())
def compare(n):
    if n==0:
        return 1
    else:
        return 0
        
print(compare(n))

# 1139
a,b=map(int, input().split())
def compare(a,b):
    if a==1 and b==1:
        return 1
    else:
        return 0
    
print(compare(a,b))

# 1140
a,b=map(int, input().split())
def compare(a,b):
    if a==0 and b==0:
        return 0
    else:
        return 1
    
print(compare(a,b))
