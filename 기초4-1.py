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
