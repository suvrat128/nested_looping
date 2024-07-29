# check wheather given no is spacial no or not
'''
A number is considered a special number if the sum of the factorial of the digits in the number is equal to the number itself.
'''

n = int(input())
dummy = n
summ = 0
while dummy>0:
    rem = dummy%10
    dummy//=10
    fact = 1
    for i in range(1,rem+1):
        fact*=i
    summ+=fact
if summ == n:
    print('special no')
else:
    print('not special no')


# pint all special number in given rang

ll = int(input())
ul = int(input())

for n in range(ll,ul+1):
    dummy = n
    summ = 0
    while dummy>0:
        rem = dummy%10
        dummy//=10
        fact = 1
        for i in range(1,rem+1):
            fact*=i
        summ+=fact
    if summ == n:
        print(n)


# first n special no 

n = int(input())
ct = 0
i =1
while True:
    dummy = i
    summ = 0
    while dummy>0:
        rem = dummy%10
        dummy//=10
        fact = 1
        for j in range(1,rem+1):
            fact*=j
        summ+=fact
    if summ == i:
        print(i)
        ct+=1
        if ct == n:
            break
    i+=1



    

# print nth special no

n = int(input())
ct = 0
i =1
while True:
    dummy = i
    summ = 0
    while dummy>0:
        rem = dummy%10
        dummy//=10
        fact = 1
        for j in range(1,rem+1):
            fact*=j
        summ+=fact
    if summ == i:
        ct+=1
        if ct == n:
            print(i)
            break
    i+=1



