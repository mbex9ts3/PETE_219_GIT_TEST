from numpy import random as rand
def PETE_219_fun(n):
    for i in range(n):
        x = rand.random()
        if x >= 0.5:
            print('x is pretty large!')
        else:
            print('x is pretty small')
    