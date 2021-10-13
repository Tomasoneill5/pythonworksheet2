#Q6
units= int(input('enter your number of units: '))
if units<=100:
    print('charge is: 0 cents')

elif units<=200:
    cost = (units-100)*0.05
    print('charge is: ', cost, 'cents')
   
else:
    cost2 = (units-200)*10 +(100 * 5)
    print('charge is: ', cost2, 'cents')