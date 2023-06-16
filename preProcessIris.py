import pandas as pd

df = pd.read_csv("iris.data", header=None)
print(df)

labelMap = {"Iris-setosa" : 1, "Iris-versicolor" : 2, "Iris-virginica" : 3}

df = df.replace({4 : labelMap})

print(df)

df[4], df[0] = df[0], df[4]

print(df)

df.to_csv("Iris_Processed.csv", header=False, index=False)