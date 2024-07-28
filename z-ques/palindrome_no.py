# given no is paliandrome or not

n = int(input())
dummy = n
rev = 0

while dummy>0:
    rem = dummy%10
    dummy//=10
    rev = rev*10+rem
if rev == n:
    print('no is palindrome')
else:
    print(' not palindrome')


# print all palindrome no in given range

ll = int(input())
ul = int(input())

for n in range(ll,ul+1):
    dummy = n
    rev = 0
    while dummy>0:
        rem = dummy%10
        dummy//=10
        rev = rev*10+rem
    if rev == n:
        print(n)

# print first n palindrome no 

n = int(input())

ct = 0
i = 1
while True:
    dummy = i
    rev = 0
    while dummy>0:
        rem = dummy%10
        dummy//=10
        rev = rev*10+rem
    if rev == i:
        print(i)
        ct+=1
        if ct == n:
            break
    i+=1


# print first nth palindrome no 

n = int(input())
i = 1
ct = 0
while True:
    dummy = i
    rev = 0
    while dummy>0:
        rem = dummy%10
        dummy//=10
        rev = rev*10+rem
    if rev == i:
        ct+=1
        if ct == n:
            print(i)
            break
    i+=1