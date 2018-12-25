#!/usr/bin/env python

import fileinput
from . import unitify


def main():
    for line in fileinput.input():
        print(unitify(line), end='')


if __name__ == "__main__":
    main()
