
import os
import numpy as np
import pandas as pd
from fleiss import fleissKappa


annotator1label = []
annotator2label = []
annotator3label = []


for resuroot, resudirs, resufiles in os.walk("./DataSet/annotator1/"):
    for file_j in resufiles:
        data_result = pd.read_csv('./DataSet/annotator1/'+str(file_j), sep='\t', delimiter="\t", encoding='ISO-8859-1')
        for labelj in data_result.label:
            annotator1label.append(labelj)
            if labelj == 13:
                print('a 13 in annotator1/' + str(file_j))

            # print(i)
            # print(data_result.label[0])

for resuroot, resudirs, resufiles in os.walk("./DataSet/annotator2/"):
    for file_j in resufiles:
        data_result = pd.read_csv('./DataSet/annotator2/' + str(file_j), sep='\t', delimiter="\t", encoding='ISO-8859-1')
        for labelj in data_result.label:
            annotator2label.append(labelj)
            if labelj == 13:
                print('a 13 in annotator2/' + str(file_j))

        # for line in data_result:
        #     annotator2label.append(line[0])

for resuroot, resudirs, resufiles in os.walk("./DataSet/annotator3/"):
    for file_j in resufiles:
        data_result = pd.read_csv('./DataSet/annotator3/' + str(file_j), sep='\t', delimiter="\t", encoding='ISO-8859-1')
        for labelj in data_result.label:
            annotator3label.append(labelj)
            if labelj == 13:
                print('a 13 in annotator3/' + str(file_j))

        # for line in data_result:
        #     annotator3label.append(line[0])

if len(annotator1label) == len(annotator2label) == len(annotator3label):
    datalen = len(annotator1label)
    print(str(len(annotator3label)) + " data")
else:
    print("error! 3 datasets are not equal")

# make 13 labels into 11
for idx in range(datalen):
    if annotator1label[idx] == 2:
        annotator1label[idx] = 0
    if annotator1label[idx] == 6:
        annotator1label[idx] = 5
    if annotator1label[idx] > 6:
        annotator1label[idx] -= 1
    if annotator1label[idx] > 2:
        annotator1label[idx] -= 1

    if annotator2label[idx] == 2:
        annotator2label[idx] = 0
    if annotator2label[idx] == 6:
        annotator2label[idx] = 5
    if annotator2label[idx] > 6:
        annotator2label[idx] -= 1
    if annotator2label[idx] > 2:
        annotator2label[idx] -= 1

    if annotator3label[idx] == 2:
        annotator3label[idx] = 0
    if annotator3label[idx] == 6:
        annotator3label[idx] = 5
    if annotator3label[idx] > 6:
        annotator3label[idx] -= 1
    if annotator3label[idx] > 2:
        annotator3label[idx] -= 1


Arraybuyizhi = [0 for i in range(datalen)]

buyizhichecklabel = 4

# take 3 annotator result into an array
kappaArray = [[0 for i in range(11)] for j in range(datalen)]
for index in range(datalen):
    kappaArray[index][annotator1label[index]] += 1
    kappaArray[index][annotator2label[index]] += 1
    kappaArray[index][annotator3label[index]] += 1

    if kappaArray[index][buyizhichecklabel] > 0 and kappaArray[index][buyizhichecklabel] < 3:
        Arraybuyizhi[index] = 1

print(Arraybuyizhi.count(1))



labelnum = 0
for resuroot, resudirs, resufiles in os.walk("./DataSet/annotator3/"):
    for file_j in resufiles:
        data_result = pd.read_csv('./DataSet/annotator3/' + str(file_j), sep='\t', delimiter="\t", encoding='ISO-8859-1')
        for labelj in data_result.sentence:

            if Arraybuyizhi[labelnum] == 1:
                print(labelj)
            labelnum += 1

print(labelnum)