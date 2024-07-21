# braking of outer loop with inner value

i=1
while i<6:
    for j in range(1,6):
        print(i,j)
    if j == 5:
        break
    i+=1

#process:
'''
iteration 1:
    outer loop i = 1:
        inner loop j = 1:
            so print 1,1
        inner loop j = 2:
            so print 1,2
        inner loop j =3:
            so print 1,3
        inner loop j =4
            so print 1,4
        inner loop j =5
            so print 1,5
        check j == 5: true 
        so terminated the outer loop so program will get end
'''
