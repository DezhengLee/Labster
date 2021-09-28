import numpy as np
from sympy import *

def findVarInFunction(function):
    """
    :param function: String
    :return: list
    """
    resultset = set()
    for char in function:
        if char.isalpha():
            resultset.add(char)
    return list(resultset)
