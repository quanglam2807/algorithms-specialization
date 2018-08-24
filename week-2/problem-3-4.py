# TO-DO
# Problem 3.4 (Difficult.) You are given an n-by-n grid of distinct numbers.
# A number is a local minimum if it is smaller than all its neighbors. (A neighbor of a number
# is one immediately above, below, to the left, or to the right.
# Most numbers have four neighbors; numbers on the side have three;
# the four corners have two.) Use the divide-and-conquer algorithm design
# paradigm to compute a local minimum with only O(n) comparisons between
# pairs of numbers. (Note: since there are n2 numbers in the input,
# you cannot afford to look at all of them.)

def main():
    with open('week-2/problem-3-4.in') as f:
        lines = f.readlines()

    grid = [[int(x) for x in line.rstrip('\n').split(' ')] for line in lines]

    print(grid)

if __name__ == "__main__":
    main()
