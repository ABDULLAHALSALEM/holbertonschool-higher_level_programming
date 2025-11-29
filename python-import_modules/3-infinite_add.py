#!/usr/bin/python3
import sys

if __name__ == "__main__":
    total = 0
    args = sys.argv[1:]

    for number in args:
        total += int(number)

    print(total)
