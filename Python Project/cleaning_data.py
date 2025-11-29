# %%
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
df = sns.load_dataset("titanic")
print(df.isnull().sum())
print(df['sex'].unique())
df.drop(columns=["deck"],inplace=True)
df['age'].fillna(df['age'].mean(),inplace=True)
df['embarked'].fillna('S', inplace=True)
df['embark_town'].fillna('Southampton', inplace=True)
print(df.head(10))
print(df.tail(10))
print(df.info())
print(df.describe())
plt.hist(df['age'])
plt.show()

plt.scatter(df['age'], df['fare'])
plt.show()

plt.plot(df['age'][:50])
plt.show()

sns.boxplot(x=df['age'])
plt.show()

sns.countplot(x=df['class'])
plt.show()

sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.show()

plt.title("Distribution of Age")
plt.xlabel("Age")
plt.ylabel("Count")

plt.figure(figsize=(10,5))
sns.histplot(df['age'])
plt.show()

fig, axs = plt.subplots(1, 2, figsize=(12, 4))

sns.histplot(df['age'], ax=axs[0])
sns.boxplot(x=df['age'], ax=axs[1])

plt.show()





