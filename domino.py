

#
# Possibility matrix considering a Domino with 0 ~ 6 parts.
#
# matrix = [# 0  1  2  3  4  5  6
#            [0, 1, 0, 1, 0, 1, 0], # 0
#            [1, 0, 1, 0, 1, 0, 1], # 1
#            [0, 1, 0, 1, 0, 1, 0], # 2
#            [1, 0, 1, 0, 1, 0, 1], # 3
#            [0, 1 ,0, 1, 0, 1, 0], # 4
#            [1, 0, 1, 0, 1, 0, 1], # 5
#            [0, 1, 0, 1, 0, 1, 0], # 6
#        ]
#


def build_matrix(n):
    """ Function to create square matrix based on n. N is the matrix size

         n, n-j
         E
         E (i+j) % 2
         E
        i=0, j=1

        consider the 3 leter E as the Sum symbol
    """

    if n <= 0:
        raise ValueError("Wrong matrix size: %s" % str(n))

    matrix = []
    for i in range(n):
        for j in range(n):

            # Gets 0 if the sum of i and j is even. Otherwise 1 if odd
            value = (i + j) % 2
            try:
                matrix[i].insert(j, value)
            except IndexError:
                matrix.insert(i, [value])

    return matrix


def brute_force(matrix):
    """ Brute force algorithm to count all odd numbers resulted from i + j

        This brute force approach takes n^2/2 - n iteration to complete:

        Time complexity: O(n^2)
        Storage complexity: n * m

    """

    total = 0  # Total odd numbers

    rows = cols = len(matrix)
    increment = 1  # Starts from 1 because determinant values are always even

    for i in range(rows):
        for j in range(increment, cols):

            if (i + j) % 2:  # If sum is odd we increment total
                total += 1
        increment += 1
    return total


def constant(n):
    """ Constant execution algorithm that computes the domino problem using a
        function to calculate the total odd number:

        Time complexity: O(1)
        Storage complexity: -

        Formula is as follows:

        . if matrix size (n) is even then the number of odd and even numbers
          are equal to n/2

        . Otherwise, if matrix size (n) is odd then even numbers are equal
          n/2 + 1
    """

    n_even = n_odd = int(n / 2)

    if n % 2:  # Matrix size is odd?
        n_even = int(n / 2) + 1

    # Domino problem is soved by simple multiplication of even and odd number
    # inside a matrix of size n
    return int(n_even * n_odd)
