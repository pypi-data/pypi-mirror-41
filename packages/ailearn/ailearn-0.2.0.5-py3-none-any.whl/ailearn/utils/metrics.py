# Copyright 2018 Zhao Xingyu & An Yuexuan. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# -*- coding: utf-8 -*-
import numpy as np
from sklearn.model_selection import StratifiedKFold, train_test_split
import warnings


# 准确率
def accuracy_score(prediction, label):
    # prediction：预测类别或one-hot编码
    # label：实际类别或one-hot编码
    prediction, label = np.array(prediction), np.array(label)
    assert len(prediction.shape) == 1 or len(prediction.shape) == 2  # 输出值形状错误
    assert len(label.shape) == 1 or len(label.shape) == 2  # 真实值形状错误
    if len(prediction.shape) == 2:
        if prediction.shape[1] == 1:
            prediction = prediction.squeeze()
        else:
            prediction = np.argmax(prediction, 1)
    if len(label.shape) == 2:
        if label.shape[1] == 1:
            label = label.squeeze()
        else:
            label = np.argmax(label, 1)
    return np.mean(np.equal(prediction, label))


# 均方误差
def MSE(prediction, y, sample_importance=None):
    # prediction：预测值
    # y:真实值
    # sample_importance：样本重要性权重
    prediction, y = np.array(prediction).squeeze(), np.array(y).squeeze()
    assert len(prediction.shape) == 1 and len(y.shape) == 1  # 预测值或真实值形状错误
    if sample_importance is None:
        return np.mean(np.square(prediction - y))
    else:
        sample_importance = np.array(sample_importance)
        assert sample_importance.shape[0] == prediction.shape[0]  # 重要性权值形状错误
        return np.mean(sample_importance * np.square(prediction - y))


# 均方根误差
def RMSE(prediction, y, sample_importance=None):
    # prediction：预测值
    # y:真实值
    # sample_importance：样本重要性权重
    prediction, y = np.array(prediction).squeeze(), np.array(y).squeeze()
    assert len(prediction.shape) == 1 and len(y.shape) == 1  # 预测值或真实值形状错误
    if sample_importance is None:
        return np.sqrt(np.mean(np.square(prediction - y)))
    else:
        sample_importance = np.array(sample_importance)
        assert sample_importance.shape[0] == prediction.shape[0]  # 重要性权值形状错误
        return np.sqrt(np.mean(sample_importance * np.square(prediction - y)))


# 平均绝对误差
def MAE(prediction, y, sample_importance=None):
    # prediction：预测值
    # y:真实值
    # sample_importance：样本重要性权重
    prediction, y = np.array(prediction).squeeze(), np.array(y).squeeze()
    assert len(prediction.shape) == 1 and len(y.shape) == 1  # 预测值或真实值形状错误
    if sample_importance is None:
        return np.mean(np.abs(prediction - y))
    else:
        sample_importance = np.array(sample_importance)
        assert sample_importance.shape[0] == prediction.shape[0]  # 重要性权值形状错误
        return np.mean(sample_importance * np.abs(prediction - y))


# 误差平方和
def SSE(prediction, y, sample_importance=None):
    # prediction：预测值
    # y:真实值
    # sample_importance：样本重要性权重
    prediction, y = np.array(prediction).squeeze(), np.array(y).squeeze()
    assert len(prediction.shape) == 1 and len(y.shape) == 1  # 预测值或真实值形状错误
    if sample_importance is None:
        return np.sum(np.square(prediction - y))
    else:
        sample_importance = np.array(sample_importance)
        assert sample_importance.shape[0] == prediction.shape[0]  # 重要性权值形状错误
        return np.sum(sample_importance * np.square(prediction - y))


# 总平方和
def SST(y, sample_importance=None):
    # y:真实值
    # sample_importance：样本重要性权重
    y = np.array(y)
    assert len(y.shape) == 1  # 真实值形状错误
    if sample_importance is None:
        return np.sum(np.square(y - np.mean(y)))
    else:
        sample_importance = np.array(sample_importance)
        assert sample_importance.shape[0] == y.shape[0]  # 重要性权值形状错误
        return np.sum(sample_importance * np.square(y - np.mean(y)))


# 回归平方和
def SSR(prediction, y, sample_importance=None):
    # prediction：预测值
    # y:真实值
    # sample_importance：样本重要性权重
    prediction, y = np.array(prediction).squeeze(), np.array(y).squeeze()
    assert len(prediction.shape) == 1 and len(y.shape) == 1  # 预测值或真实值形状错误
    if sample_importance is None:
        return np.sum(np.square(prediction - np.mean(y)))  # Total sum of squares
    else:
        sample_importance = np.array(sample_importance)
        assert sample_importance.shape[0] == prediction.shape[0]  # 重要性权值形状错误
        return np.sum(sample_importance * np.square(prediction - np.mean(y)))


# 确定系数
def R_square(prediction, y, sample_importance=None):
    # prediction：预测值
    # y:真实值
    # sample_importance：样本重要性权重
    return 1 - SSE(prediction, y, sample_importance) / SST(y, sample_importance)


# K折交叉验证
def cross_val_score(estimator, x, y, k=10, verbose=True, **kwargs):
    # estimator：待评价的模型
    # x：样本数据
    # y：样本标签
    x, y = np.array(x), np.array(y)
    folder = StratifiedKFold(k, True, 0)
    scores = []
    for i, (train_index, test_index) in enumerate(folder.split(x, y)):
        estimator.fit(x[train_index], y[train_index], **kwargs)
        score = estimator.score(x[test_index], y[test_index])
        scores.append(score)
        if verbose:
            print('第%d次交叉验证完成，得分为%.4f' % (i + 1, score))
    scores = np.array(scores)
    return scores


# 留p法交叉验证
def leave_p_score(estimator, x, y, p=1, verbose=True, **kwargs):
    # estimator：待评价的模型
    # x：样本数据
    # y：样本标签
    x, y = np.array(x), np.array(y)
    if x.shape[0] < p:
        warnings.warn('交叉验证参数错误，不执行操作！')
        return None
    epoch = x.shape[0] // p
    index = np.arange(x.shape[0])
    np.random.shuffle(index)
    scores = []
    for i in range(epoch):
        test_index = slice(i * p, (i + 1) * p)
        train_index = np.delete(index, test_index)
        estimator.fit(x[train_index], y[train_index], **kwargs)
        score = estimator.score(x[test_index], y[test_index])
        scores.append(score)
        if verbose:
            print('第%d次交叉验证完成，得分为%.4f' % (i + 1, score))
    scores = np.array(scores)
    return scores


# Hold-Out检验
def hold_out_score(estimator, x, y, test_size=0.25, **kwargs):
    # estimator：待评价的模型
    # x：样本数据
    # y：样本标签
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=test_size, shuffle=True, stratify=y,
                                                        random_state=0)
    estimator.fit(x_train, y_train, **kwargs)
    return estimator.score(x_test, y_test)