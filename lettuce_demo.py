from lettuce import *
# 循环实现阶乘
def f(n):
    c = 1
    for i in range(n):
        i = i+1
        c = c*i
    return c

# 递归实现阶乘
def f2(n):
    if n > 1:
        return n*f2(n-1)
    else:
        return 1

#=====================================================
# lettuce实现
@step('I have a number "(.*)"')
def have_a_number(step, number):
    world.number = int(number)

@step('I compute its factorial')
def compute_its_factorial(step):
    world.number = factorial(world.number)

@step('I see the number "(.*)"')
def check_number(step, expected):
    expected = int(expected)
    assert world.number == expected, \
        "Got %s" % world.number

def factorial(number):
    number = int(number)
    if(number == 0) or (number == 1):
        return 1
    else:
        return number
