#! /usr/bin/env/python

import os
import operator
import itertools
import functools

def get_numbers_from_file():
    cwd = os.getcwd()
    input_file = open(f"{cwd}/input.txt",'r')
    input_numbers = [int(i) for i in input_file]
    return input_numbers

def get_product(numbers_to_multiply):
    return(functools.reduce(operator.mul, [i for i in numbers_to_multiply], 1))

def find_two_numbers_equaling_sum(input_numbers,sum_target=2020):
   for i in input_numbers:
       number_to_find = sum_target - i
       if number_to_find in input_numbers:
           return(i,number_to_find)

numbers_to_multiply = find_two_numbers_equaling_sum(get_numbers_from_file())
print(f"Part 1: {get_product(numbers_to_multiply)}")

def find_any_amount_of_numbers_equaling_sum(input_numbers,sum_target=2020,number_of_combinations=3):
    for i in itertools.combinations(input_numbers,number_of_combinations):
        if sum(i) == sum_target:
            return(i)

numbers_to_multiply = find_any_amount_of_numbers_equaling_sum(get_numbers_from_file())
print(f"Part 2: {get_product(numbers_to_multiply)}")