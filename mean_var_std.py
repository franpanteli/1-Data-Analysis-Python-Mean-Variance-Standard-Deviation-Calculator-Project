#!/usr/bin/env python3
"""
Author: Frankie Panteli
"""
import numpy as np


def calculate(list_numbers):
    """
    This function outputs summary statistics for the rows, columns, and elements in a 3 x 3 matrix.
    This is inputted into the function as a 1x9 array. 
    These summary statistics are:
    - mean;
    - variance;
    - standard deviation;
    - max;
    - min
    - sum.
    """

    # If the input array does not contain 9 values, a ValueError is raised
    if len(list_numbers) < 9:
        raise ValueError("List must contain nine numbers.")

    # To convert the input array into a 3x3 matrix 
    np_matrix = np.array(list_numbers).reshape((3, 3))

    # Defining a dictionary in the syntax of the output which we want to return 
    dict_statistics = {
        'mean': np.mean,
        'variance': np.var,
        'standard deviation': np.std,
        'max': np.max,
        'min': np.min,
        'sum': np.sum,
    }

    # Populating the dictionary with the list of statistics for the array 
    calculations = dict()
    for name, function in dict_statistics.items():
        calculations[name] = [
            function(np_matrix, axis=0).tolist(),
            function(np_matrix, axis=1).tolist(),
            function(np_matrix).tolist()]
    return calculations
