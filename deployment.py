# Change drinking level to frequency
data_drink = data.replace({'T01_DRINK': {1: 0, 2: 1, 3: 2}})

# LIB patient data
# Height ~150cm
H140W40_LIB_mean = data_drink[(data_drink['T01_LIP'] == 2) & (150 > data_drink['T01_HEIGHT'])
                        & (50 > data_drink['T01_WEIGHT'])]
H140W50_LIB_mean = data_drink[(data_drink['T01_LIP'] == 2) & (150 > data_drink['T01_HEIGHT'])
                        & (60 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 50)]
H140W60_LIB_mean = data_drink[(data_drink['T01_LIP'] == 2) & (150 > data_drink['T01_HEIGHT'])
                        & (70 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 60)]
H140W70_LIB_mean = data_drink[(data_drink['T01_LIP'] == 2) & (150 > data_drink['T01_HEIGHT'])
                        & (80 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 70)]
H140W80_LIB_mean = data_drink[(data_drink['T01_LIP'] == 2) & (150 > data_drink['T01_HEIGHT'])
                        & (data_drink['T01_WEIGHT'] >= 80)]

# Height 150cm~160cm
H150W40_LIB_mean = data_drink[(data_drink['T01_LIP'] == 2) & (160 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 150)
                        & (50 > data_drink['T01_WEIGHT'])]
H150W50_LIB_mean = data_drink[(data_drink['T01_LIP'] == 2) & (160 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 150)
                        & (60 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 50)]
H150W60_LIB_mean = data_drink[(data_drink['T01_LIP'] == 2) & (160 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 150)
                        & (70 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 60)]
H150W70_LIB_mean = data_drink[(data_drink['T01_LIP'] == 2) & (160 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 150)
                        & (80 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 70)]
H150W80_LIB_mean = data_drink[(data_drink['T01_LIP'] == 2) & (160 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 150)
                        & (data_drink['T01_WEIGHT'] >= 80)]

# Height 160cm~170cm
H160W40_LIB_mean = data_drink[(data_drink['T01_LIP'] == 2) & (170 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 160)
                        & (50 > data_drink['T01_WEIGHT'])]
H160W50_LIB_mean = data_drink[(data_drink['T01_LIP'] == 2) & (170 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 160)
                        & (60 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 50)]
H160W60_LIB_mean = data_drink[(data_drink['T01_LIP'] == 2) & (170 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 160)
                        & (70 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 60)]
H160W70_LIB_mean = data_drink[(data_drink['T01_LIP'] == 2) & (170 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 160)
                        & (80 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 70)]
H160W80_LIB_mean = data_drink[(data_drink['T01_LIP'] == 2) & (170 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 160)
                        & (data_drink['T01_WEIGHT'] >= 80)]

# Height 170cm~180cm
H170W40_LIB_mean = data_drink[(data_drink['T01_LIP'] == 2) & (180 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 170)
                        & (50 > data_drink['T01_WEIGHT'])]
H170W50_LIB_mean = data_drink[(data_drink['T01_LIP'] == 2) & (180 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 170)
                        & (60 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 50)]
H170W60_LIB_mean = data_drink[(data_drink['T01_LIP'] == 2) & (180 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 170)
                        & (70 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 60)]
H170W70_LIB_mean = data_drink[(data_drink['T01_LIP'] == 2) & (180 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 170)
                        & (80 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 70)]
H170W80_LIB_mean = data_drink[(data_drink['T01_LIP'] == 2) & (180 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 170)
                        & (data_drink['T01_WEIGHT'] >= 80)]

# Height 180cm~
H180W40_LIB_mean = data_drink[(data_drink['T01_LIP'] == 2) & (data_drink['T01_HEIGHT'] >= 180)
                        & (50 > data_drink['T01_WEIGHT'])]
H180W50_LIB_mean = data_drink[(data_drink['T01_LIP'] == 2) & (data_drink['T01_HEIGHT'] >= 180)
                        & (60 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 50)]
H180W60_LIB_mean = data_drink[(data_drink['T01_LIP'] == 2) & (data_drink['T01_HEIGHT'] >= 180)
                        & (70 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 60)]
H180W70_LIB_mean = data_drink[(data_drink['T01_LIP'] == 2) & (data_drink['T01_HEIGHT'] >= 180)
                        & (80 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 70)]
H180W80_LIB_mean = data_drink[(data_drink['T01_LIP'] == 2) & (data_drink['T01_HEIGHT'] >= 180)
                        & (data_drink['T01_WEIGHT'] >= 80)]

# Calculate drink frequency mean
H140W40_LIB_mean = H140W40_LIB_mean['T01_DRINK'].mean()
H140W50_LIB_mean = H140W50_LIB_mean['T01_DRINK'].mean()
H140W60_LIB_mean = H140W60_LIB_mean['T01_DRINK'].mean()
H140W70_LIB_mean = H140W70_LIB_mean['T01_DRINK'].mean()
H140W80_LIB_mean = H140W80_LIB_mean['T01_DRINK'].mean()

H150W40_LIB_mean = H150W40_LIB_mean['T01_DRINK'].mean()
H150W50_LIB_mean = H150W50_LIB_mean['T01_DRINK'].mean()
H150W60_LIB_mean = H150W60_LIB_mean['T01_DRINK'].mean()
H150W70_LIB_mean = H150W70_LIB_mean['T01_DRINK'].mean()
H150W80_LIB_mean = H150W80_LIB_mean['T01_DRINK'].mean()

H160W40_LIB_mean = H160W40_LIB_mean['T01_DRINK'].mean()
H160W50_LIB_mean = H160W50_LIB_mean['T01_DRINK'].mean()
H160W60_LIB_mean = H160W60_LIB_mean['T01_DRINK'].mean()
H160W70_LIB_mean = H160W70_LIB_mean['T01_DRINK'].mean()
H160W80_LIB_mean = H160W80_LIB_mean['T01_DRINK'].mean()

H170W40_LIB_mean = H170W40_LIB_mean['T01_DRINK'].mean()
H170W50_LIB_mean = H170W50_LIB_mean['T01_DRINK'].mean()
H170W60_LIB_mean = H170W60_LIB_mean['T01_DRINK'].mean()
H170W70_LIB_mean = H170W70_LIB_mean['T01_DRINK'].mean()
H170W80_LIB_mean = H170W80_LIB_mean['T01_DRINK'].mean()

H180W40_LIB_mean = H180W40_LIB_mean['T01_DRINK'].mean()
H180W50_LIB_mean = H180W50_LIB_mean['T01_DRINK'].mean()
H180W60_LIB_mean = H180W60_LIB_mean['T01_DRINK'].mean()
H180W70_LIB_mean = H180W70_LIB_mean['T01_DRINK'].mean()
H180W80_LIB_mean = H180W80_LIB_mean['T01_DRINK'].mean()


# HTN patient data
# Height ~150cm
H140W40_HTN_mean = data_drink[(data_drink['T01_HTN'] == 2) & (150 > data_drink['T01_HEIGHT'])
                        & (50 > data_drink['T01_WEIGHT'])]
H140W50_HTN_mean = data_drink[(data_drink['T01_HTN'] == 2) & (150 > data_drink['T01_HEIGHT'])
                        & (60 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 50)]
H140W60_HTN_mean = data_drink[(data_drink['T01_HTN'] == 2) & (150 > data_drink['T01_HEIGHT'])
                        & (70 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 60)]
H140W70_HTN_mean = data_drink[(data_drink['T01_HTN'] == 2) & (150 > data_drink['T01_HEIGHT'])
                        & (80 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 70)]
H140W80_HTN_mean = data_drink[(data_drink['T01_HTN'] == 2) & (150 > data_drink['T01_HEIGHT'])
                       & (data_drink['T01_WEIGHT'] >= 80)]

# Height 150cm~160cm
H150W40_HTN_mean = data_drink[(data_drink['T01_HTN'] == 2) & (160 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 150)
                        & (50 > data_drink['T01_WEIGHT'])]
H150W50_HTN_mean = data_drink[(data_drink['T01_HTN'] == 2) & (160 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 150)
                        & (60 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 50)]
H150W60_HTN_mean = data_drink[(data_drink['T01_HTN'] == 2) & (160 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 150)
                        & (70 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 60)]
H150W70_HTN_mean = data_drink[(data_drink['T01_HTN'] == 2) & (160 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 150)
                        & (80 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 70)]
H150W80_HTN_mean = data_drink[(data_drink['T01_HTN'] == 2) & (160 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 150)
                        & (data_drink['T01_WEIGHT'] >= 80)]

# Height 160cm~170cm
H160W40_HTN_mean = data_drink[(data_drink['T01_HTN'] == 2) & (170 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 160)
                        & (50 > data_drink['T01_WEIGHT'])]
H160W50_HTN_mean = data_drink[(data_drink['T01_HTN'] == 2) & (170 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 160)
                        & (60 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 50)]
H160W60_HTN_mean = data_drink[(data_drink['T01_HTN'] == 2) & (170 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 160)
                        & (70 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 60)]
H160W70_HTN_mean = data_drink[(data_drink['T01_HTN'] == 2) & (170 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 160)
                        & (80 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 70)]
H160W80_HTN_mean = data_drink[(data_drink['T01_HTN'] == 2) & (170 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 160)
                        & (data_drink['T01_WEIGHT'] >= 80)]

# Height 170cm~180cm
H170W40_HTN_mean = data_drink[(data_drink['T01_HTN'] == 2) & (180 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 170)
                        & (50 > data_drink['T01_WEIGHT'])]
H170W50_HTN_mean = data_drink[(data_drink['T01_HTN'] == 2) & (180 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 170)
                        & (60 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 50)]
H170W60_HTN_mean = data_drink[(data_drink['T01_HTN'] == 2) & (180 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 170)
                        & (70 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 60)]
H170W70_HTN_mean = data_drink[(data_drink['T01_HTN'] == 2) & (180 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 170)
                        & (80 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 70)]
H170W80_HTN_mean = data_drink[(data_drink['T01_HTN'] == 2) & (180 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 170)
                        & (data_drink['T01_WEIGHT'] >= 80)]

# Height 180cm~
H180W40_HTN_mean = data_drink[(data_drink['T01_HTN'] == 2) & (data_drink['T01_HEIGHT'] >= 180)
                        & (50 > data_drink['T01_WEIGHT'])]
H180W50_HTN_mean = data_drink[(data_drink['T01_HTN'] == 2) & (data_drink['T01_HEIGHT'] >= 180)
                        & (60 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 50)]
H180W60_HTN_mean = data_drink[(data_drink['T01_HTN'] == 2) & (data_drink['T01_HEIGHT'] >= 180)
                        & (70 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 60)]
H180W70_HTN_mean = data_drink[(data_drink['T01_HTN'] == 2) & (data_drink['T01_HEIGHT'] >= 180)
                        & (80 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 70)]
H180W80_HTN_mean = data_drink[(data_drink['T01_HTN'] == 2) & (data_drink['T01_HEIGHT'] >= 180)
                        & (data_drink['T01_WEIGHT'] >= 80)]

# Calculate drink frequency mean
H140W40_HTN_mean = H140W40_HTN_mean['T01_DRINK'].mean()
H140W50_HTN_mean = H140W50_HTN_mean['T01_DRINK'].mean()
H140W60_HTN_mean = H140W60_HTN_mean['T01_DRINK'].mean()
H140W70_HTN_mean = H140W70_HTN_mean['T01_DRINK'].mean()
H140W80_HTN_mean = H140W80_HTN_mean['T01_DRINK'].mean()

H150W40_HTN_mean = H150W40_HTN_mean['T01_DRINK'].mean()
H150W50_HTN_mean = H150W50_HTN_mean['T01_DRINK'].mean()
H150W60_HTN_mean = H150W60_HTN_mean['T01_DRINK'].mean()
H150W70_HTN_mean = H150W70_HTN_mean['T01_DRINK'].mean()
H150W80_HTN_mean = H150W80_HTN_mean['T01_DRINK'].mean()

H160W40_HTN_mean = H160W40_HTN_mean['T01_DRINK'].mean()
H160W50_HTN_mean = H160W50_HTN_mean['T01_DRINK'].mean()
H160W60_HTN_mean = H160W60_HTN_mean['T01_DRINK'].mean()
H160W70_HTN_mean = H160W70_HTN_mean['T01_DRINK'].mean()
H160W80_HTN_mean = H160W80_HTN_mean['T01_DRINK'].mean()

H170W40_HTN_mean = H170W40_HTN_mean['T01_DRINK'].mean()
H170W50_HTN_mean = H170W50_HTN_mean['T01_DRINK'].mean()
H170W60_HTN_mean = H170W60_HTN_mean['T01_DRINK'].mean()
H170W70_HTN_mean = H170W70_HTN_mean['T01_DRINK'].mean()
H170W80_HTN_mean = H170W80_HTN_mean['T01_DRINK'].mean()

H180W40_HTN_mean = H180W40_HTN_mean['T01_DRINK'].mean()
H180W50_HTN_mean = H180W50_HTN_mean['T01_DRINK'].mean()
H180W60_HTN_mean = H180W60_HTN_mean['T01_DRINK'].mean()
H180W70_HTN_mean = H180W70_HTN_mean['T01_DRINK'].mean()
H180W80_HTN_mean = H180W80_HTN_mean['T01_DRINK'].mean()

# DM patient data
# Height ~150cm
H140W40_DM_mean = data_drink[(data_drink['T01_DM'] == 2) & (150 > data_drink['T01_HEIGHT'])
                        & (50 > data_drink['T01_WEIGHT'])]
H140W50_DM_mean = data_drink[(data_drink['T01_DM'] == 2) & (150 > data_drink['T01_HEIGHT'])
                        & (60 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 50)]
H140W60_DM_mean = data_drink[(data_drink['T01_DM'] == 2) & (150 > data_drink['T01_HEIGHT'])
                        & (70 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 60)]
H140W70_DM_mean = data_drink[(data_drink['T01_DM'] == 2) & (150 > data_drink['T01_HEIGHT'])
                        & (80 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 70)]
H140W80_DM_mean = data_drink[(data_drink['T01_DM'] == 2) & (150 > data_drink['T01_HEIGHT'])
                        & (data_drink['T01_WEIGHT'] >= 80)]

# Height 150cm~160cm
H150W40_DM_mean = data_drink[(data_drink['T01_DM'] == 2) & (160 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 150)
                        & (50 > data_drink['T01_WEIGHT'])]
H150W50_DM_mean = data_drink[(data_drink['T01_DM'] == 2) & (160 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 150)
                        & (60 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 50)]
H150W60_DM_mean = data_drink[(data_drink['T01_DM'] == 2) & (160 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 150)
                        & (70 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 60)]
H150W70_DM_mean = data_drink[(data_drink['T01_DM'] == 2) & (160 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 150)
                        & (80 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 70)]
H150W80_DM_mean = data_drink[(data_drink['T01_DM'] == 2) & (160 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 150)
                        & (data_drink['T01_WEIGHT'] >= 80)]

# Height 160cm~170cm
H160W40_DM_mean = data_drink[(data_drink['T01_DM'] == 2) & (170 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 160)
                        & (50 > data_drink['T01_WEIGHT'])]
H160W50_DM_mean = data_drink[(data_drink['T01_DM'] == 2) & (170 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 160)
                        & (60 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 50)]
H160W60_DM_mean = data_drink[(data_drink['T01_DM'] == 2) & (170 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 160)
                        & (70 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 60)]
H160W70_DM_mean = data_drink[(data_drink['T01_DM'] == 2) & (170 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 160)
                        & (80 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 70)]
H160W80_DM_mean = data_drink[(data_drink['T01_DM'] == 2) & (170 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 160)
                        & (data_drink['T01_WEIGHT'] >= 80)]

# Height 170cm~180cm
H170W40_DM_mean = data_drink[(data_drink['T01_DM'] == 2) & (180 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 170)
                        & (50 > data_drink['T01_WEIGHT'])]
H170W50_DM_mean = data_drink[(data_drink['T01_DM'] == 2) & (180 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 170)
                        & (60 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 50)]
H170W60_DM_mean = data_drink[(data_drink['T01_DM'] == 2) & (180 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 170)
                        & (70 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 60)]
H170W70_DM_mean = data_drink[(data_drink['T01_DM'] == 2) & (180 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 170)
                        & (80 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 70)]
H170W80_DM_mean = data_drink[(data_drink['T01_DM'] == 2) & (180 > data_drink['T01_HEIGHT']) & (data_drink['T01_HEIGHT'] >= 170)
                        & (data_drink['T01_WEIGHT'] >= 80)]

# Height 180cm~
H180W40_DM_mean = data_drink[(data_drink['T01_DM'] == 2) & (data_drink['T01_HEIGHT'] >= 180)
                        & (50 > data_drink['T01_WEIGHT'])]
H180W50_DM_mean = data_drink[(data_drink['T01_DM'] == 2) & (data_drink['T01_HEIGHT'] >= 180)
                        & (60 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 50)]
H180W60_DM_mean = data_drink[(data_drink['T01_DM'] == 2) & (data_drink['T01_HEIGHT'] >= 180)
                        & (70 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 60)]
H180W70_DM_mean = data_drink[(data_drink['T01_DM'] == 2) & (data_drink['T01_HEIGHT'] >= 180)
                        & (80 > data_drink['T01_WEIGHT']) & (data_drink['T01_WEIGHT'] >= 70)]
H180W80_DM_mean = data_drink[(data_drink['T01_DM'] == 2) & (data_drink['T01_HEIGHT'] >= 180)
                        & (data_drink['T01_WEIGHT'] >= 80)]

# Calculate drink frequency mean
H140W40_DM_mean = H140W40_DM_mean['T01_DRINK'].mean()
H140W50_DM_mean = H140W50_DM_mean['T01_DRINK'].mean()
H140W60_DM_mean = H140W60_DM_mean['T01_DRINK'].mean()
H140W70_DM_mean = H140W70_DM_mean['T01_DRINK'].mean()
H140W80_DM_mean = H140W80_DM_mean['T01_DRINK'].mean()

H150W40_DM_mean = H150W40_DM_mean['T01_DRINK'].mean()
H150W50_DM_mean = H150W50_DM_mean['T01_DRINK'].mean()
H150W60_DM_mean = H150W60_DM_mean['T01_DRINK'].mean()
H150W70_DM_mean = H150W70_DM_mean['T01_DRINK'].mean()
H150W80_DM_mean = H150W80_DM_mean['T01_DRINK'].mean()

H160W40_DM_mean = H160W40_DM_mean['T01_DRINK'].mean()
H160W50_DM_mean = H160W50_DM_mean['T01_DRINK'].mean()
H160W60_DM_mean = H160W60_DM_mean['T01_DRINK'].mean()
H160W70_DM_mean = H160W70_DM_mean['T01_DRINK'].mean()
H160W80_DM_mean = H160W80_DM_mean['T01_DRINK'].mean()

H170W40_DM_mean = H170W40_DM_mean['T01_DRINK'].mean()
H170W50_DM_mean = H170W50_DM_mean['T01_DRINK'].mean()
H170W60_DM_mean = H170W60_DM_mean['T01_DRINK'].mean()
H170W70_DM_mean = H170W70_DM_mean['T01_DRINK'].mean()
H170W80_DM_mean = H170W80_DM_mean['T01_DRINK'].mean()

H180W40_DM_mean = H180W40_DM_mean['T01_DRINK'].mean()
H180W50_DM_mean = H180W50_DM_mean['T01_DRINK'].mean()
H180W60_DM_mean = H180W60_DM_mean['T01_DRINK'].mean()
H180W70_DM_mean = H180W70_DM_mean['T01_DRINK'].mean()
H180W80_DM_mean = H180W80_DM_mean['T01_DRINK'].mean()

# LIB patient data result
LIB_result = pd.DataFrame(data = { "~150cm" : [H140W40_LIB_mean, H140W50_LIB_mean, H140W60_LIB_mean, H140W70_LIB_mean, H140W80_LIB_mean],
                           "150cm~160cm" : [H150W40_LIB_mean, H150W50_LIB_mean, H150W60_LIB_mean, H150W70_LIB_mean, H150W80_LIB_mean],
                           "160cm~170cm" : [H160W40_LIB_mean, H160W50_LIB_mean, H160W60_LIB_mean, H160W70_LIB_mean, H160W80_LIB_mean],
                           "170cm~180cm" : [H170W40_LIB_mean, H170W50_LIB_mean, H170W60_LIB_mean, H170W70_LIB_mean, H170W80_LIB_mean],
                           "180cm~" : [H180W40_LIB_mean, H180W50_LIB_mean, H180W60_LIB_mean, H180W70_LIB_mean, H180W80_LIB_mean],})
# Missing data process
LIB_result.fillna(0.0, inplace=True)

# Number of drinks per week
LIB_result = LIB_result * 3.5
LIB_result = LIB_result.round(1)

# Indexing
LIB_result.index = ["~50kg", "50kg~60kg", "60kg~70kg", "70kg~80kg", "80kg~"]

# HTN result
HTN_result = pd.DataFrame(data = { "~150cm" : [H140W40_HTN_mean, H140W50_HTN_mean, H140W60_HTN_mean, H140W70_HTN_mean, H140W80_HTN_mean],
                           "150cm~160cm" : [H150W40_HTN_mean, H150W50_HTN_mean, H150W60_HTN_mean, H150W70_HTN_mean, H150W80_HTN_mean],
                           "160cm~170cm" : [H160W40_HTN_mean, H160W50_HTN_mean, H160W60_HTN_mean, H160W70_HTN_mean, H160W80_HTN_mean],
                           "170cm~180cm" : [H170W40_HTN_mean, H170W50_HTN_mean, H170W60_HTN_mean, H170W70_HTN_mean, H170W80_HTN_mean],
                           "180cm~" : [H180W40_HTN_mean, H180W50_HTN_mean, H180W60_HTN_mean, H180W70_HTN_mean, H180W80_HTN_mean],})
# Missing data process
HTN_result.fillna(0.0, inplace=True)

# Number of drinks per week
HTN_result = HTN_result * 3.5
HTN_result = HTN_result.round(1)

# Indexing
HTN_result.index = ["~50kg", "50kg~60kg", "60kg~70kg", "70kg~80kg", "80kg~"]

# DM result
DM_result = pd.DataFrame(data = { "~150cm" : [H140W40_DM_mean, H140W50_DM_mean, H140W60_DM_mean, H140W70_DM_mean, H140W80_DM_mean],
                           "150cm~160cm" : [H150W40_DM_mean, H150W50_DM_mean, H150W60_DM_mean, H150W70_DM_mean, H150W80_DM_mean],
                           "160cm~170cm" : [H160W40_DM_mean, H160W50_DM_mean, H160W60_DM_mean, H160W70_DM_mean, H160W80_DM_mean],
                           "170cm~180cm" : [H170W40_DM_mean, H170W50_DM_mean, H170W60_DM_mean, H170W70_DM_mean, H170W80_DM_mean],
                           "180cm~" : [H180W40_DM_mean, H180W50_DM_mean, H180W60_DM_mean, H180W70_DM_mean, H180W80_DM_mean],})
# Missing data process
DM_result.fillna(0.0, inplace=True)

# Number of drinks per week
DM_result = DM_result * 3.5
DM_result = DM_result.round(1)

# Indexing
DM_result.index = ["~50kg", "50kg~60kg", "60kg~70kg", "70kg~80kg", "80kg~"]

print("<Drinking frequency according to height and weight of LIB patients>\n")
print(LIB_result, "\n")

print("<Drinking frequency according to height and weight of HTN patients>\n")
print(HTN_result, "\n")

print("<Drinking frequency according to height and weight of DM patients>\n")
print(DM_result, "\n")