# print armstrong no of given range

el = int(input())
ul = int(input())
for i in range(el,ul+1):

    summ =0
    count = len(str(i))
    dummy = i
    while dummy>0:
        rem=dummy%10
        summ+=rem**count
        dummy//=10
        if summ == i:
            print(i)

# print first n armstrong number:

ct=int(input())
c =0
n = 1
while True:
    summ = 0
    count = len(str(n))
    dummy = n
    while dummy>0:
        rem=dummy%10
        dummy//=10
        summ+=rem**count
        
    if summ == n:
        print(n)
        c+=1
        if ct == c:
            break
    n+=1
    
# print nth  armstrong number:

ct=int(input())
c =0
n = 1
while True:
    summ = 0
    count = len(str(n))
    dummy = n
    while dummy>0:
        rem=dummy%10
        dummy//=10
        summ+=rem**count
        
    if summ == n:
        c+=1
        if ct == c:
            print(n)
            break
    n+=1

# print 5th to 10th aramstrong no

c =0
n = 1
while True:
    summ = 0
    count = len(str(n))
    dummy = n
    while dummy>0:
        rem=dummy%10
        dummy//=10
        summ+=rem**count
        
    if summ == n:
        c+=1
        if c>=5 and c<=10:
            print(n)
        if c == 10:
            break
    n+=1