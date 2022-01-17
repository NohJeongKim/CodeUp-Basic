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
