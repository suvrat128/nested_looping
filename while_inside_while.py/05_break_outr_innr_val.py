#break outer loop with inner loop value

i=1
while i<6:
    j=1
    while j<6:
        print(i,j)
        j+=1
    if j==6:
        break
    i+=1

#process:
'''
iteration 1:
    outer loop i = 1:
        inner loop j = 1:
            so print 1,1
            increment j from 1 to 2
        inner loop j = 2:
            so print 1,2
            increment j from 2 to 3
        inner loop j =3:
            so print 1,3
            increment j from 3 to 4
        inner loop j =4
            so print 1,4
            increment j from 4 to 5
        inner loop j =5
            so print 1,5
            increment j from 5 to 6
        check j == 6: true 
        so terminated the outer loop so program will get end
'''