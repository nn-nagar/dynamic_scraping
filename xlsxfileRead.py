import pandas as pd


data = pd.read_excel (r'C:\Users\hp\Desktop\asco\test 1.xlsx')
df = pd.DataFrame(data, columns= ['Name'])
#df.list()
print (df)
