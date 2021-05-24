import pandas as pd

# read data
raw01 = pd.read_csv('follow_01_data.csv')
raw02 = pd.read_csv('follow_02_data.csv')
raw03 = pd.read_csv('follow_03_data.csv')
raw04 = pd.read_csv('follow_04_data.csv')
raw05 = pd.read_csv('follow_05_data.csv')

# 공통 T00_ID 기준으로 merge (두 데이터에 T00_ID가 모두 존재해야함)
# merge data01 and data02
merge1 = pd.merge(raw01, raw02, on='T00_ID')
merge1.set_index('T00_ID', inplace=True)

merge1.to_csv('merge01.csv')

# merge data02 and data03
merge2 = pd.merge(raw02, raw03, on='T00_ID')
merge2.set_index('T00_ID', inplace=True)

merge2.to_csv('merge02.csv')

# merge data03 and data04
merge3 = pd.merge(raw03, raw04, on='T00_ID')
merge3.set_index('T00_ID', inplace=True)

merge3.to_csv('merge03.csv')

# merge data04 and data05
merge4 = pd.merge(raw04, raw05, on='T00_ID')
merge4.set_index('T00_ID', inplace=True)

merge4.to_csv('merge04.csv')