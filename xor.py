from sklearn import svm
import pandas as pd


xor_data = [
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]


df = pd.DataFrame(xor_data)


# print ("head\t", df.head)
# print ("columns\t", list(df.columns))
# print ("shape\t", df.shape)
# print ("length\t" , len(df.index))


clf = svm.SVC(gamma='auto')   
clf.fit(df.loc[:, 0:1], df.loc[:, 2])