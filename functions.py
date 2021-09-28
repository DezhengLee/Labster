from decimal import *

"""
All the data are in type of Decimal, all data are analysed in  2-d matrix of numpy
"""

rowindex = [0.683, 0.9, 0.955, 0.997]
columnindex = [3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 21]

data = [
    ['1.32', '1.2', '1.14', '1.11', '1.09', '1.08', '1.07', '1.06', '1.04',
     '1.03', '1'],
    ['2.92', '2.35', '2.13', '2.02', '1.94', '1.89', '1.86', '1.83', '1.76',
     '1.73', '1.65'],
    ['4.3', '3.18', '2.78', '2.56', '2.45', '2.37', '2.31', '2.26', '2.15',
     '2.09', '1.96'],
    ['9.93', '5.84', '4.6', '4.03', '3.71', '3.5', '3.36', '3.25', '2.98',
     '2.86', '2.58']]


def toDecimal(num):
    """
    :param num: a number from the test data which is of type float, int or string
    :return: the corresponding number in type of Decimal
    """
    if isinstance(num, str):
        return Decimal(num)
    else:
        num = str(num)
        return Decimal(num)


def rounddigits(inttype):
    """
    Given a int number, pop a Decimal with the digits of inttype. eg. input:3, output: Decimal('0.001')
    This should be only used in .quantize() method in Decimal class.
    :param inttype: a number in type of int
    :return: a Decimal with the digits of inttype
    """
    return Decimal(10) ** ((-1) * inttype)


def eff(num):
    """
    接受一个数字num in Decimal并返回其有效数字数量
    :param num: a number in type of Decimal
    :return: the number of effective digits
    """
    num = num.to_eng_string()
    assert isinstance(num, str)
    digits = 0
    is_leading_zero = True
    for i in range(len(num)):
        if num[i] == 'E' or num[i] == 'e':
            break
        digit = ord(num[i]) - ord('0')
        if 0 <= digit <= 9:
            if digit > 0 or (digit == 0 and not is_leading_zero):
                digits += 1  # 每遇到有效数字: digit++
                is_leading_zero = False  # 遇到第一个有效数字后所有的0都不是leading zero了，都是有效数字
    return max(digits, 1)


def digits(num, truedigit=False):
    """
    :param num: (Decimal) a number in type of Decimal
    :return: (int) the effective digits after the decimal dot
    """
    if not isinstance(num, Decimal):
        raise TypeError(r'<class \'Decimal\'> type is needed, not ' + str(type(num)) + '.')

    numstr = num.to_eng_string()
    try:
        temp = numstr.split('.')[1]
    except:  # if num is an integer
        return len(numstr.split('.')[0])

    if truedigit:
        # if number is a pure dicemal
        if numstr.split('.')[0] == '0':
            return eff(num)
        else:
            return len(temp)
    else:
        return len(temp)


def checkeff(datamat):
    # Need to be tested#
    """
    This function is used to check if there are any data loose their last digit '0' throughout the numpy data matrix
    :param datamat: the checked numpy datamatrix with elements in type of Decimal. ¡The data must not have any indices!
    :return: the corrected datamatrix
    """
    counter = {}
    length = len(datamat)
    for i in range(0, length):
        num = datamat[i]
        try:
            counter[str(digits(num))] += 1
        except KeyError:
            counter[str(digits(num))] = 1
    if len(counter) == 1:
        print("No data need to be fixed.")
        return datamat
    else:
        tempkeyarray = []
        tempvaluearray = []
        for k in counter.keys():
            tempkeyarray.append(k)
            tempvaluearray.append(counter[k])
        maxdigit = tempkeyarray[tempvaluearray.index(max(tempvaluearray))]
        maxdigit = int(maxdigit)
        for i in range(0, length):
            datamat[i] = datamat[i].quantize(Decimal(10) ** ((-1) * maxdigit))

        print("Data has been fixed")
        return datamat


def findMean(array, auto=True, roundornot=True):
    """
    :param array: (Decimal array) an array which elements are in type of Decimal
    :param auto: (boolean) switch if the return value saves one digit more automatically, default as true
    :param roundornot: (boolean) choose if the the result is to be rounded
    :return: (Decimal) the mean of this array in Decimal
    """
    digeff = digits(array[0])  # the effective digits after the decimal dot
    if auto:
        digeff += 1

    n = Decimal(len(array))  # the length of array in type of Decimal
    arraysum = sum(array)

    mean = arraysum / n
    if roundornot:
        meanString = mean.to_eng_string()
        meanStringDecimalPart = meanString.split('.')[1]
        if len(meanStringDecimalPart) == (digeff - 1):
            digeff -= 1
        return mean.quantize(rounddigits(digeff), ROUND_HALF_EVEN)
    else:
        return mean


def findSigmaSquare(array, auto=True, perceMod=False, roundornot=True):
    """
    Give the variance of the input array (data).
    :param array: (Decimal array) the data that is wanted to find the variance.
    :param auto: (boolean) switch if the return value saves one digit more automatically, default as true.
    :param perceMod: (boolean) switch if calculate from the original array or by function .findMean(auto = Ture)
    :param roundornot: (boolean) choose if the the result is to be rounded
    :return: (Decimal) the sample variance.
    """
    digeff = digits(array[0])  # the effective digits after the decimal dot
    if auto:
        digeff += 1

    n = Decimal(len(array))
    if not perceMod:
        mean = findMean(array, auto=True, roundornot=True)
    else:
        mean = findMean(array, auto=True, roundornot=False)

    errorSquareSum = sum([(x - mean) ** 2 for x in array])
    sigmaSquare = errorSquareSum / (n - 1)

    if roundornot:
        return sigmaSquare.quantize(rounddigits(digeff), ROUND_HALF_EVEN)
    else:
        return sigmaSquare


def findSigma(array, auto=True, perceMod=True, roundornot=True):
    """
    :param array: (Decimal array) the data that is wanted to find the SD.
    :param auto: (boolean) switch if the return value saves one digit more automatically, default as true.
    :param perceMod: (boolean) switch if calculate from the original array or by function .findMean(auto = Ture)
    :return: (Decimal) the standard difference of the input data
    """

    if not perceMod:
        SigmaSquare = findSigmaSquare(array, auto=True, perceMod=False, roundornot=True)
    else:
        SigmaSquare = findSigmaSquare(array, auto=True, perceMod=True, roundornot=False)

    sigma = SigmaSquare.sqrt()
    zeroflag = False
    decimalflag = False

    sigmaString = sigma.to_eng_string()
    intPart = sigmaString.split('.')[0]
    if not len(intPart) == len(sigmaString):
        decimalflag = True
        decimalPart = sigmaString.split('.')[1]
        digiteff = 0
        if intPart == '0':
            while decimalPart[digiteff] == '0':
                digiteff += 1
            digiteff += 2
        else:
            digiteff = -len(intPart) + 2
    elif sigmaString == '0':
        zeroflag = True
    else:
        digiteff = 0
        digiteff = -len(intPart) + 2

    if roundornot:
        if zeroflag:
            return sigma.sqrt()
        elif decimalflag:
            if decimalPart[digiteff - 1] == '0':
                digiteff += 1
            return (SigmaSquare.sqrt()).quantize(rounddigits(digiteff), ROUND_HALF_EVEN)
        else:
            return (SigmaSquare.sqrt()).quantize(rounddigits(digiteff), ROUND_HALF_EVEN)
    else:
        return SigmaSquare.sqrt()


def findAverageStanderdDifference(array, auto=True, perceMod=False, roundornot=True):
    """

    :param array: (Decimal array)
    :param auto: (boolean)
    :param perceMod: (boolean)
    :param roundornot: (boolean)
    :return: (Decimal)
    """
    digeff = digits(array[0])  # the effective digits after the decimal dot
    if auto:
        digeff += 1

    if not perceMod:
        sigma = findSigma(array, auto=True, perceMod=False, roundornot=True)
    else:
        sigma = findSigma(array, auto=True, perceMod=True, roundornot=False)

    n = Decimal(len(array))
    if roundornot:
        return (sigma / (n.sqrt())).quantize(rounddigits(digeff), ROUND_HALF_EVEN)
    else:
        return sigma / (n.sqrt())


def findPIndexOfFactor(number):
    try:
        return rowindex.index(number)
    except BaseException:
        print('Cannot Find Corresponding Index of Input P.')


def findnIndexOfFactor(number):
    try:
        return columnindex.index(number)
    except BaseException:
        print('Cannot Find Corresponding Index of Input n.')


def findCorrectionFactor(n, P):
    """

    :param n: (int) the number of attempts of experiments
    :param P: (float) the wanted probability
    :return: (Decimal) the correction factor
    """
    return Decimal(data[findPIndexOfFactor(P)][findnIndexOfFactor(n)])


def checkLayouts(array, range=3):
    """
    :param array: (Decimal array) input data.
    :param range: (int > 0) the range (x*sigma, default for x = 3) of layout range.
    :return: (Decimal array) the array with out layouts. If there is any layouts, a notification
                will show up.
    """
    mean = findMean(array)
    sigma = findSigma(array)
    minus3sigma = mean - range * sigma
    plus3sigma = mean + range * sigma
    newarray = []

    flag = 0
    for x in array:
        if x <= plus3sigma and x >= minus3sigma:
            newarray.append(x)
        else:
            if flag == 1:
                print('Layout:' + str(x))
            else:
                flag = 1
                print('There are layouts in this data.')
                print('Layout:' + str(x))
    return newarray


def findUa(array, n, P, perceMod=False, roundornot=True):
    CorrectionFactor = findCorrectionFactor(n=n, P=P)
    if perceMod:
        sigma = findSigma(array, perceMod=True, roundornot=False)
    else:
        sigma = findSigma(array)
    n = Decimal(len(array))
    Ua = CorrectionFactor * sigma / n.sqrt()

    zeroflag = False
    decimalflag = False

    UaString = Ua.to_eng_string()
    intPart = UaString.split('.')[0]
    if not len(intPart) == len(UaString): # the number is not a int
        decimalflag = True
        decimalPart = UaString.split('.')[1]  # Ua cannot be zero
        digiteff = 0
        if intPart == '0':
            try:
                while decimalPart[digiteff] == '0': # find the second effective digits
                    digiteff += 1
                digiteff += 2
            except IndexError: # the decimal is also equal to 0 (ua is 0.000)
                digiteff = 1
        else:
            digiteff = -len(intPart) + 2
    elif UaString == '0':
        zeroflag = True
    else:
        digiteff = 0
        digiteff = -len(intPart) + 2

    if roundornot:
        if zeroflag:
            return Ua
        elif decimalflag:
            return Ua.quantize(rounddigits(digiteff))
        else:
            return Ua.quantize(rounddigits(digiteff))
    else:
        return Ua


def findU(Ua, Ub, roundornot=True):
    """
    :param Ua: (Decimal)
    :param Ub: (Decimal)
    :return: (Decimal)
    """
    if (not isinstance(Ua, Decimal)) or (not isinstance(Ub, Decimal)):
        raise TypeError("<Class \'Decimal\'> is needed here, not " + str(type(Ua)) + " and " + str(type(Ub)))

    U = (Ua ** 2 + Ub ** 2).sqrt()

    if roundornot:
        UString = U.to_eng_string()
        intPart = UString.split('.')[0]
        decimalPart = UString.split('.')[1]  # U cannot be zero
        digiteff = 0
        if intPart == '0':
            while decimalPart[digiteff] == '0':
                digiteff += 1
            digiteff += 2
        else:
            digiteff = -len(intPart)
        return U.quantize(rounddigits(digiteff), ROUND_HALF_EVEN)
    else:
        return U


def roundU(u):
    """
    Give a uncertainty U, round this U to
    :param u: Decimal
    :return: Decimal
    """
    string = u.to_eng_string()
    intpart = string.split('.')[0]
    try:
        decimalpart = string.split('.')[1]
        digiteff = 0
        if intpart == '0':
            while decimalpart[digiteff] == '0':
                digiteff += 1
            digiteff += 1
        else:
            digiteff = -len(intpart) + 1
    except IndexError:
        digiteff = -len(intpart) + 1  # may not true
    return u.quantize(rounddigits(digiteff), ROUND_UP)


def roundMean(mean, roundedU):
    """
    :param mean: Decimal mean with one digit more
    :param roundedU: Decimal rounded u with only 1 effective digit
    :return:
    """
    return mean.quantize(roundedU, ROUND_HALF_EVEN)
