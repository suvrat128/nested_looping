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

