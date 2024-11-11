# -*- encoding: utf-8 -*-
'''
@File    :   broken_plot.py
@Time    :   2022/06/07 21:59:01
@Author  :   HMX 
@Version :   1.0
@Contact :   kdhb8023@163.com
'''
# here put the import lib
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

def cm2inch(a, b):
    return a / 2.54, b / 2.54

def plot_broken(ax1, ax2):
    # 绘制断裂处的标记
    d = 0.85  # 设置倾斜度    
    kwargs = dict(marker=[(-1, -d), (1, d)], markersize=5,
                  linestyle='none', color='k', mec='k', mew=1, clip_on=False)
    ax2.plot([0, 1], [0, 0], transform=ax2.transAxes, **kwargs)
    ax1.plot([0, 1], [1, 1], transform=ax1.transAxes, **kwargs)
    ax2.spines['bottom'].set_visible(False)  # 关闭子图2中底部脊
    ax1.spines['top'].set_visible(False)  # 关闭子图1中顶部脊
    ax2.set_xticks([])

size1 = 10.5
mpl.rcParams.update(
    {
        'text.usetex': False,
        'font.family': 'stixgeneral',
        'mathtext.fontset': 'stix',
        "font.family": 'serif',
        "font.size": size1,
        "font.serif": ['Times New Roman'],
    }
)

# 构造数据
data = np.array([[5, 7, 6, 8], [10, 12, 11, 9], [3, 4, 2, 5], [8, 9, 7, 6], [15, 14, 13, 16], [20, 18, 19, 17]])
x = range(1, len(data[0]) + 1)

# 构造fig,ax
fig = plt.figure(figsize=(cm2inch(16, 9)))
ax1 = fig.add_axes([0.15, 0.15, 0.8, 0.35])
ax2 = fig.add_axes([0.15, 0.55, 0.8, 0.35])

colors = ['red', 'blue', 'green', 'orange', 'purple', 'pink']

for i in range(len(data)):
    ax1.bar(x, data[i], color=colors[i], label=f'Group {i+1}')
    ax2.bar(x, data[i], color=colors[i])

ax1.set_ylim(0, 0.01)
ax2.set_ylim(10, 25)
ax1.set_yticks(np.arange(0, 0.011, 0.002))
plot_broken(ax1, ax2)
ax1.set_xlabel('xlabel')
ax2.set_ylabel('ylabel                                        ')  # 空格调节令ylabel居中
plt.savefig(r'out.png', dpi=600)
plt.show()
