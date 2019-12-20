
import os
import numpy as np
import pandas as pd
from fleiss import fleissKappa


annotator1label = []
annotator2label = []
annotator3label = []


for resuroot, resudirs, resufiles in os.walk("./DataSet/writeannotator1/"):
    for file_j in resufiles:
        data_result = pd.read_csv('./DataSet/writeannotator1/'+str(file_j), sep='\t', delimiter="\t", encoding='ISO-8859-1')
        for labelj in data_result.label:
            annotator1label.append(labelj)

            if labelj == 13:
                print('a 13 in annotator1/' + str(file_j))
        print(len(data_result.label))
            # print(i)
            # print(data_result.label[0])

for resuroot, resudirs, resufiles in os.walk("./DataSet/writeannotator2/"):
    for file_j in resufiles:
        data_result = pd.read_csv('./DataSet/writeannotator2/' + str(file_j), sep='\t', delimiter="\t", encoding='ISO-8859-1')
        for labelj in data_result.label:
            annotator2label.append(labelj)
            if labelj == 13:
                print('a 13 in annotator2/' + str(file_j))
        print(len(data_result.label))

        # for line in data_result:
        #     annotator2label.append(line[0])

for resuroot, resudirs, resufiles in os.walk("./DataSet/writeannotator3/"):
    for file_j in resufiles:
        data_result = pd.read_csv('./DataSet/writeannotator3/' + str(file_j), sep='\t', delimiter="\t", encoding='ISO-8859-1')
        for labelj in data_result.label:
            annotator3label.append(labelj)
            if labelj == 13:
                print('a 13 in annotator3/' + str(file_j))
        print(len(data_result.label))

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




# take 3 annotator result into an array
kappaArray = [[0 for i in range(11)] for j in range(datalen)]
for index in range(datalen):
    kappaArray[index][annotator1label[index]] += 1
    kappaArray[index][annotator2label[index]] += 1
    kappaArray[index][annotator3label[index]] += 1


# calculate each label kappa
labelnum = 10
binarykappa = [[0 for i in range(2)] for j in range(datalen)]
for index in range(datalen):
    binarykappa[index][0] = kappaArray[index][labelnum]
    binarykappa[index][1] = 3 - kappaArray[index][labelnum]

    # binarykappa[index][0] = kappaArray[index][1] + kappaArray[index][3]
    # binarykappa[index][1] = 3 - binarykappa[index][0]

# kappa = fleissKappa(kappaArray,3)
kappa = fleissKappa(binarykappa, 3)
print(kappa)


# for resuroot, resudirs, resufiles in os.walk("./DataSet/annotator3/"):
#     for file_j in resufiles:
#         with open('./DataSet/annotator3/'+str(file_j), 'r+', encoding='ISO-8859-1') as f:
#             content = f.read()
#             f.seek(0, 0)
#             f.write('label\tsentence\n'+content)