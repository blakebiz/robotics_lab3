import math

from robot_model import *


def test_a():
    # perform dh transformation on args given in assignment
    result = dh_transformation(1, 1, math.pi / 2, math.pi / 2)
    # return the position and rotation of the result
    return get_pos(result), get_rot(result)


def test_b():
    # declare test cases given in slides
    test_cases = [
        [math.pi / 2, .1625, 0, 0],
        [0, -.425, 0, 0],
        [0, -.3922, 0, 0],
        [math.pi / 2, 0, 0, .1333],
        [-math.pi / 2, 0, 0, .0997],
        [0, 0, 0, .0996]
    ]
    # get kinematic chain result of the test cases
    result = kinematic_chain(test_cases)
    # return position and rotation of result
    return get_pos(result), get_rot(result)


if __name__ == '__main__':
    # call the two test functions and print the results
    test1 = test_a()
    print(f'test a: {test1}')
    test2 = test_b()
    print(f'test b: {test2}')

    # for some reason test b appears to work fine (well mostly one or two numbers are very slightly off but I'm assuming
    # that's due to float imprecision)
    # however test a doesn't seem to work at all I'm not sure why, I believe all my math is correct

