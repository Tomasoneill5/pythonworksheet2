numberOne= int(input('Enter your first number: '))
numberTwo= int(input('Enter your second number: '))
if numberOne>numberTwo:
    print(numberOne, numberTwo)
elif numberOne<numberTwo:
    print(numberTwo, numberOne)
elif numberOne==numberTwo:
    print('The numbers are equal:', numberOne,'and', numberTwo)