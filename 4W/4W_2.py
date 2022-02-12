import pandas as pd

Data1 = [['cherry', 'Fruit', 100], ['mango', 'Fruit', 110], ['potato', 'Vegetable', 60], ['onion', 'Vegetable', 80]]
Data2 = [['pepper', 'Vegetable', 50], ['carrot', 'Vegetable', 70], ['banana', 'Fruit', 90], ['kiwi', 'Fruit', 120]]
df1 = pd.DataFrame(Data1, columns=["name", "Type", "Price"])
df2 = pd.DataFrame(Data2, columns=["name", "Type", "Price"])
df3 = pd.concat([df1, df2])

df_fruit = df3.loc[df3['Type'] == 'Fruit'].sort_values(by="Price", ascending=False)
df_veg = df3.loc[df3['Type'] == 'Vegetable'].sort_values(by="Price", ascending=False)

print("Sum of Top 2 Fruit Price : ", sum(df_fruit[:2]["Price"]))
print("Sum of Top 2 Vegetable Price : ", sum(df_veg[:2]["Price"]))