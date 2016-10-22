from timeit import default_timer

from domino import build_matrix
from domino import brute_force
from domino import constant


N_EXECUTIONS = 300

LOG_FILE = "times.log"

def compute():
    """ Runs all algorithms N_EXECUTIONS times. On each execution logs time
    execution results to a file
    """

    with open(LOG_FILE, "w") as output:

        header = "Input{0}Brute Force{0}Constant\n"
        print(header.format("\t"))
        output.write(header.format(", "))

        # We start from 1 because there is no result of a matrix of length 0
        for i in range(1, N_EXECUTIONS):
            matrix = build_matrix(i)

            # Compute brute force algorithm
            start_brute_force = default_timer()
            total_brute_force = brute_force(matrix)
            elapsed_brute_force = default_timer() - start_brute_force

            # Compute constant algorithm
            start_constant = default_timer()
            total_constant = constant(len(matrix))
            elapsed_constant = default_timer() - start_constant

            print("{0}\t{1}\t{2}".format(i, elapsed_brute_force,
                elapsed_constant))
            # Logs to file
            output.write("{0}, {1}, {2}\n".format(i, elapsed_brute_force,
                elapsed_constant))

if __name__ == "__main__":
    compute()
