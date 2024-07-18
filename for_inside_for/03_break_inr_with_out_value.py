# breaking inner loop with outer loop value

for i in range(1,6):
    for j in range(1,6):
        print(i,j)
        if i == 3:
            break

#process
'''
iteration 1:
    outer loop i = 1:
        inner loop j = 1:
            so print 1,1
            check i == 3:false
        inner loop j =2:
            so print 1,2
            check i == 3: false
        inner loop j =3:
            so print 1,3
            check i == 3: false
        inner loop j = 4:
            so print 1,4
            check i == 3: fasle
        inner loop j = 5:
            so print 1,5
            check i == 3: false
iteration 2:
    outer loop i = 2:
        inner loop will again run for 5 times :
            so print 2,1 2,2 2,3 2,4 2,5
            becuse in this iteration i == 3 will never true

iteration 3:
    outer loop i =3 :
        inner loop j = 1
            so print 3,1
            checkin i ==3 true
            so terminate this inner loop
iteration 4:
    outer loop i = 4:
        inner loop will again run for 5 times :
            so print 4,1 4,2 4,3 4,4 4,5
            becuse in this iteration i == 3 will never true
iteration 5:
    outer loop i = 5:
        inner loop will again run for 5 times :
            so print 5,1 5,2 5,3 5,4 5,5
            becuse in this iteration i == 3 will never true

'''