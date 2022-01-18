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
