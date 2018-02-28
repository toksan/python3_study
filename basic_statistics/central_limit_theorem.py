"""
=======================================
Experiment on the central limit theorem
=======================================

Requirements
Python3, numpy, matplotlib

Document
https://it-engineer-lab.com/archives/1237
"""

import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

n = 100  # 取り出すサンプルサイズ（適当に設定）
num_trials = 10000  # サンプルを取り出す回数（適当に設定）
num_bins = 50  # ヒストグラムのビン数（適当に設定）

# 母集団
# 0〜999の中からランダムで300個の整数を取得
population = np.random.randint(0, 1000, size=300)  # （適当に設定）

# 母集団からn個のサンプルをランダム抽出し、その平均値を取得。この試行を num_trials 回繰り返す。各回の平均値をリスト内包表記でセット。
# mean_list の中身 [1回目の平均値, 2回目の平均値, 3回目の平均値, ... num_trials回目の平均値]
mean_list = [np.random.choice(population, n).mean() for i in range(num_trials)]
mean_array = np.array(mean_list)  # list to np.array


def _round(num):
    """
    出力時に見やすいよう数値を丸める
    :param num: 数値
    :return: 丸めた数値
    """
    return round(num, 2)


# レポートの出力
print('母平均:', _round(population.mean()))
print('母分散:', _round(population.var()))
print('母分散/n:', _round(population.var() / n))
print('標本平均の分布:', 'N({0}, {1})'.format(_round(mean_array.mean()), _round(mean_array.var())))

# 以下、図の出力（上下2分割）
plt.figure(figsize=(6, 8))
ax1 = plt.subplot(2, 1, 1)
ax2 = plt.subplot(2, 1, 2)

# 母集団を可視化（ヒストグラム）
ax1.hist(population, bins=num_bins, alpha=0.8, normed=True)
ax1.set_title('Histogram of the Population')

# 各試行の平均値を可視化（ヒストグラムと確率密度を表示）
# https://matplotlib.org/examples/statistics/histogram_demo_features.html
_, bins, patches = ax2.hist(mean_array, num_bins, alpha=0.8, normed=True)
y = mlab.normpdf(bins, mean_array.mean(), mean_array.std())
ax2.plot(bins, y)
ax2.set_title('Distribution of sample mean')

plt.tight_layout()
plt.subplots_adjust(hspace=0.3)
plt.show()

'''
実行結果（一例）

母平均: 489.45
母分散: 86307.64
母分散/n: 863.08
標本平均の分布: N(489.61, 865.81)

備考
スクリプト実行時に乱数で母集団を作るので、
結果の数値は実行する度に変わります。
'''