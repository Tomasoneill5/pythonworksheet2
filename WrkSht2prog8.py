#Q8
numberOne=int(input('enter any number: '))
lastDigit=numberOne%10
print('Last digit is', lastDigit)
if lastDigit==0:
    print('This number is not divisible by 3')
elif lastDigit%3==0:
    print('This number is divisible by 3')
else:
    print('This number is not divisible by 3')
