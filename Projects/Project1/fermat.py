import random


# While for most cases the two algorithms should return the same result for prime_test, there is one major difference
# between the two that will cause some disagreements. As is mentioned in the Algorithms textbook, Fermat's theorem is
# an if statement, not if and only if and
def prime_test(N, k):
    # This is main function, that is connected to the Test button. You don't need to touch it.
    return fermat(N, k), miller_rabin(N, k)


# One function call of mod_exp is Time Complexity O(n^2)
# Because we iterate based on y // 2, we get approximately log y recursive calls of mod_exp
# Assuming y has a similar number of bits as x, we can approximate that log y = O(n)
#
# Therefore, mod_exp total Time Complexity = O(n^3) or in other words O(n^2) for the function, running O(n) times.
#
# mod_exp Space Complexity = O(n) as it has n levels of recursion, so the computer return n times
# and the stack will grow with each recursive call.
def mod_exp(x, y, N):

    # Base case for recursion if y=0 then return 1
    if y == 0:  # Time Complexity O(1)
        return 1  # Time Complexity O(1)

    # Recursive mod_exp call x = x, y = y//2, N = N
    z = mod_exp(x, (y // 2), N)  # Time Complexity for 1 mod_exp call - O(n^2)

    # if y is even return z^2mod N
    if (y % 2) == 0:  # Time Complexity O(1)
        return (z ** 2) % N  # Time Complexity O(n^2) + O(n^2) + O(1) = O(n^2)

    # if y is odd return x*z^2 mod N
    else:  # Time Complexity O(1)
        return (x * (z ** 2)) % N  # Time Complexity O(n^2) + O(n^2) + O(n^2) + O(1) = O(n^2)


# fprobability(k) uses k to make one calculation for the probability and returns it. The function
# uses the ** power operator to calculate 2^k which runs in O(n^2) time.
#
# Because the rest of equation runs in O(1) time, the time complexity for calculating
# probability and the whole function is O(n^2)
#
# The space complexity is O(1) as all the program is doing is creating one variable and returning it.
def fprobability(k):
    # Get probability of Fermat's Little Theorem using 1/(2^k)
    probability = 1 - (1 / (2 ** k))  # Time Complexity O(n^2)

    return probability  # Time Complexity O(1)


# mprobability(k) uses k to make one calculation for the probability and returns it. The function
# is simple, but includes the ** power operator which runs in O(n^2) time.
#
# Because the rest of equation runs in O(1) time, the time complexity for calculating
# probability and the whole function is O(n^2)
#
# The space complexity is O(1) as all the program is doing is creating one variable and returning it.
def mprobability(k):
    # Get probability of M-R test results using 1/(4^k)
    probability = 1 - (1 / (4 ** k))  # Time Complexity O(n^2)

    return probability  # Time Complexity O(1)


# fermat(N, k) uses mod_exp of Time Complexity O(n^3) on each value of an array of length k, making that portion of
# the algorithm run in O(k*n^3) times, where k is the number of loops the for loop is making to test each of the
# random values. There is another for loop before used to generate the values in O(k) times where k is the number
# of values to generate. This is not significant enough to change the result of the Time Complexity analysis.
#
# Therefore, Time Complexity of fermat is O(n^3)
#
# Space Complexity of fermat is O(n) as it only creates the one-dimensional array to store test values.
def fermat(N, k):
    # Check for even N and return composite immediately
    if N % 2 == 0:  # Time Complexity O(1)
        return 'composite'  # Time Complexity O(1)

    # Create empty array to store test values
    test_values = []  # Time Complexity O(1)

    # Generate random values (must be a < N) k times
    for i in range(k):  # Time Complexity O(n)
        test_values.append(random.randint(1, N - 1))  # Time Complexity O(1), Space Complexity O(n)

    #  Loop through test values array - Time Complexity O(n)
    for value in test_values:

        # Run mod_exp for a=x, N-1 = y, and N = N
        fermat_result = mod_exp(value, N-1, N)  # Time Complexity O(n^3)

        # If =! 1 mod N, return composite, end for loop, if == 1 mod N, continue for loop
        if fermat_result != 1:  # Time Complexity O(1)
            return 'composite'  # Time Complexity O(1)

    # return prime if all values pass fermat test
    return 'prime'  # Time Complexity O(1)


# In miller_rabin, most of the Time Complexity stems from calling mod_exp during the while loop to check the test
# values. mod_exp has a Time Complexity of O(n^3). There are three loops within the function, a for loop to set the
# random test values, a for loop to test each value in the array, and a while loop to take the square root of the
# exponential function after running mod_exp to test for primality. Both for loops run in O(k) time where k is the
# number of values to test and the while loop runs in O(log n) time, as it is being divided by 2 with each iteration
# of the loop. However, all of the time complexity of the loop is dominated by the O(n^3) mod_exp function call.
#
# Therefore, the resulting time complexity of the miller_rabin test function is O(n^3).
#
# Space Complexity is O(n) as the function only creates the one dimensional array test_values to store our values
def miller_rabin(N, k):
    # Check for even N and return composite immediately
    if N % 2 == 0:  # Time Complexity O(1)
        return 'composite'  # Time Complexity O(1)

    # Create empty array to store test values
    test_values = []  # Time Complexity O(1)

    # Generate random values (must be a < N) k times
    for i in range(k):  # Time Complexity O(n)
        test_values.append(random.randint(1, N - 1))  # Time Complexity O(1), Space Complexity O(n)

    # Loop through test values array
    for value in test_values:  # Time Complexity O(n)

        # Set variable to track exponent y and result of Miller-Rabin test
        miller_rabin_result = 1  # Time Complexity O(1)
        y = N - 1  # Time Complexity O(1) TODO

        # Repeat Miller-Rabin test until exit condition met
        while miller_rabin_result == 1 and (y % 2) == 0:  # Time Complexity O(log n)
            miller_rabin_result = mod_exp(value, y, N)  # Time Complexity O(n^3)

            # Value passes M-R test if result == -1
            if miller_rabin_result == N - 1:  # Time Complexity O(1)
                break  # Time Complexity O(1)

            # Number is composite if M-R test != 1 or -1
            if miller_rabin_result != 1:  # Time Complexity O(1)
                return 'composite'  # Time Complexity O(1)

            # Square root x^y by dividing y in half
            y = y // 2  # Time Complexity O(1) TODO

    # Return prime if all test values pass M-R test
    return 'prime'  # Time Complexity O(1)
