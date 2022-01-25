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

# 1172
from sys import stdin
a,b,c=map(int, stdin.readline().split())
_list=[a,b,c]
_list=sorted(_list)
for ii in _list:
    print(ii, end=' ')

# 1173
from sys import stdin
hour, minute=map(int, stdin.readline().split())
if minute<30:
    if hour != 0:
        print(hour-1, 30+minute)
    else:
        print(23, 30+minute)
else:
    print(hour, minute-30)
    
# 1180
str=input()
if 1<=int(str)<=9:
    n=str+'0'
    if int(n)*2>100:
        if (int(n)*2)%100>50:
            print((int(n)*2)%100, 'OH MY GOD')
        else:
            print((int(n)*2)%100, 'GOOD')
    else:
        if int(n)*2>50:
            print(int(n)*2, 'OH MY GOD')
        else:
            print(int(n)*2, 'GOOD')
else:
    n=str[::-1]
    if int(n)*2>100:
        if (int(n)*2)%100>50:
            print((int(n)*2)%100, 'OH MY GOD')
        else:
            print((int(n)*2)%100, 'GOOD')
    else:
        if int(n)*2>50:
            print(int(n)*2, 'OH MY GOD')
        else:
            print(int(n)*2, 'GOOD')
            
# 1202
score=int(input())
if score>=90:
    print('A')
elif score>=80:
    print('B')
elif score>=70:
    print('C')
elif score>=60:
    print('D')
else:
    print('F')
    
# 1203
bmi=int(input())
if bmi>20:
    print('비만')
elif 10<bmi<=20:
    print('과체중')
else:
    print('정상')

# 1204
num=int(input())
if 11<=num<=19:
    print(num, 'th', sep='')
else:
    if (num%10)==1:
        print(num, 'st', sep='')
    elif (num%10)==2:
        print(num, 'nd', sep='')
    elif (num%10)==3:
        print(num, 'rd', sep='')
    else:
        print(num, 'th', sep='')

# 1205
a,b=map(float, input().split())
_list=[a+b, b+a, a-b, b-a, a*b, b*a, a/b, b/a, a**b, b**a]
_max=max(_list)
print(format(_max, '.6f'))

# 1206
a,b=map(int, input().split())
if a>b:
    if a%b==0:
        x=a//b
        print(f'{b}*{x}={a}')
    else:
        print('none')
else:
    if b%a==0:
        x=b//a
        print(f'{a}*{x}={b}')
    else:
        print('none')
        
# 1207
from sys import stdin
a,b,c,d=map(int, stdin.readline().split())
_list=[a,b,c,d]

count_1=0
for ii in _list:
    if ii == 1:
        count_1+=1
        
if count_1==0:
    print('모')
elif count_1==1:
    print('도')
elif count_1==2:
    print('개')
elif count_1==3:
    print('걸')
else:
    print('윷')
    
# 1210
a,b=map(int, input().split())
menu={1:400, 2:340, 3:170, 4:100, 5:70}
if menu[a]+menu[b]>500:
    print('angry')
else:
    print('no angry')

# 1212
from sys import stdin
a,b,c=map(int, stdin.readline().split())
_list=[a,b,c]
_list=sorted(_list)
if _list[0]+_list[1]>_list[-1]:
    print('yes')
else:
    print('no')
    
# 1214
from sys import stdin
year, month=map(int, stdin.readline().split())

if month==2:
    if (year%400==0) or ((year%4==0)&(year%100!=0)):
        print(29)
    else:
        print(28)
elif month in [1,3,5,7,8,10,12]:
    print(31)
else:
    print(30)

# 1216
not_adv, adv, cost=map(int, input().split())
do_adv=adv-cost
if do_adv>not_adv:
    print('advertise')
elif do_adv<not_adv:
    print('do not advertise')
else:
    print('does not matter')

# 1218
from sys import stdin
a,b,c=map(int, stdin.readline().split())
_list=[a,b,c]
_list=sorted(_list)

if _list[0]+_list[1]>_list[-1]:
    if _list[0]==_list[1]==_list[-1]:
        print('정삼각형')
    elif (_list[0]==_list[1])or(_list[1]==_list[-1]):
        print('이등변삼각형')
    elif _list[0]**2+_list[1]**2==_list[-1]**2:
        print('직각삼각형')
    else:
        print('삼각형')
else:
    print('삼각형아님')

# 1222
from sys import stdin
time, score1, score2=map(int, stdin.readline().split())

goal=0
while time<90:
    goal+=1
    time+=5
score1+=goal

if score1>score2:
    print('win')
elif score1<score2:
    print('lose')
else:
    print('same')
    
# 1224
from sys import stdin
a,b,c,d=map(int, stdin.readline().split())

if(a / b > c / d):
    print('>')
elif(a / b == c / d):
    print('=')
else:
    print('<')

# 1228
height, weight=map(float, input().split())
standard_weight=(height-100)*0.9
obesity=((weight-standard_weight)*100)/standard_weight

if obesity<=10:
    print('정상')
elif 10<obesity<=20:
    print('과체중')
else:
    print('비만')

# 1229
height, weight=map(float, input().split())

if height<150:
    standard_weight=height-100
elif 150<=height<160:
    standard_weight=(height-150)/2+50
else:
    standard_weight=(height-100)*0.9
    
obesity=((weight-standard_weight)*100)/standard_weight

if obesity<=10:
    print('정상')
elif 10<obesity<=20:
    print('과체중')
else:
    print('비만')

# 1230
from sys import stdin
a,b,c=map(int, stdin.readline().split())
tunnel=[a,b,c]
height=170

for ii in tunnel:
    if ii<=height:
        print('CRASH', ii)
        break
else:
    print('PASS')
