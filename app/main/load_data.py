# -*- coding:UTF-8 -*-


class Algorithm(object):
    y_pre = []
    y_real = []

    def __init__(self,  filename):
        y_pre,y_real = self.net_predict(filename)
        self.y_pre = y_pre[0:23]
        self.y_real = y_real[0:23]


    # 小波神经网络预测
    def net_predict(self, filename):
        from numpy import *
        from sklearn.neural_network import MLPRegressor
        from sklearn.preprocessing import MinMaxScaler
        import numpy as np
        import xlrd

        data = xlrd.open_workbook(filename)
        sheet = data.sheet_by_index(0)
        nrows = sheet.nrows  # 读取Excel表格行数
        ncols = sheet.ncols - 6  # 读取Excel表格列数
        datamatrix = zeros((nrows, ncols))
        for x in range(nrows):
            row = sheet.row_values(x)
            datamatrix[x, :] = row[6:30]
        dataMat = np.array(datamatrix)
        HOURS = 24
        D = 14  # 输入维数
        TRAIN_SIZE = 32 * HOURS  # 输入训练样本个数
        TEST_SIZE = 8 * HOURS  # 输入测试样本个数
        input_train_data = zeros((TRAIN_SIZE, D))  # 初始化训练样本
        output_train_data = zeros((TRAIN_SIZE, 1))
        input_test_data = zeros((TEST_SIZE, D))
        output_test_data = zeros((TEST_SIZE, 1))
        var = 0
        for i in range(2, nrows):
            for j in range(HOURS):
                if var < TRAIN_SIZE:
                    input_train_data[var, 0] = dataMat[i - 1, j]
                    input_train_data[var, 1] = dataMat[i - 2, j]
                    if j < 12:
                        input_train_data[var, 2:14 - j] = dataMat[i - 1, j + 12:24]
                        input_train_data[var, 14 - j:14] = dataMat[i, 0:j]
                    else:
                        input_train_data[var, 2:14] = dataMat[i, j - 12:j]
                    output_train_data[var, 0] = dataMat[i, j]
                else:
                    input_test_data[var - TRAIN_SIZE, 0] = dataMat[i - 1, j]
                    input_test_data[var - TRAIN_SIZE, 1] = dataMat[i - 2, j]
                    if j < 12:
                        input_test_data[var - TRAIN_SIZE, 2:14 - j] = dataMat[i - 1, j + 12:24]
                        input_test_data[var - TRAIN_SIZE, 14 - j:14] = dataMat[i, 0:j]
                    else:
                        input_test_data[var - TRAIN_SIZE, 2:14] = dataMat[i, j - 12:j]
                    output_test_data[var - TRAIN_SIZE, 0] = dataMat[i, j]
                var = var + 1
        # 数据归一化
        min_max_scaler = MinMaxScaler()
        input_train_data = min_max_scaler.fit_transform(input_train_data)
        input_test_data = min_max_scaler.fit_transform(input_test_data)
        solver = 'lbfgs'
        alpha = 1e-5
        hidden_layer_sizes = (100, 10)
        clf = MLPRegressor(solver=solver, alpha=alpha, hidden_layer_sizes=hidden_layer_sizes, random_state=1)
        clf.fit(input_train_data, output_train_data)
        y_pre = clf.predict(input_test_data)
        return y_pre,output_test_data[:,0]



