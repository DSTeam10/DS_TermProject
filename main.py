# heatmap 으로 attribute 간의 상관관계

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# read csv
data01 = pd.read_csv('merge01.csv')
data02 = pd.read_csv('merge02.csv')
data03 = pd.read_csv('merge03.csv')
data04 = pd.read_csv('merge04.csv')

# feature: 고지혈증,당뇨병 의 병의 여부와 음주 강도
# target: 헤모글로빈, 혈압 등 수치

# data01 에 대한 feature, target 분리
features = ['T01_DRINK', 'T01_TAKAM', 'T01_RICEAM', 'T01_WINEAM', 'T01_SOJUAM', 'T01_BEERAM',
            'T01_HLIQAM', 'T01_SMAM', 'T01_TAKFQ','T01_RICEFQ', 'T01_WINEFQ', 'T01_SOJUFQ',
            'T01_BEERFQ', 'T01_HLIQFQ', 'T01_SMOKE', 'T01_HTN', 'T01_DM', 'T01_LIP', 'T02_DRINK',
            'T02_TAKAM', 'T02_RICEAM', 'T02_WINEAM', 'T02_SOJUAM', 'T02_BEERAM', 'T02_HLIQAM',
            'T02_SMAM', 'T02_TAKFQ', 'T02_RICEFQ', 'T02_WINEFQ', 'T02_SOJUFQ', 'T02_BEERFQ',
            'T02_HLIQFQ', 'T02_SMOKE', 'T02_HTN', 'T02_DM', 'T02_LIP']
target = ['T01_SBP', 'T01_DBP', 'T01_HBA1C', 'T01_GLU0', 'T01_TCHL', 'T01_HDL',
          'T02_SBP', 'T02_DBP', 'T02_HBA1C', 'T02_GLU0', 'T02_TCHL', 'T02_HDL']

x, y = data01[features], data01[target]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, shuffle=True)