import numpy as np
from csv import reader
class DataReader:
    def __init__(self, filename):
        self.filename = filename
        with open(filename, 'rt', encoding='UTF-8') as raw_data:
            readers = reader(raw_data, delimiter=',')
            overx = list(readers)
            data = np.array(overx)
            self.data = data
            self.resultVar = data[0][1]
            self.resultUnit = data[0][3]
            self.function = data[1][1]
            self.P = float(data[0][5])
            if data[1][3] == 'Y':
                self.flag = True
            elif data[1][3] == 'N':
                self.flag = False
            else:
                raise IOError('Y or N wanted, not ' + data[1][3])

            experimentdata = data[4:len(data)]
            tempvarlist = []
            tempunitlist = []
            tempdatalist = []
            tempUblist = []
            tempUbFunclist = []
            for item in experimentdata:
                tempvarlist.append(item[0])
                tempunitlist.append(item[1])
                tempUbFunclist.append(item[2])
                temptempdata = []
                for j in range(3, len(item)):
                    if j == 3:
                        tempUblist.append(item[j])
                    else:
                        if not item[j] == '':
                            temptempdata.append(item[j])
                tempdatalist.append(temptempdata)
            self.varList = tempvarlist
            self.unitList = tempunitlist
            self.dataList = tempdatalist
            self.UbList = tempUblist
            self.UbFuncList = tempUbFunclist