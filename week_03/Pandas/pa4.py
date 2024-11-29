import pandas as pd

names=pd.Series(['Asha','Ashok','Anupama','Akash'])

ages=pd.Series([19,22,21,20])
branches=pd.Series(['CSE','AIML','ISE','ECE'])

data={'Name': names,'Age':ages,'Branch':branches}

studentf1=pd.DataFrame(data)

print(studentf1[:,:3])
print(studentf1[:-2,:3])