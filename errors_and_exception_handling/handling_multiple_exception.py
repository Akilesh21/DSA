try:
    a = 10
    b = 0
    c = a/b
    print(c)
except NameError:
    print('Name Error occured')
except ZeroDivisionError:
    print('Zero Division Error occured')