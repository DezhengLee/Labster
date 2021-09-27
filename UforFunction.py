from sympy import *
from sympy.abc import *
import functions as func
from decimal import *

def findAbsFuncU(function, U, variable, means, roundornot=True):
    """
    :param function: (String) the formula
    :param U: (Decimal dic, keys: variable) ceiled
    :param variable: (char list) [x,y,z,...]
    :param means: (Decimal dic, keys: variable)
    :return: (Decimal)
    """
    resultListSquared = []
    values = []
    for k in variable:
        values.append(float(means[str(k)]))

    for k in variable:
        tempfunc = lambdify(variable, diff(function, k), 'numpy')
        tempvalue = tempfunc(*values)
        resultListSquared.append((tempvalue**2) * float(U[str(k)]**2))

    sumResult = Decimal(sum(resultListSquared))
    result = sumResult.sqrt()

    if roundornot:
        resultString = result.to_eng_string()
        intPart = resultString.split('.')[0]
        try: # may not have '.'
            decimalPart = resultString.split('.')[1]
            digiteff = 0
            if intPart == '0':
                while decimalPart[digiteff] == '0':
                    digiteff += 1
                digiteff += 2
            else:
                digiteff = -len(intPart) + 2 # may not true
        except IndexError:
            digiteff = -len(intPart) + 2  # may not true
        return result.quantize(func.rounddigits(digiteff), ROUND_HALF_EVEN)
    else:
        return result


def findRelaFuncU(function, U, variable, means, roundornot=True):
    """
    :param function: (String) the formula
    :param U: (Decimal dic, keys: variable) ceiled
    :param variable: (char list) [x,y,z,...]
    :param means: (Decimal dic, keys: variable)
    :return: (Decimal)
    """
    lnfunction = 'ln(' + function + ')'
    result = findAbsFuncU(lnfunction, U, variable, means, roundornot=roundornot)
    return result


def findCompMean(function, variable, means):
    """

    :param function:
    :param variable:
    :param means:
    :return:
    """
    values = [] # in float
    for k in variable:
        values.append(float(means[str(k)]))

    tempfunc = lambdify(variable, function, 'numpy')
    result = Decimal(tempfunc(*values))

    efflist = []
    for k in variable:
        eff = func.eff(means[str(k)])
        efflist.append(eff)

    smallest = min(efflist)
    dig = smallest
    intPart = result.to_eng_string().split('.')[0]
    DecimalPart = result.to_eng_string().split('.')[1]
    if len(intPart) == 1 and intPart[0] == '0':
        i = 0
        while DecimalPart[i] == '0':
            i += 1
            dig += 1
    else:
        dig = dig - len(intPart)
    return result.quantize(func.rounddigits(dig + 1), ROUND_HALF_EVEN)


def findAbsFuncUFromRelaU(CompMean, ru):
    """
    :param CompMean:
    :param ru:
    :return:
    """
    result = CompMean * ru

    resultString = result.to_eng_string()
    intPart = resultString.split('.')[0]
    try:  # may not have '.'
        decimalPart = resultString.split('.')[1]
        digiteff = 0
        if intPart == '0':
            while decimalPart[digiteff] == '0':
                digiteff += 1
            digiteff += 2
        else:
            digiteff = -len(intPart) + 2
    except IndexError:
        digiteff = -len(intPart) + 2  # may not true
    return result.quantize(func.rounddigits(digiteff), ROUND_HALF_EVEN)

