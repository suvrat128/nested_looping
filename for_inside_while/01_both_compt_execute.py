# for inside while loop

i=1
while i<6:
    for j in range(1, 6):
        print(i,j)
    i+=1


'''

iteration 1:
    outer loop i will 1:
        inner loop j will 1:
           so  print 1,1
        now i increment form 1 to 2
        inner loop j = 2:
           so print 1,2
        i increment form 2 to 3
        inere loop j =3:
            so pritn 1,3
        i increment form 3 to 4
        inner loop j =4
            so print 1,4
        i increment form 4 to 5
        inner loop j = 5
            so print 1,5
        i increment form 5 to 6
iteration 2:
    outer loop i = 2:
        inner loop will again run for 5 time :
            so print 2,1 2,2 2,3 2,4 2,5
iteration 3:
    outer loop i =3:
        inner loop will again run for 5 times:
            so print 3,1 3,2 3,3 3,4 3,5
iteration 4:
    outer loop i =4:
        inner loop will again run for 5 times:
            so print 4,1 4,2 4,3 4,4 4,5
iteration 5:
    outer loop i =5:
        inner loop will again run for 5 times:
            so print 5,1 5,2 5,3 5,4 5,5
'''