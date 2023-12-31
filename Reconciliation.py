#This is a sheet for reconciliation
import pandas as pd 
import numpy as np

def compare_spreadsheet(filepath): 
    df = pd.read_excel(filepath, sheet_name=None) 
    df1 = df["logistics"] 
    df2 = df["warehouse"] 
    comparison_values = df1.eq(df2) 
    rows,cols=np.where(comparison_values==False)
    post = []
    for i in range(len(rows)):
        post.append([rows[i], cols[i]])
    for i in range(len(post)):
	    df1.iloc[post[i][0], post[i][1]] = '{} --> {}'.format(df1.iloc[post[i][0], post[i][1]],df2.iloc[post[i][0], post[i][1]]) 
    print(df1.head())

compare_spreadsheet("C:/Users/840/Desktop/Real_compare.xlsx")

