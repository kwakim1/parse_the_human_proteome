#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 19:55:39 2023

@author: kwakim
"""

#-----
#6.1
#-----

def doubleit(num):
    return num*2

y = 5

dy = doubleit(y)     # calling 'doubleit()', expecting one return value
print(dy)            # 10


#-----
#6.2
#-----

def get_greeting(name):
    return(f'Hello, {name}!')

x = 'World'
y = 'Guido'

z = get_greeting(x)
print(z)

a= get_greeting(y)
print(a)


#-----
#6.3
#-----
def multiplyem(a,b):
    return a*b

a = 5
b = 10

product = multiplyem(a,b)
print(product)

#-----
#6.4
#-----

def multi_div(a):
    return(a*2,a/2)

a,b=multi_div(6)
print(a,b)

#-----
#6.5
#-----

def mul(x,y=1):
    return x*y


b = mul(5, 3)           # int, 15
print(b)
c = mul(5)              # int, 5
print(c)

#-----
#6.6
#-----

# make sure your function does not attempt to return anything
def greet():
    print("hello,world!")
    return None


x = greet()
print(x)         # None

#-----
#6.7
#-----

def do(arg):
    lvar = arg * 2
    return lvar


a = do(5)
print(a)
print(lvar) #error (not available outside the function)


#-----
#6.8
#-----

gvar = 2

def do(arg):
    lvar = arg * gvar
    return lvar


a = do(5)
print(a)

#it works!

#-----
#6.9
#-----

filename = '../pyku.txt'

def get_text(fname):
    fh = open(fname)
    text = fh.read()
    return text

txt = get_text(filename)

# filename = global
# get_text = global
# fh = local
# text = local
# txt = global

#-----
#6.1
#-----












































































