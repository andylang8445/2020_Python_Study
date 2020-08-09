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

'''family = ['mother', 'father', 'me', 'sister']

for x in family:
    print('%s %d'%(x,len(x)))'''

'''a=[1,2,3,5,6,7,10]

for i in a:
    print(i)'''

'''for i in range(1,10):
    print(i)'''

'''def print_list(a):
    for i in a:
        print(i)

list_a=[1,1,2,3,5,8,13,21]
print_list(list_a)'''

'''def intComp(x, y):
    if x > y:
        print("%d > %d" % (x, y))
    elif x == y:
        print("%d == %d" % (x, y))
    else:
        print("%d < %d" % (x, y))


a = int(input("num1: "))
b = int(input("num2: "))
intComp(a, b)'''


def gugu(n):
    for m in range(1, 10):
        print("%d * %d = %d" % (n, m, n * m))


for i in range(2, 10):
    gugu(i)
    print()
