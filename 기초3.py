# 1151
n=int(input())
if n<10:
    print('small')
else:
    print('')

n=int(input())
if n<10:
    print('small')
# else를 사용하지 않고, 조건이 1개이므로 if에서 끝내버릴 수도 있다

# 1153
a,b=map(int, input().split())
if a>b:
    print('>')
elif a<b:
    print('<')
elif a==b:
    print('=')

# 1154
a,b=map(int, input().split())
if a>=b:
    print(a-b)
else:
    print(b-a)
    
# 1158
n=int(input())
if (30<=n<=40) or (60<=n<=70):
    print('win')
else:
    print('lose')

# 1159
n=int(input())
if (50<=n<=70) or (n%6==0):
    print('win')
else:
    print('lose')
    
# 1160
n=int(input())
if n%2!=0: # 1,3,5,7을 
    print('oh my god')
else:
    print('enjoy')

# 1161
a,b=map(int, input().split())
if a%2==0:
    if b%2==0:
        print('짝수+짝수=짝수')
    else:
        print('짝수+홀수=홀수')
else:
    if b%2==0:
        print('홀수+짝수=홀수')
    else:
        print('홀수+홀수=짝수')

# 1162
y,m,d=map(int, input().split())
standard=(y-m+d)
if standard%10==0:
    print('대박')
else:
    print('그럭저럭')

# 1163
from sys import stdin
y,m,d=map(int, stdin.readline().split())
standard=((y+m+d)%1000)//100
if standard%2==0:
    print('대박')
else:
    print('그럭저럭')

# 1164
from sys import stdin
a,b,c=map(int, stdin.readline().split())
if (a>170)&(b>170)&(c>170):
    print('PASS')
else:
    print('CRASH')
    
# 1165
from sys import stdin
time, score=map(int, stdin.readline().split())

count=0
while time<90:
    time+=5
    count+=1
    
print(count+score)

# 1166
year=int(input())
if (((year%4==0)&(year%100!=0))|(year%400==0)):
    print("yes")
else:
    print("no")

# 1167
A1.
from sys import stdin
a,b,c=map(int, stdin.readline().split())
list1=[a,b,c]
list1=sorted(list1)
print(list1[1])

# 1168
ymd, s=input().split()
s=int(s)
if (s==1) or (s==2):
    year='19'+ymd[:2]
else:
    year='20'+ymd[:2]
print(2012-int(year)+1)

# 1169
age=int(input())
year=2013-age
year=str(year)
if year[:2]=='19':
    if year[-2]=='0': # 만약에 출생년도가 2000인 경우
        print(year[-1], 1) # 0 1을 출력하기
    else:
        print(year[2:], 1)
else:
    if year[-2]=='0':
        print(year[-1], 3)
    else:
        print(year[2:], 3)

# 1170
grade, _class, num=input().split()
if int(num)<10:
    print(grade,_class,'0'+num, sep='')
else:
    print(grade, _class, num, sep='')

# 1171
A1.
grade, _class, num=input().split()
if 1<=int(_class)<=9:
    if 1<=int(num)<=9:
        print(grade, '0'+_class, '00'+num, sep='')
    elif 10<=int(num)<=99:
        print(grade, '0'+_class, '0'+num, sep='')
    else:
        print(grade, '0'+_class, num, sep='')
else:
    if 1<=int(num)<=9:
        print(grade, _class, '00'+num, sep='')
    elif 10<=int(num)<=99:
        print(grade, _class, '0'+num, sep='')
    else:
        print(grade, _class, num, sep='')

A2.
from sys import stdin
grade, _class, num= map(str, stdin.readline().split())
if 1<=int(_class)<=9:
    if 1<=int(num)<=9:
        print(grade, '0'+_class, '00'+num, sep='')
    elif 10<=int(num)<=99:
        print(grade, '0'+_class, '0'+num, sep='')
    else:
        print(grade, '0'+_class, num, sep='')
else:
    if 1<=int(num)<=9:
        print(grade, _class, '00'+num, sep='')
    elif 10<=int(num)<=99:
        print(grade, _class, '0'+num, sep='')
    else:
        print(grade, _class, num, sep='')

A3.
from sys import stdin
grade, _class, num= stdin.readline().split()
if 1<=int(_class)<=9:
    if 1<=int(num)<=9:
        print(grade, '0'+_class, '00'+num, sep='')
    elif 10<=int(num)<=99:
        print(grade, '0'+_class, '0'+num, sep='')
    else:
        print(grade, '0'+_class, num, sep='')
else:
    if 1<=int(num)<=9:
        print(grade, _class, '00'+num, sep='')
    elif 10<=int(num)<=99:
        print(grade, _class, '0'+num, sep='')
    else:
        print(grade, _class, num, sep='')

