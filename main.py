from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV, KFold, RandomizedSearchCV
import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split

# setting show all col
pd.set_option('display.max_columns', None)

data = pd.read_csv('total dataset_cleaned_edit.csv')

# Remove column
# T00_ID, T00_DATA_CLASS, and T01_EDATE are to be excluded from scaling
data = data.iloc[:,3:]

# cleaning data
# Fill missing values with mean column values in the df
data.fillna(data.mean(), inplace=True)

# Change data type from object to float
data = data.apply(pd.to_numeric, errors='coerce').fillna(0)

# feature - Blood health indicators
feature_list = ['T01_SBP', 'T01_DBP', 'T01_HBA1C', 'T01_GLU0', 'T01_TCHL', 'T01_HDL']
x = data[['T01_SBP', 'T01_DBP', 'T01_HBA1C', 'T01_GLU0',
                  'T01_TCHL', 'T01_HDL']]
# target - Categorical data for drink (FQ)
target_list = ['T01_DRINK', 'T01_TAKFQ', 'T01_RICEFQ', 'T01_WINEFQ', 'T01_BEERFQ', 'T01_HLIQFQ']

# define GridSearchCV parameters
param_grid = [{
    'weights':["uniform", "distance"],
    'metric' : ['euclidean', 'manhattan', 'minkowski'],
    'n_neighbors' : list(range(1,20)),
}]

# definition : function with encoder, All scaling and knn, It calculate best scaling auto.
# input : dataset, independent feature, target feature, test size
# return : void
def AutoFunction(data, feature, target, test_size):
    x = data[feature]
    y = data[target]

    # ******************************** Ordinal encoding and onehot encoding ********************************
    print("\n〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓 Target : {} 〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓".format(target))
    print("\n────────────────────────────────────── OrdinalEncoding ──────────────────────────────────────")
    enc = preprocessing.OrdinalEncoder()
    enc_result_ordinal = enc.fit_transform(y.to_numpy().reshape(-1,1))

    # Split the dataset
    # x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=test_size)
    x_train, x_test, y_train, y_test = train_test_split(x, enc_result_ordinal.ravel(), test_size=test_size)

    # Scaling
    x_train_robust, x_test_robust, x_train_standard, x_test_standard, x_train_min_max, x_test_min_max, x_train_max_abs, x_test_max_abs = getScaling(x_train, x_test)

    # get Accuracy
    ac_train_robust_grid, ac_train_robust_rand, ac_test_robust = getAccuracy(x_train_robust, y_train, x_test_robust, y_test,'Robust Scaling')
    ac_train_standard_grid, ac_train_standard_rand, ac_test_standard = getAccuracy(x_train_standard, y_train, x_test_standard, y_test,'Standard Scaling')
    ac_train_min_max_grid, ac_train_min_max_rand, ac_test_min_max = getAccuracy(x_train_min_max, y_train, x_test_min_max, y_test,'MinMax Scaling')
    ac_train_max_abs_grid, ac_train_max_abs_rand, ac_test_max_abs = getAccuracy(x_train_max_abs, y_train, x_test_max_abs, y_test,'MaxAbs Scaling')
    # print Accuracy
    # print("ac_train_robust : {}, ac_test_robust : {}".format(ac_train_robust, ac_test_robust))
    # print("ac_train_standard : {}, ac_test_standard : {}".format(ac_train_standard, ac_test_standard))
    # print("ac_train_max_abs : {}, ac_test_max_abs : {}".format(ac_train_max_abs, ac_test_max_abs))
    print("\n┌────────────────────────────────── Best Score ──────────────────────────────────┐")
    print("(TRAIN SETS) Robust Scaling 'GridSearch CV' best score : ({})".format(ac_train_robust_grid))
    print("(TRAIN SETS) Robust Scaling 'Randomized CV' best score : ({})".format(ac_train_robust_rand))

    print("(TRAIN SETS) Standard Scaling 'GridSearch CV' best score : ({})".format(ac_train_standard_grid))
    print("(TRAIN SETS) Standard Scaling 'Randomized CV' best score : ({})".format(ac_train_standard_rand))

    print("(TRAIN SETS) MinMax Scaling 'GridSearch CV' best score : ({})".format(ac_train_min_max_grid))
    print("(TRAIN SETS) MinMax Scaling 'Randomized CV' best score : ({})".format(ac_train_min_max_rand))

    print("(TRAIN SETS) MaxAbs Scaling 'GridSearch CV' best score : ({})".format(ac_train_max_abs_grid))
    print("(TRAIN SETS) MaxAbs Scaling 'Randomized CV' best score : ({})".format(ac_train_max_abs_rand))


    result_accuray_test = [ac_test_robust, ac_test_standard, ac_test_min_max, ac_test_max_abs]
    # Index of the most accurate values
    index = result_accuray_test.index(max(result_accuray_test))
    if index == 0:
        print("(TEST SETS) Robust scaling is best score : ({})".format(max(result_accuray_test)))
    if index == 1:
        print("(TEST SETS) Standard scaling is best score : {})".format(max(result_accuray_test)))
    if index == 2:
        print("(TEST SETS) MinMax scaling is best score : ({})".format(max(result_accuray_test)))
    if index == 3:
        print("(TEST SETS) MaxAbs scaling is best score : ({})".format(max(result_accuray_test)))

    # --------------------------------------------------------------------------------------------------

    print("\n────────────────────────────────────── OneHotEncoding ──────────────────────────────────────")
    enc = preprocessing.OneHotEncoder()
    enc_result_one_hot = enc.fit_transform(y.to_numpy().reshape(-1,1)).toarray()
    # Split the dataset
    # x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=test_size)
    x_train, x_test, y_train, y_test = train_test_split(x, enc_result_ordinal.ravel(), test_size=test_size)

    # Scaling
    x_train_robust, x_test_robust, x_train_standard, x_test_standard, x_train_min_max, x_test_min_max, x_train_max_abs, x_test_max_abs = getScaling(
        x_train, x_test)
    # get Accuracy
    ac_train_robust_grid, ac_train_robust_rand, ac_test_robust = getAccuracy(x_train_robust, y_train, x_test_robust,
                                                                             y_test,'Robust Scaling')
    ac_train_standard_grid, ac_train_standard_rand, ac_test_standard = getAccuracy(x_train_standard, y_train,
                                                                                   x_test_standard, y_test,'Standard Scaling')
    ac_train_min_max_grid, ac_train_min_max_rand, ac_test_min_max = getAccuracy(x_train_min_max, y_train,
                                                                                x_test_min_max, y_test,'MinMax Scaling')
    ac_train_max_abs_grid, ac_train_max_abs_rand, ac_test_max_abs = getAccuracy(x_train_max_abs, y_train,
                                                                                x_test_max_abs, y_test,'MaxAbs Scaling')
    # print Accuracy
    # print("ac_train_robust : {}, ac_test_robust : {}".format(ac_train_robust, ac_test_robust))
    # print("ac_train_standard : {}, ac_test_standard : {}".format(ac_train_standard, ac_test_standard))
    # print("ac_train_max_abs : {}, ac_test_max_abs : {}".format(ac_train_max_abs, ac_test_max_abs))
    print("\n┌────────────────────────────────── Best Score ──────────────────────────────────┐")
    print("(TRAIN SETS) Robust Scaling 'GridSearch CV' best score : ({})".format(ac_train_robust_grid))
    print("(TRAIN SETS) Robust Scaling 'Randomized CV' best score : ({})".format(ac_train_robust_rand))

    print("(TRAIN SETS) Standard Scaling 'GridSearch CV' best score : ({})".format(ac_train_standard_grid))
    print("(TRAIN SETS) Standard Scaling 'Randomized CV' best score : ({})".format(ac_train_standard_rand))

    print("(TRAIN SETS) MinMax Scaling 'GridSearch CV' best score : ({})".format(ac_train_min_max_grid))
    print("(TRAIN SETS) MinMax Scaling 'Randomized CV' best score : ({})".format(ac_train_min_max_rand))

    print("(TRAIN SETS) MaxAbs Scaling 'GridSearch CV' best score : ({})".format(ac_train_max_abs_grid))
    print("(TRAIN SETS) MaxAbs Scaling 'Randomized CV' best score : ({})".format(ac_train_max_abs_rand))

    result_accuray_test = [ac_test_robust, ac_test_standard, ac_test_min_max, ac_test_max_abs]
    # Index of the most accurate values
    index = result_accuray_test.index(max(result_accuray_test))
    if index == 0:
        print("(TEST SETS) Robust scaling is best score ({})".format(max(result_accuray_test)))
    if index == 1:
        print("(TEST SETS) Standard scaling is best score {})".format(max(result_accuray_test)))
    if index == 2:
        print("(TEST SETS) MinMax scaling is best score ({})".format(max(result_accuray_test)))
    if index == 3:
        print("(TEST SETS) MaxAbs scaling is best score ({})".format(max(result_accuray_test)))

# definition : return all scaling object (Robust, Standard, MinMax, MaxAbs)
# input : x_train, x_test
# return : x_train_robust, x_test_robust, x_train_standard, x_test_standard, x_train_min_max, x_test_min_max, x_train_max_abs, x_test_max_abs
def getScaling(x_train, x_test):
    ########### Robust scaling ############
    scaler = preprocessing.RobustScaler()
    scaler.fit(x_train)
    robust_scaled_train = scaler.transform(x_train)
    robust_scaled_test = scaler.transform(x_test)

    # numpy to dataframe
    x_train_robust = pd.DataFrame(robust_scaled_train)
    x_test_robust = pd.DataFrame(robust_scaled_test)

    ########### Standard scaling ############
    scaler = preprocessing.StandardScaler()
    scaler.fit(x_train)
    standard_scaled_train = scaler.transform(x_train)
    standard_scaled_test = scaler.transform(x_test)

    # numpy to dataframe
    x_train_standard = pd.DataFrame(standard_scaled_train)
    x_test_standard = pd.DataFrame(standard_scaled_test)

    ########### MinMax scaling ############
    scaler = preprocessing.MinMaxScaler()
    scaler.fit(x_train)
    min_max_scaled_train = scaler.transform(x_train)
    min_max_scaled_test = scaler.transform(x_test)

    # numpy to dataframe
    x_train_min_max = pd.DataFrame(min_max_scaled_train)
    x_test_min_max = pd.DataFrame(min_max_scaled_test)

    ########### MaxAbs scaling ############
    scaler = preprocessing.MaxAbsScaler()
    scaler.fit(x_train)
    max_abs_scaled_train = scaler.transform(x_train)
    max_abs_scaled_test = scaler.transform(x_test)

    # numpy to dataframe
    x_train_max_abs = pd.DataFrame(max_abs_scaled_train)
    x_test_max_abs = pd.DataFrame(max_abs_scaled_test)

    return x_train_robust, x_test_robust, x_train_standard, x_test_standard, x_train_min_max, x_test_min_max, x_train_max_abs, x_test_max_abs

# definition : get accuracy each of scaling
# input : x_train,y_train,x_test,y_test,n_neighbors, current scaling name
# return : Train accuracy and Test accuracy
def getAccuracy(x_train,y_train,x_test,y_test,scale_name):
    # Kfold for KNN
    # prepare the cross-validation procedure
    kfold = KFold(n_splits=5, shuffle=True, random_state=1)

    y_train = y_train.astype('int')
    knn = KNeighborsClassifier()
    knn.fit(x_train, y_train)

    # Values predicted by the test set
    y_predict = knn.predict(x_test)

    # grid-search
    grid_search = GridSearchCV(knn, param_grid, cv=kfold, verbose=1, n_jobs=-1)
    grid_search.fit(x_train, y_train)
    print("\n┌───────────────────── {} ─────────────────────┐".format(scale_name))
    print("\n│               GridSearchCV's best params                 │")
    print(grid_search.best_params_)

    # randomized-search
    randomized_search = RandomizedSearchCV(knn, param_grid, cv=kfold, verbose=1, n_jobs=-1)
    randomized_search.fit(x_train, y_train)
    print("\n│               RandomizedSearch CV's best params          │")
    print(randomized_search.best_params_)

    # return knn.score(x_train, y_train), np.mean(y_predict == y_test)
    return grid_search.best_score_, randomized_search.best_score_, np.mean(y_predict == y_test)

# Assign each one in the target list as the target of AutoFunction
for idx, target in enumerate(target_list):
    AutoFunction(data, feature_list, target, 0.2)
