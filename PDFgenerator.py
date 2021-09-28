import functions as func
import UforFunction as uf
import ToLaTeX as tex
from pylatex import Document, Section, Subsection, Command, Package
from pylatex.utils import italic, NoEscape
import os
from pylatex import Document, Section, Subsection, Tabular, Math, TikZ, Axis, \
    Plot, Figure, Matrix, Alignat
from DataReader import *
import symbolicalculation as symcal

"""
Assume data is a database without indices (float/int/string matrix). 
Assume var is a list of names of corresponding indices in data (char list)
"""

class PDFgenerator:
    def __init__(self, filename,savename):
        self.filename = filename
        self.savename = savename
        self.dataobj = DataReader(filename)

    def generatePDF(self):
        var = self.dataobj.varList
        data = self.dataobj.dataList
        ub = self.dataobj.UbList
        P = self.dataobj.P
        unitlist = self.dataobj.unitList
        function = self.dataobj.function
        Ubfunclist = self.dataobj.UbFuncList
        flag = self.dataobj.flag
        resvar = self.dataobj.resultVar
        resunit = self.dataobj.resultUnit
        SDMflagList = self.dataobj.SDMflagList
        tempfunction = self.dataobj.TempFunctionList

        ## Decimalize all data in data matrix
        for i in range(0, len(data)):
            for j in range(0, len(data[i])):
                data[i][j] = func.toDecimal(data[i][j])

        for i in range(0, len(ub)):
            if not ub[i] == '':
                ub[i] = func.toDecimal(ub[i])

        row = len(data)  # the number of variables




        MeanDic = {}
        RoundedMeanDic = {}
        SigmaDic = {}
        UaDic = {}
        UbDic = {}
        UDic = {}
        RoundedUDic = {}
        UnitDic = {}


        for i in range(0, row): # first, find all direct variables' mean, sigma, Ua, Ub, U, RoundedU and Roundedmean.
            nowdata = data[i]  # a list
            nowvar = var[i]
            nowtempfunction = tempfunction[i]

            ## Diclize the  variable units
            UnitDic[nowvar] = unitlist[i]

            if nowtempfunction == '':
                nowdata = func.checkeff(nowdata)
                nowdata = func.checkLayouts(nowdata)
                nowmean = func.findMean(nowdata)
                MeanDic[nowvar] = nowmean

                nowsigma = func.findSigma(nowdata)
                SigmaDic[nowvar] = nowsigma

                nowUa = func.findUa(nowdata, len(nowdata), P)
                UaDic[nowvar] = nowUa

                nowUb = ub[i]
                UbDic[nowvar] = nowUb

                nowU = func.findU(nowUa, nowUb)
                UDic[nowvar] = nowU

                nowRoundedU = func.roundU(nowU)
                RoundedUDic[nowvar] = nowRoundedU

                nowRoundedMean = func.roundMean(nowmean, nowRoundedU)
                RoundedMeanDic[nowvar] = nowRoundedMean


        for i in range(0, row): # second find all temp variables' mean, rounded mean, U and roundedU

            nowvar = var[i]
            nowtempfunction = tempfunction[i]
            if not nowtempfunction == '':
                nowmean = uf.findCompMean(nowtempfunction, symcal.findVarInFunction(nowtempfunction), RoundedMeanDic)
                MeanDic[nowvar] = nowmean

                nowU = uf.findAbsFuncU(nowtempfunction, RoundedUDic, symcal.findVarInFunction(nowtempfunction), RoundedMeanDic)
                UDic[nowvar] = nowU

                nowRoundedU = func.roundU(nowU)
                RoundedUDic[nowvar] = nowRoundedU

                nowRoundedMean = func.roundMean(nowmean, nowRoundedU)
                RoundedMeanDic[nowvar] = nowRoundedMean


        # now generate the LaTeX document
        doc = Document(default_filepath='basic',
                       documentclass='article')
        doc.preamble.append(Command('title', 'Physics Experiment Result Report'))
        doc.preamble.append(Command('author', 'User 000'))
        doc.preamble.append(Command('date', NoEscape(r'\today')))
        doc.append(NoEscape(r'\maketitle'))

        counter = 0
        for i in range(0, len(data)):
            counter += 1
            varnow = var[i]
            SDMflag = SDMflagList[i]
            tempfunctionnow = tempfunction[i]
            if tempfunctionnow == '':
                datanow = data[i]
                datanow = func.checkeff(datanow)
                datanow = func.checkLayouts(datanow)
                # try:
                with doc.create(Section('Section '+str(counter)+'. Result for ' + varnow + ':')):
                    if SDMflag == 'Y':
                        doc.append(NoEscape(r'A SDM is used in this section. Thus the variable $' + varnow + r'$\ is actually the $\Delta ' + varnow + '$ throughout this report.'))
                    doc.append(NoEscape(r'The mean for ' + varnow +r'\ is:'))
                    doc.append(NoEscape(tex.generateMeanTeX(varnow, len(datanow), MeanDic[varnow], UnitDic[varnow])))
                    doc.append(NoEscape(r'The sigma (kick off all layouts) is:'))
                    doc.append(NoEscape(tex.generateSigmaTeX(varnow, len(datanow), MeanDic[varnow], SigmaDic[varnow], UnitDic[varnow])))
                    doc.append(NoEscape(r'The type A uncertainty is:'))
                    doc.append(NoEscape(tex.generateUaTeX(len(datanow), func.toDecimal(func.findCorrectionFactor(len(datanow), P)), SigmaDic[varnow], UaDic[varnow], UnitDic[varnow])))
                    doc.append(NoEscape(r'The type B uncertainty is:'))
                    doc.append(NoEscape(tex.generateUbTeX(Ubfunclist[i], UbDic[varnow], UnitDic[varnow])))
                    doc.append(NoEscape(r'The compound uncertainty is:'))
                    doc.append(NoEscape(tex.generateUTeX(varnow, UaDic[varnow], UbDic[varnow], UDic[varnow], UnitDic[varnow])))
                    doc.append(NoEscape(r'By the ceiling principle, the final compound uncertainty for '+varnow + ' is:'))
                    doc.append(NoEscape('\[u(' + varnow + ')=' + RoundedUDic[varnow].to_eng_string() + r'\ ' + UnitDic[varnow] + '\]'))
                    doc.append(NoEscape(r'And the final result for ' + varnow + r'\ is:'))
                    doc.append(NoEscape(tex.generateFinalResult(varnow, RoundedMeanDic[varnow], RoundedUDic[varnow], UnitDic[varnow],P)))
            else: # for temp variables
                with doc.create(Section('Section ' + str(counter) + '. Result for ' + varnow + ':')):
                    doc.append(NoEscape(r'The mean for ' + varnow + r'\ is:'))
                    doc.append(NoEscape(tex.generateCompMeanTeX(varnow, tempfunctionnow, MeanDic[varnow], UnitDic[varnow])))
                    doc.append(NoEscape('The uncertainty is:'))
                    doc.append(NoEscape(tex.generateAbsCompUTeX(varnow, UDic[varnow], UnitDic[varnow], symcal.findVarInFunction(tempfunctionnow))))
                    doc.append(NoEscape(r'And the final result for ' + varnow + r'\ is:'))
                    doc.append(NoEscape(
                        tex.generateFinalResult(varnow, RoundedMeanDic[varnow], RoundedUDic[varnow], UnitDic[varnow],
                                                P)))



        if not counter == 1: # find compond U
            compMean = uf.findCompMean(function, symcal.findVarInFunction(var), MeanDic)
            if flag:
                relaCompU = uf.findRelaFuncU(function, UDic, symcal.findVarInFunction(function), MeanDic)
                absCompUfromRela = uf.findAbsFuncUFromRelaU(compMean, relaCompU)
                RoundedabsCompUfromRela = func.roundU(absCompUfromRela)
                RoundedCompMean = func.roundMean(compMean, RoundedabsCompUfromRela)
                with doc.create(Section('Section ' + str(counter+1))):
                    doc.append(NoEscape('The compound mean is:'))
                    doc.append(NoEscape(tex.generateCompMeanTeX(resvar, function, compMean, resunit)))
                    doc.append(NoEscape(r'The relative compound uncertainty is:'))
                    doc.append(NoEscape(tex.generateRelaCompUTex(resvar, relaCompU, symcal.findVarInFunction(function))))
                    doc.append(NoEscape(r'The absolut compound uncertainty is:'))
                    doc.append(NoEscape(tex.generateAbsCompUFromRelaCompUTex(resvar, compMean, relaCompU, absCompUfromRela, resunit)))
                    doc.append(NoEscape(r'The final result is:'))
                    doc.append(NoEscape(tex.generateFinalResult(resvar, RoundedCompMean, RoundedabsCompUfromRela, resunit, P)))
            else:
                AbsCompU = uf.findAbsFuncU(function, UDic, symcal.findVarInFunction(function), MeanDic)
                RoundedAbsCompU = func.roundU(AbsCompU)
                RoundedCompMean = func.roundMean(compMean, RoundedAbsCompU)
                with doc.create(Section('Section ' + str(counter + 1))):
                    doc.append(NoEscape('The compound mean is:'))
                    doc.append(NoEscape(tex.generateCompMeanTeX(resvar, function, compMean, resunit)))
                    doc.append(NoEscape('The absolut compound uncertainty is:'))
                    doc.append(NoEscape(tex.generateAbsCompUTeX(resvar, AbsCompU, resunit)))
                    doc.append(NoEscape('The final result is:'))
                    doc.append(NoEscape(tex.generateFinalResult(resvar, RoundedCompMean, RoundedAbsCompU, resunit, P)))

        doc.generate_pdf(self.savename, clean_tex=False)
