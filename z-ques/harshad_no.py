# no is harshad no or not
'''
n = int(input())
summ = 0
dummy = n
while dummy>0:
    rem = dummy%10
    dummy//=10
    summ += rem
if n%summ == 0:
    print('harsad no')
else:
    print('not a harsad no')


# print harshad no in given range

ll = int(input())
ul = int(input())

for n in range(ll,ul+1):
    dummy = n
    summ = 0
    while dummy>0:
        rem = dummy%10
        dummy//=10
        summ+= rem
    if n%summ == 0:
        print(n)

# print first n harshad no

n = int(input())
c = 0
i = 1
while True:
    dummy = i
    summ = 0
    while dummy>0:
        rem = dummy%10
        dummy//=10
        summ +=rem
    if i%summ==0:
        print(i)
        c+=1
        if c == n:
            break
    i+=1

'''
# porint the nth harsad no 

n = int(input())
c = 0
i = 1
while True:
    dummy = i
    summ = 0
    while dummy>0:
        rem = dummy%10
        dummy//=10
        summ +=rem
    if i%summ==0:
        c+=1
        if c == n:
            print(i)
            break
    i+=1


# print 5th to 10th harsad no 

c = 0
n = 1
while True:
    dummy = n
    summ = 0
    while dummy>0:
        rem = dummy%10
        dummy//=10
        summ+=rem
    if n%summ ==0:
        c+=1
        if c>=5 and c<=10:
            print(n)
        if c == 10:
            break
    n+=1