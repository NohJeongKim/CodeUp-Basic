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
