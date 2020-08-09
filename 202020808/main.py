'''a = 1
b = 2
c = 3
d = 4
if a > b:
    print('a')
elif a == b:
    print('equal')
else:
    print('b')'''

'''current=int(input())
check=0

if current%4==0:
    if current%100==0:
        if current%400==0:
            check=1
    else:
        check=1

if check==1:
    print("윤년!")
else:
    prin("평년")'''

family = ['mother', 'father', 'me', 'sister']

for x in family:
    print('%s %d'%(x,len(x)))