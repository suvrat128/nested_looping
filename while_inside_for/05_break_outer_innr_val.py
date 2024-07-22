# breaking of outer loop with innner value

for i in range(1,6):
    j=1
    while i<6:
        print(i,j)
        j+=1
    if j==6:
        break


#process:
'''
iteration 1:
    outer loop i = 1:
        inner loop j = 1:
            so print 1,1
            increment j 1 to 2
        inner loop j = 2:
            so print 1,2
            increment j 2 to 3
        inner loop j =3:
            so print 1,3
            increment j 3 to 4
        inner loop j =4
            so print 1,4
            increment j 4 to 5
        inner loop j =5
            so print 1,5
            increment j 5 to 6
        check j == 6: true 
        so terminated the outer loop so program will get end
'''