# coding:utf-8
import os.path as osp
import os
import decoder
import pickle
import pandas as pd
from tqdm import tqdm
import numpy as np
__COUNTER_CHECK__ = False
htmlPath = 'C:\\Users\\K\\Desktop\\NSIdata\\html'

# print(os.checkMultiChoicesstdir(htmlPath))

counter = 0
checkMultiChoices = []
for i in range(40):
    checkMultiChoices.append([])
dataSheet = []

for file in tqdm(os.listdir(htmlPath), ncols=60):
    counter += 1
    if counter > 10 and __COUNTER_CHECK__:
        break
    fileHdl = osp.join(htmlPath, file)
    fileInfo = decoder.decodeFile(fileHdl)
    # print(len(fileInfo))
    # print(len(fileInfo), fileInfo[0])
    if len(dataSheet) == 0:
        dataSheet.append([])
        for it in fileInfo:
            dataSheet[0].append(it[0])
    if fileInfo[0][1] != '':
        dataSheet.append([])
        for it in fileInfo:
            cont = it[1]
            if type(it[1]) == type([]):
                cont = ''
                itLen = len(it[1])
                for j in range(itLen):
                    cont += it[1][j]
                    if j != itLen - 1:
                        cont += ' '
            try:
                cont = int(cont)
            except ValueError:
                cont = cont
            dataSheet[counter].append(cont)
    else:
        counter -= 1
    # ----------Data Sheet End -------------------
    # ----------Multiple choices -----------------
    # for i in range(len(fileInfo)):
    #     item = fileInfo[i]
    #     if type(item) != type([]):
    #         if item not in checkMultiChoices[i]:
    #             checkMultiChoices[i].append(item.strip())
    #         if item[0] not in checkMultiChoices[i]:
    #             checkMultiChoices[i].append(item[0])
    #     if type(item) == type([]):

    #         if type(item[1]) == type([]):
    #             for j in item[1]:
    #                 if j not in checkMultiChoices[i] and j != '':
    #                     checkMultiChoices[i].append(j)
    # ----------Multiple choices End-----------------

# for i in checkMultiChoices:
#     print(len(checkMultiChoices))
# print(checkMultiChoices)
# ---------------Data Sheet Clearning ------------------
print('Data Clearning')
for i in range(len(dataSheet)):
    for j in range(40):
        if j in [6, 7, 8, 9] and i > 0:
            if type(dataSheet) == type(''):
                if dataSheet[i][j] == '':
                    dataSheet[i][j] = np.nan
                if ',' in dataSheet[i][j]:
                    print(dataSheet[i][j])
                    dataSheet[i][j] = dataSheet[i][j].replace(',', '')
                if '万' in dataSheet[i][j]:
                    dataSheet[i][j] = dataSheet[i][j].replace('万', '0000')
                if '+' in dataSheet[i][j]:
                    _ = dataSheet[i][j].split('+')
                    dataSheet[i][j] = int(_[0]) + int(_[1])
            if dataSheet[i][j] != np.nan:
                try:
                    dataSheet[i][j] = int(dataSheet[i][j])
                except ValueError:
                    print(dataSheet[i][j])

# ---------------Data Sheet Clearning ------------------
# ---------------Create datasheet ----------------------
with open('datasheet.txt', 'w') as f:
    datatxt = ''
    for i in dataSheet:
        dataline = ''
        for j in i:
            dataline += str(j) + ' '
        dataline += '\n'
        datatxt += dataline
    f.write(datatxt)
dataFrame = pd.DataFrame(dataSheet)
dataFrame.to_csv('data.csv')
dataSheetFile = open('data.pkl', 'wb')
pickle.dump(dataSheet, dataSheetFile)

# print(dataSheet)

# ---------------Create Multiple Choice Summary---------------
# with open('summary.txt', 'w') as f:
#     summary = ''
#     for i in checkMultiChoices:
#         if len(i) > 1:
#             summary += str(i[0]) + ':' + str(i[1:]) + '\n'
#         else:
#             summary += str(i[0]) + '\n'
#     f.write(summary)
