# 1251
for ii in range(1, 101):
    print(ii, end=' ')

# 1252
n=int(input())

for ii in range(1, n+1):
    print(ii, end=' ')
  
# 1253
a,b=map(int, input().split())
if a>b:
    for ii in range(b,a+1):
        print(ii, end=' ')
else:
    for ii in range(a, b+1):
        print(ii, end=' ')
        
# 1254
s1, s2=input().split()
s1=ord(s1)
s2=ord(s2)

for ii in range(s1, s2+1):
    print(chr(ii), end=' ')
    
#1255
a,b=map(float, input().split())

while a<=b:
    print(format(a,'.2f'))
    a+=0.01
    
# 1256
n=int(input())
print('*'*n, end='')

# 1257
a,b=map(int, input().split())

if a%2==0:
    for ii in range(a+1, b+1, 2):
        print(ii)
else:
    for ii in range(a, b+1, 2):
        print(ii)

# 1258
n=int(input())

count=0
for ii in range(1, n+1):
    count+=ii
    
print(count)

# 1259
n=int(input())

even_count=0
for ii in range(1, n+1):
    if ii%2==0:
        even_count+=ii
        
print(even_count)

# 1260
from sys import stdin
a,b=map(int, stdin.readline().split())

multiple_of_3=0
for ii in range(a, b+1):
    if ii%3==0:
        multiple_of_3+=ii
        
print(multiple_of_3)

# 1261
a,b,c,d,e,f,g,h,i,j=map(int, input().split())
_list=[a,b,c,d,e,f,g,h,i,j]

for ii in _list:
    if ii%5==0:
        print(ii)
        break   
else:
    print(0)

# 1265
n=int(input())
for ii in range(1,10):
    print(f'{n}*{ii}={n*ii}')

# 1266
n=int(input())
numbers=list(map(int, input().split()))

count=0
for ii in numbers:
    count+=ii
    
print(count)

# 1267
n=int(input())
numbers=list(map(int, input().split()))

count_5=0
for ii in numbers:
    if ii%5==0:
        count_5+=ii
        
print(count_5)

# 1268
n=int(input())
from sys import stdin
numbers=list(map(int, stdin.readline().split()))

count=0
for ii in numbers:
    if ii%2==0:
        count+=1
        
print(count)

# 1269
a,b,c,n=map(int, input().split())
for ii in range(1, n):
    a=a*b+c
    
print(a)

# 1270
n=int(input())

count=0
for ii in range(1, n+1):
    if ii%10==1:
        count+=1
        
print(count)

# 1271
n=int(input())
from sys import stdin
numbers=list(map(int, stdin.readline().split()))

num_max=numbers[0]
for ii in numbers:
    if num_max<ii:
        num_max=ii

print(num_max)

# 1272
A1.
k,h = map(int, input().split())
nums_list=[k,h]

money=0
for ii in nums_list:
    if ii%2!=0:
        money+=((ii//2)+1)
    else:
        money+=((ii//2)*10)
        
print(money)

A2.
nums_list = list(map(int, input().split()))

money=0
for ii in nums_list:
    if ii%2!=0:
        money+=((ii//2)+1)
    else:
        money+=((ii//2)*10)
        
print(money)

# 1273
A1.
n=int(input())

measure_list=[]
for ii in range(1, n+1):
    if n%ii==0:
        measure_list.append(ii)
        
for i in measure_list:
    print(i, end=' ')
    
A2.
n=int(input())
for ii in range(1, n+1):
    if n%ii==0:
        print(ii, end=' ')

# 1274
A1.
n = int(input())
now = 'prime'

for i in range(2, n):
    if n % i == 0:
        now = 'not prime'
        break

print(now)

A2.
n = int(input())
count = 1

for i in range(2, n+1):
    if n % i == 0:
        count += 1

if count > 2:
    print('not prime')
else:
    print('prime')

# 1275
n,k=map(int, input().split())
print(n**k)

# 1276
n=int(input())
factorial_count=1

for ii in range(1, n+1):
    factorial_count*=ii
    
print(factorial_count)
