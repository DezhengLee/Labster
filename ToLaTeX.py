from sympy import *
from sympy.abc import *
from decimal import *


def generateMeanTeX(var, length, mean, unit):
    """
    :param var: (Char)
    :param length: (int)
    :param mean: (Decimal)
    :param unit: (String)
    :return:
    """
    string = '\[' +r'\bar{' + var + r'} = \frac{1}{' + str(length) + r'}\sum_{i=1}^{' + str(
        length) + '}' + var + '_i=' + mean.to_eng_string() + '\ ' + unit + '\]'
    return string


def generateSigmaTeX(var, length, mean, sigma, unit):
    """

    :param var: (Char)
    :param length: (int)
    :param mean: (Decimal)
    :param sigma: (Decimal)
    :param unit: (String)
    :return:
    """
    string = '\[' +r'\sigma = \sqrt{\frac{\sum_{i=1}^{' + str(
        length) + '}(' + var + '_i-' + mean.to_eng_string() + ')^2}{' + str(
        length) + '-1}} =' + sigma.to_eng_string() + '\ ' + unit + '\]'
    return string


def generateUaTeX(length, tp, sigma, ua, unit):
    """
    :param length:(int)
    :param tp: (Decimal)
    :param sigma:(Decimal)
    :param ua: (Decimal)
    :param unit: (String)
    :return:
    """
    if not isinstance(tp, Decimal):
        raise TypeError(
            'Here t_P should be in class Decimal not ' + str(type(tp)) + ', please change it to Decimal and '
                                                                         'check the effective digits. ')
    string = '\[' +r'u_A = t_p \cdot \frac{\sigma}{\sqrt{n}} = \frac{' + tp.to_eng_string() + r'\times' + sigma.to_eng_string() + '}{\sqrt{' + str(
        length) + '}} =' + ua.to_eng_string() + '\ (' + unit + ')' + '\]'
    return string


def generateUbTeX(function, ub, unit):
    """

    :param function: (String)
    :param ub: (Decimal)
    :param unit: (String)
    :return: (String)
    """
    try:
        funString = latex(sympify(function))
    except:
        funString = function
    String = '\[' +r'u_B = \Delta_I = ' + funString + '=' + ub.to_eng_string() + '\ ' + unit + '\]'

    return String


def generateUTeX(var, ua, ub, u, unit):
    """

    :param var: (Char)
    :param ua: (Decimal)
    :param ub: (Decimal)
    :param u: (Decimal)
    :param unit: (String)
    :return: (String)
    """
    String = '\[' +r'u(' + var + ')=\sqrt{u_A^2+u_B^2}=\sqrt{' + ua.to_eng_string() + '^2+' + ub.to_eng_string() + '^2}=' + u.to_eng_string() + '\ (' + unit + ')' + '\]'
    return String


def generateCompMeanTeX(wantedvar, function, CompMean, unit):
    try:
        funString = latex(sympify(function))
    except:
        funString = function
    string = '\[' +r'\bar{' + wantedvar + '}=' + funString +"="+ CompMean.to_eng_string() + '\ (' + unit + ')'+ '\]'
    return string


def generateAbsCompUTeX(var, cu, unit, varlist):
    """
    :param var: Char
    :param cu: Decimal
    :return: String
    """
    InnerTerm = r'\left( \frac{\partial ' + var + r'}{\partial ' + varlist[0] + r'} \right)^2\cdot u^2(' + varlist[0] + ')'
    for i in range(1, len(varlist)):
        InnerTerm = InnerTerm + r'+\left( \frac{\partial ' + var + r'}{\partial ' + varlist[i] + r'} \right)^2\cdot u^2(' + varlist[i] + ')'
    formula = r'\sqrt{' + InnerTerm + '}'

    string = '\[' + r'u(' + var + r')=' + formula + '=' + cu.to_eng_string() + '\ (' + unit + ')' + '\]'
    return string


def generateRelaCompUTex(var, cu, varlist):
    """
    :param var: Char
    :param cu: Decimal
    :return: String
    """
    InnerTerm = r'\left( \frac{\partial \ln ' + var + r'}{\partial ' + varlist[0] + r'} \right)^2\cdot u^2(' + varlist[
        0] + ')'
    for i in range(1, len(varlist)):
        InnerTerm = InnerTerm + r'+\left( \frac{\partial \ln ' + var + r'}{\partial ' + varlist[
            i] + r'} \right)^2\cdot u^2(' + varlist[i] + ')'
    formula = r'\sqrt{' + InnerTerm + '}'

    string = '\[' +r'E_' + var + r'=\frac{u(' + var + r')}{\bar{' + var + '}}='+ formula + '=' + cu.to_eng_string() + '\]'
    return string


def generateAbsCompUFromRelaCompUTex(var, mean, relativeU, cu, unit):
    """

    :param var:
    :param mean:
    :param relativeU:
    :param cu: Decimal , should only have 1 effective digit
    :param unit:
    :return:
    """
    string = '\[' +r'u(' + var + r')=\bar{' + var + r'}\cdot E_{' + var + '} = ' + mean.to_eng_string() + r'\times' + relativeU.to_eng_string() + '=' + cu.to_eng_string() + '\ (' + unit + ')' + '\]'
    return string


def generateFinalResult(var, mean, u, unit, P):
    """
    :param var: char
    :param Mean: rounded
    :param u: Decimal 1 digit
    :param unit:
    :param P: int
    :return:
    """
    string = '\[' + var + r'=(' + mean.to_eng_string() + r'\pm' + u.to_eng_string() + ')' + r'\ ' + unit + r'\ (P=' + str(P) + ')\]'
    return string

varlist=['a', 'b', 'c']
var='T'
cu=Decimal("3.1")
unit = "cm"
print(generateAbsCompUTeX(var, cu, unit, varlist))
