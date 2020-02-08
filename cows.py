#!/usr/bin/python3
# coding: utf-8


import random


def bc(query, target):
    b, c = 0, 0
    digits = [0 for _ in range(10)]
    for i in range(len(query)):
        if query[i] == target[i]:
            b += 1
        else:
            digits[int(target[i])] += 1
    for i in range(len(query)):
        if query[i] == target[i]:
            continue
        d = int(query[i])
        if digits[d] > 0:
            c += 1
            digits[d] -= 1
    return b, c
            

def convert2string(number, count):
    result = str(number)
    while len(result) < count:
        result = "0" + result
    return result


def main():
    target = convert2string(random.randint(0, 9999), 4)
    while True:
        query = input("Enter number: ")
        b, c = bc(query, target)
        print(b, c)
        if b == 4:
            break


if __name__ == "__main__":
    main()

