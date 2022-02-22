#!/usr/bin/env python3

def do_twice(f,x):
    f(x)
    f(x)

def do_four(f,x):
    do_twice(f,x)
    do_twice(f,x)

def print_spam():
    print('spam')

def print_twice(bruce):
    print(bruce)
    print(bruce)


do_twice(print,'spam')

do_four(print,'spam')
