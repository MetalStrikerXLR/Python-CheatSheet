try:
    age = int(input('age: '))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print('Age cant be 0')
except ValueError:
    print('Invalid value')