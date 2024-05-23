#!/usr/bin/env python3

def happy_new_year():
    counter =10
    while counter>=1:
        print(counter)
        counter -=1
    print('Happy New Year!')


def square_integers(int_list):
    squared_list =[x**2 for x in int_list]
    return squared_list
print(square_integers([1,2,3,4,5]))


def fizzbuzz():
    i=1
    while i<=100:

        if i%3==0 and i%5==0:
            print("FizzBuzz")
        elif i%3==0:
           print("Fizz")
        elif i%5==0:
            print("Buzz")
        else:
            print(i)
        i+=1

fizzbuzz()