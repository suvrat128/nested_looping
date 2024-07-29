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




