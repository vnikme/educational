#!/usr/bin/python3
# coding: utf-8


import time, random


def selection_sort(a):
    n = len(a)
    for i in range(n):
        m = i
        for j in range(i + 1, n):
            if a[j] < a[m]:
                m = j
        a[m], a[i] = a[i], a[m]
    return a


def read_data():
    return list(map(int, input().split()))
    #return [random.randint(0, 1000000) for _ in range(50000)]


def main():
    a = read_data()
    print(a)
    start_ts = time.time()
    a = selection_sort(a)
    a = sorted(a)
    print(time.time() - start_ts)
    print(a)


if __name__ == "__main__":
    main()

