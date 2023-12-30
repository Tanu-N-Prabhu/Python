import sys
import math
from contextlib import redirect_stdout


def compute_closest_to_zero(ts):
    # Write your code here
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    if len(ts) > 0 and len(ts) <= 10000:
        temp = ts[min(range(len(ts)), key = lambda i: abs(ts[i]-0))]
        if temp < 0 and abs(temp) in ts:
            return abs(temp)
        else:
            return temp
    return 0
    


# Ignore and do not change the code below
def main():
    # pylint: disable = C, W
    n = int(input())
    ts = [int(i) for i in input().split()]
    with redirect_stdout(sys.stderr):
        solution = compute_closest_to_zero(ts)
    print(solution)


if __name__ == "__main__":
    main()
