import numpy as np

from math import sin, cos, atan, sqrt


def dh_transformation(alpha, a, theta, d):
    # return array with changes listed in assignment applied
    return [[cos(theta), -sin(theta)*cos(alpha), sin(theta)*sin(alpha), a*cos(theta)],
            [sin(theta), cos(theta)*cos(alpha), -cos(theta)*sin(alpha), a*sin(theta)],
            [0, sin(alpha), cos(alpha), d],
            [0, 0, 0, 1]]


def kinematic_chain(array):
    # initialize default array
    result = np.identity(4)
    # loop through given array of arguments
    for args in array:
        # pass args to function then multiply by result and assign return value to result
        result = np.matmul(result, dh_transformation(*args))
    return result


def get_pos(array):
    # return the specified indexes of the given array
    return array[0][3], array[1][3], array[2][3]


def get_rot(array):
    # roll based on assignment criteria
    roll = atan(array[2][1] / array[2][2])
    # pitch based on assignment criteria
    pitch = atan(-array[2][0] / sqrt((array[2][1] ** 2) + (array[2][2] ** 2)))
    # yaw based on assignment criteria
    yaw = atan(array[1][0] / array[0][0])

    return roll, pitch, yaw

