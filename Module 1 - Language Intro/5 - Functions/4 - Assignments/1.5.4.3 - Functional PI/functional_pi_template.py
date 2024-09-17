import math


def my_pi(target_error):
    """
    Implementation of Gauss–Legendre algorithm to approximate PI from https://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_algorithm

    :param target_error: Desired error for PI estimation
    :return: Approximation of PI to specified error bound
    """

    ### YOUR CODE HERE ###
    a = 1
    b = 1 / (math.sqrt(2))
    t = 0.25
    p = 1
    
    for n in range(1, 10):

        an = (a+b)/2
        bn = math.sqrt(a*b)
        pn = 2*p
        tn = t-p * ((an-a)**2)

        a = an
        b = bn
        t = tn
        p = pn

        my_pi = ((an + bn)**2)/(4*tn)


    # change this so an actual value is returned
    return my_pi




desired_error = 1E-10

approximation = my_pi(desired_error)

print("Solution returned PI=", approximation)

error = abs(math.pi - approximation)

if error < abs(desired_error):
    print("Solution is acceptable")
else:
    print("Solution is not acceptable")
