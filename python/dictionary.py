age=1
while age>0:
    age = input('please input age:')
    if age>=18:
        print('your age is ',age)
        print('adult')
    elif age>=12 :
        print('your age is',age)
        print('teenager')
    else:
        print('your age is ',age)
        print('kid')