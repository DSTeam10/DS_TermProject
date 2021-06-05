import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('total dataset_cleaned_edit.csv')

# Fill missing values with mean column values in the df
data.fillna(0, inplace=True)

data = data.apply(pd.to_numeric, errors='coerce').fillna(0)

data_temp = data[['T01_DRINK', 'T01_TAKAM', 'T01_RICEAM', 'T01_WINEAM', 'T01_SOJUAM', 'T01_BEERAM',
            'T01_HLIQAM', 'T01_SMAM', 'T01_TAKFQ','T01_RICEFQ', 'T01_WINEFQ', 'T01_SOJUFQ',
            'T01_BEERFQ', 'T01_HLIQFQ', 'T01_SMOKE', 'T01_SBP']]

smoke_data1 = data[data['T01_SMOKE'] == 1]
smoke_data2 = data[data['T01_SMOKE'] == 2]
smoke_data3 = data[data['T01_SMOKE'] == 3]
print("smoke_data #1 : {}".format(smoke_data1))
print("smoke_data #2 : {}".format(smoke_data2))
print("smoke_data #3 : {}".format(smoke_data3))
# systolic blood pressure
smoke_data1_SBP = smoke_data1['T01_SBP'].mean()
smoke_data2_SBP = smoke_data2['T01_SBP'].mean()
smoke_data3_SBP = smoke_data3['T01_SBP'].mean()
# Relaxed blood pressure
smoke_data1_DBP = smoke_data1['T01_DBP'].mean()
smoke_data2_DBP = smoke_data2['T01_DBP'].mean()
smoke_data3_DBP = smoke_data3['T01_DBP'].mean()
# Hemoglobin levels
smoke_data1_HBA1C = smoke_data1['T01_HBA1C'].mean()
smoke_data2_HBA1C = smoke_data2['T01_HBA1C'].mean()
smoke_data3_HBA1C = smoke_data3['T01_HBA1C'].mean()
# Glucose
smoke_data1_GLUO = smoke_data1['T01_GLU0'].mean()
smoke_data2_GLUO = smoke_data2['T01_GLU0'].mean()
smoke_data3_GLUO = smoke_data3['T01_GLU0'].mean()
# cholesterol
smoke_data1_TCHL = smoke_data1['T01_TCHL'].mean()
smoke_data2_TCHL = smoke_data2['T01_TCHL'].mean()
smoke_data3_TCHL = smoke_data3['T01_TCHL'].mean()
# HDL cholesterol
smoke_data1_HDL = smoke_data1['T01_HDL'].mean()
smoke_data2_HDL = smoke_data2['T01_HDL'].mean()
smoke_data3_HDL = smoke_data3['T01_HDL'].mean()

# Value Verification Code
print("smoke_data1_SBP : {}, smoke_data2_SBP : {}, smoke_data3_SBP : {} ".format(smoke_data1_SBP,smoke_data2_SBP,smoke_data3_SBP))
print("smoke_data1_DBP : {}, smoke_data2_DBP : {}, smoke_data3_DBP : {} ".format(smoke_data1_DBP,smoke_data2_DBP,smoke_data3_DBP))
print("smoke_data1_HBA1C : {}, smoke_data2_HBA1C : {}, smoke_data3_HBA1C : {} ".format(smoke_data1_HBA1C,smoke_data2_HBA1C,smoke_data3_HBA1C))
print("smoke_data1_GLUO : {}, smoke_data2_GLUO : {}, smoke_data3_GLUO : {} ".format(smoke_data1_GLUO,smoke_data2_GLUO,smoke_data3_GLUO))
print("smoke_data1_TCHL : {}, smoke_data2_TCHL : {}, smoke_data3_TCHL : {} ".format(smoke_data1_TCHL,smoke_data2_TCHL,smoke_data3_TCHL))
print("smoke_data1_HDL : {}, smoke_data2_HDL : {}, smoke_data3_HDL : {} ".format(smoke_data1_HDL,smoke_data2_HDL,smoke_data3_HDL))

# Showing a tendency to lower HDL cholesterol levels.
plt.hist(smoke_data1['T01_HDL'], color='green',bins=50, density=True, alpha=0.7, histtype='stepfilled',label="smoke#1")
plt.title("Non-smoker HDL Value")
plt.show()

plt.hist(smoke_data2['T01_HDL'], color='red',bins=50, density=True, alpha=0.5, histtype='stepfilled',label="smoke#3")
plt.title("Formal-smoker HDL Value")
plt.show()

plt.hist(smoke_data3['T01_HDL'], color='black',bins=50, density=True, alpha=0.9, histtype='stepfilled',label="smoke#3")
plt.title("Regular-smoker HDL Value")
plt.show()

# Hemoglobin levels also show a tendency to increase
plt.scatter([1,2,3],[smoke_data1_HBA1C,smoke_data2_HBA1C,smoke_data3_HBA1C],edgecolors='black',linewidths=3)
line = plt.plot([1,2,3],[smoke_data1_HBA1C,smoke_data2_HBA1C,smoke_data3_HBA1C])
plt.setp(line, color='r', linewidth=3.0)
plt.title("Smoker HBA1C Value")
plt.show()