import pandas as pd
dataframe=pd.read_excel("C:/Users/hrutu/Desktop/records.xlsx",index_col=False)
dataframe.reset_index()
print(dataframe)
