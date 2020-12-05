#! /usr/bin/env/python
import os

def load_data():
    cwd = os.getcwd()
    with open(f"{cwd}/input.txt") as f:
        data = f.read().splitlines()
        return data

data = load_data()

row_size = len(data)
column_size = len(data[0])

def traverse_hill(x,y):
    pos_x, pos_y = 0, 0
    trees_encountered_count = 0

    while pos_y < row_size:
        if data[pos_y][pos_x] == "#":
            trees_encountered_count += 1
        pos_x += x
        pos_y += y
        
        if pos_x >= column_size:
            pos_x = pos_x - column_size

    return trees_encountered_count

print(f"Part 1: {traverse_hill(3,1)}")

print(f"Part 2: {traverse_hill(1,1)*traverse_hill(3,1)*traverse_hill(5,1)*traverse_hill(7,1)*traverse_hill(1,2)}")
