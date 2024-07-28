# the ginven no is disarium no or not

n = int(input())
dummy = n
summ = 0
c = len(str(n))
while dummy>0:
    rem = dummy%10
    dummy//=10
    summ += (rem**c)
    c-=1
if summ ==n:
    print('no is disarium no ')
else:
    print('not disarium no')

# print all disarium no in the given range

ll = int(input())
ul = int(input())

for n in range(ll,ul+1):
    dummy = n
    summ = 0
    c = len(str(n))
    while dummy>0:
        rem = dummy%10
        dummy//=10
        summ+= (rem**c)
        c-=1
    if summ == n:
        print(n)



# print first n disarium no 

n = int(input())
cout = 0
i = 1
while True:
    dummy = i
    summ = 0
    c = len(str(i))
    while dummy>0:
        rem = dummy%10
        dummy//=10
        summ+= (rem**c)
        c-=1
    if summ ==i:
        print(i)
        cout+=1
        if cout == n:
            break
    i+=1


# print nth disarium no 

n = int(input())

ct = 0
i = 1
while True:
    dummy = i
    c = len(str(i))
    summ = 0
    while dummy>0:
        rem = dummy%10
        dummy//=10
        summ+= (rem**c)
        c-=1
    if summ == i:
        ct+=1
        if ct == n:
            print(i)
            break
    i+=1
