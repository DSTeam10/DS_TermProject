import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('total dataset_cleaned_edit.csv')

# Fill missing values with mean column values in the df
data.fillna(0, inplace=True)

data = data.apply(pd.to_numeric, errors='coerce').fillna(0)

data_temp = data[['T01_DRINK', 'T01_TAKAM', 'T01_RICEAM', 'T01_WINEAM', 'T01_SOJUAM', 'T01_BEERAM',
                  'T01_HLIQAM', 'T01_SMAM', 'T01_TAKFQ','T01_RICEFQ', 'T01_WINEFQ', 'T01_SOJUFQ',
                  'T01_BEERFQ', 'T01_HLIQFQ', 'T01_HTN', 'T01_DM', 'T01_LIP']]

data_temp_new = data[['T01_DRINK', 'T01_SOJUFQ', 'T01_AST', 'T01_ALT']]

drink_data1 = data[data['T01_DRINK'] == 1]
drink_data2 = data[data['T01_DRINK'] == 2]
drink_data3 = data[data['T01_DRINK'] == 3]
print("drink_data #1 : {}".format(drink_data1))
print("drink_data #2 : {}".format(drink_data2))
print("drink_data #3 : {}".format(drink_data3))
# Systolic blood pressure
drink_data1_SBP = drink_data1['T01_SBP'].mean()
drink_data2_SBP = drink_data2['T01_SBP'].mean()
drink_data3_SBP = drink_data3['T01_SBP'].mean()
# Diastolic blood pressure
drink_data1_DBP = drink_data1['T01_DBP'].mean()
drink_data2_DBP = drink_data2['T01_DBP'].mean()
drink_data3_DBP = drink_data3['T01_DBP'].mean()
# Hemoglobin level
drink_data1_HBA1C = drink_data1['T01_HBA1C'].mean()
drink_data2_HBA1C = drink_data2['T01_HBA1C'].mean()
drink_data3_HBA1C = drink_data3['T01_HBA1C'].mean()
# Glucose
drink_data1_GLUO = drink_data1['T01_GLU0'].mean()
drink_data2_GLUO = drink_data2['T01_GLU0'].mean()
drink_data3_GLUO = drink_data3['T01_GLU0'].mean()
# Cholesterol
drink_data1_TCHL = drink_data1['T01_TCHL'].mean()
drink_data2_TCHL = drink_data2['T01_TCHL'].mean()
drink_data3_TCHL = drink_data3['T01_TCHL'].mean()
# HDL cholesterol
drink_data1_HDL = drink_data1['T01_HDL'].mean()
drink_data2_HDL = drink_data2['T01_HDL'].mean()
drink_data3_HDL = drink_data3['T01_HDL'].mean()
# AST
drink_data1_AST = drink_data1['T01_AST'].mean()
drink_data2_AST = drink_data2['T01_AST'].mean()
drink_data3_AST = drink_data3['T01_AST'].mean()
# ALT
drink_data1_ALT = drink_data1['T01_ALT'].mean()
drink_data2_ALT = drink_data2['T01_ALT'].mean()
drink_data3_ALT = drink_data3['T01_ALT'].mean()

# Value check code
print("drink_data1_SBP : {}, drink_data2_SBP : {}, drink_data3_SBP : {} ".format(drink_data1_SBP,drink_data2_SBP,drink_data3_SBP))
print("drink_data1_DBP : {}, drink_data2_DBP : {}, drink_data3_DBP : {} ".format(drink_data1_DBP,drink_data2_DBP,drink_data3_DBP))
print("drink_data1_HBA1C : {}, drink_data2_HBA1C : {}, drink_data3_HBA1C : {} ".format(drink_data1_HBA1C,drink_data2_HBA1C,drink_data3_HBA1C))
print("drink_data1_GLUO : {}, drink_data2_GLUO : {}, drink_data3_GLUO : {} ".format(drink_data1_GLUO,drink_data2_GLUO,drink_data3_GLUO))
print("drink_data1_TCHL : {}, drink_data2_TCHL : {}, drink_data3_TCHL : {} ".format(drink_data1_TCHL,drink_data2_TCHL,drink_data3_TCHL))
print("drink_data1_HDL : {}, drink_data2_HDL : {}, drink_data3_HDL : {} ".format(drink_data1_HDL,drink_data2_HDL,drink_data3_HDL))
print("drink_data1_AST : {}, drink_data2_AST : {}, drink_data3_AST : {} ".format(drink_data1_AST,drink_data2_AST,drink_data3_AST))
print("drink_data1_ALT : {}, drink_data2_ALT : {}, drink_data3_ALT : {} ".format(drink_data1_ALT,drink_data2_ALT,drink_data3_ALT))
# AST and ALT increase steadily

# Showing the trend of lowering HDL
plt.hist(drink_data1['T01_HDL'], color='green',bins=50, density=True, alpha=0.7, histtype='stepfilled',label="drink#1")
plt.title("Non-drinker HDL Value")
plt.show()

plt.hist(drink_data2['T01_HDL'], color='red',bins=50, density=True, alpha=0.5, histtype='stepfilled',label="drink#3")
plt.title("Formal-drinker HDL Value")
plt.show()

plt.hist(drink_data3['T01_HDL'], color='black',bins=50, density=True, alpha=0.9, histtype='stepfilled',label="drink#3")
plt.title("Regular-drinker HDL Value")
plt.show()

# Shows an increase in hemoglobin levels
plt.scatter([1,2,3],[drink_data1_HBA1C,drink_data2_HBA1C,drink_data3_HBA1C],edgecolors='black',linewidths=3)
line = plt.plot([1,2,3],[drink_data1_HBA1C,drink_data2_HBA1C,drink_data3_HBA1C])
plt.setp(line, color='r', linewidth=3.0)
plt.title("drinker HBA1C Value")
plt.show()