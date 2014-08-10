#!/usr/bin/python3
"""\
Solution to the water problem\
"""

import random
from termcolor import cprint
import sys


def print_arr(array, array2=None):
    """Print array one as solid blocks and array2 as water."""
    if array2 is None:
        print("Before:")
        array2 = [0 for _ in array]
    else:
        print("After:")
    for i in range(len(array)):
        cprint('_'*array[i], 'grey', 'on_white', attrs=['dark'], end='')
        cprint('~'*array2[i], 'cyan')


def solve(array1, silent=False):
    """Solve the water problem, that is find where the water would get stuck
    in array1."""
    biggest_el = max(array1)
    amount_of_el = len(array1)
    array2 = [biggest_el - i for i in array1]

    total = [array1[i]+array2[i] for i in range(amount_of_el)]

    fixed = True
    while fixed:
        fixed = False
        # First one always has to spill
        if array2[0] != 0:
            fixed = True
            array2[0] = 0
            total[0] = array1[0]
        # The rest spills to neighbours
        for i in range(1, amount_of_el - 1):
            # Decide whether to spill left or right
            comp = total[i - 1] if total[i-1] < total[i + 1] else total[i+1]
            # Spill if higher but only if water left
            if total[i] > comp and array2[i] != 0:
                fixed = True
                array2[i] = max(comp - array1[i], 0)
                total[i] = array1[i] + array2[i]
        # Last one always has to spill
        if array2[-1] != 0:
            fixed = True
            array2[-1] = 0
            total[-1] = array1[-1]

    if not silent:
        print_arr(array1, array2)
    print("Total water left: {}".format(sum(array2)))


def main():
    """Prepare arrays, print them and solve the water problem."""
    # Preparing
    if len(sys.argv) < 2:
        total = 10
    else:
        total = int(sys.argv[1])
    silent = False
    if total > 80:
        silent = True
    array1 = [random.randint(0, total) for _ in range(total)]
    if not silent:
        print_arr(array1)
    solve(array1, silent)

if __name__ == "__main__":
    main()
    print(__doc__)
