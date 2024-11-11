import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

from brokenaxes import brokenaxes

def cm2inch(a, b):
    return a / 2.54, b / 2.54

def plot_broken(ax1, ax2):
    # 绘制断裂处的标记
    d = 1  # 设置倾斜度    
    kwargs = dict(marker=[(-1, -d), (1, d)], markersize=20,
                  linestyle='none', color='k', mec='k', mew=2, clip_on=False)
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


fig = plt.figure(figsize=cm2inch(36,25))

ax1 = fig.add_axes([0.15, 0.15, 0.8, 0.35])
ax2 = fig.add_axes([0.15, 0.55, 0.8, 0.35])




'''
#任务固定,用户数量变时,用户端的开销
x_data = [format(i) for i in range(5,11)]
y1_data = [49.103,59.699,67.775,77.612,85.624,94.899]
y2_data = [2434,2431,2430,2433,2434,2439]
y3_data = [3270,3271,3274,3271,3271,3277]
y4_data = [0.014,0.014,0.014,0.0148,0.014,0.014]

x1_width = [i-0.3 for i in range(5,11)]
x2_width = [i-0.1 for i in range(5,11)]
x3_width = [i+0.1 for i in range(5,11)]
x4_width = [i+0.3 for i in range(5,11)]

ax1.bar(x1_width,y1_data,lw = 0.6,fc = "aquamarine",edgecolor = 'k',width=0.2)
ax2.bar(x1_width,y1_data,lw = 0.6,fc = "aquamarine",edgecolor = 'k',width=0.2,label = "RsAnonTD-Worker")
ax1.bar(x2_width,y2_data,lw = 0.6,fc = "lightskyblue",edgecolor = 'k',width=0.2)
ax2.bar(x2_width,y2_data,lw = 0.6,fc = "lightskyblue",edgecolor = 'k',width=0.2,label = "McFeKDeTD-Worker")
ax1.bar(x3_width,y3_data,lw = 0.6,fc = "lightpink",edgecolor = 'k',width=0.2)
ax2.bar(x3_width,y3_data,lw = 0.6,fc = "lightpink",edgecolor = 'k',width=0.2,label = "RPTD-Ⅱ-Worker")
ax1.bar(x4_width,y4_data,lw = 0.6,fc = "gold",edgecolor = 'k',width=0.2)
ax2.bar(x4_width,y4_data,lw = 0.6,fc = "gold",edgecolor = 'k',width=0.2,label = "L\u00B2-PPTD-Worker")

ax1.set_ylim(0, 0.04)
ax2.set_ylim(30, 4000)
ax1.set_yticks(np.arange(0, 0.041, 0.02))
ax2.set_yticks(np.arange(30, 4000, 500))
plot_broken(ax1, ax2)

ax1.set_xlabel('Number of workers',fontsize=48)
ax2.set_ylabel('Running time (ms)                          ',fontsize=48)  # 空格调节令ylabel居中
ax2.yaxis.set_label_coords(-0.1, 0.5)

ax2.legend(loc = 'upper left',fontsize=32)
ax1.tick_params(axis='x', labelsize=32)
ax1.tick_params(axis='y', labelsize=32)
ax2.tick_params(axis='y', labelsize=32)

plt.savefig("F:/研究生论文资料/群智感知/隐私保护真值发现算法构建/实验结果图/任务固定工人数量变-用户端开销.pdf",format = 'pdf',dpi=1000,bbox_inches = 'tight') 
plt.show()
'''


#任务固定,用户数量变时,第一个服务器的开销
x_data = [format(i) for i in range(5,11)]
y1_data = [0.131542,0.175938,0.248893,0.317672,0.379383,0.464084]
y2_data = [0.199622,0.258650,0.286251,0.326152,0.368422,0.406916]
y3_data = [5.600,6.215,6.830,7.550,7.990,9.091]
y4_data = [0.979480,1.156,1.302,1.476,1.597,1.768]

x1_width = [i-0.3 for i in range(5,11)]
x2_width = [i-0.1 for i in range(5,11)]
x3_width = [i+0.1 for i in range(5,11)]
x4_width = [i+0.3 for i in range(5,11)]

ax1.bar(x1_width,y1_data,lw = 0.6,fc = "aquamarine",edgecolor = 'k',width=0.2)
ax2.bar(x1_width,y1_data,lw = 0.6,fc = "aquamarine",edgecolor = 'k',width=0.2,label = "RsAnonTD-AS")
ax1.bar(x2_width,y2_data,lw = 0.6,fc = "lightskyblue",edgecolor = 'k',width=0.2)
ax2.bar(x2_width,y2_data,lw = 0.6,fc = "lightskyblue",edgecolor = 'k',width=0.2,label = "McFeKDeTD-KGC")
ax1.bar(x3_width,y3_data,lw = 0.6,fc = "lightpink",edgecolor = 'k',width=0.2)
ax2.bar(x3_width,y3_data,lw = 0.6,fc = "lightpink",edgecolor = 'k',width=0.2,label = "RPTD-Ⅱ-FN")
ax1.bar(x4_width,y4_data,lw = 0.6,fc = "gold",edgecolor = 'k',width=0.2)
ax2.bar(x4_width,y4_data,lw = 0.6,fc = "gold",edgecolor = 'k',width=0.2,label = "L²-PPTD-ServerB")

ax1.set_ylim(0, 2)
ax2.set_ylim(3, 12)
ax1.set_yticks(np.arange(0, 2.1, 0.5))
ax2.set_yticks(np.arange(3, 12, 2))
plot_broken(ax1, ax2)

ax1.set_xlabel('Number of workers',fontsize=48)
ax2.set_ylabel('Running time (ms)                          ',fontsize=48)  # 空格调节令ylabel居中
ax2.yaxis.set_label_coords(-0.1, 0.5)

ax2.legend(loc = 'upper left',fontsize=32)
ax1.tick_params(axis='x', labelsize=32)
ax1.tick_params(axis='y', labelsize=32)
ax2.tick_params(axis='y', labelsize=32)
plt.savefig("F:/研究生论文资料/群智感知/隐私保护真值发现算法构建/实验结果图/任务固定工人数量变-第一个服务器的开销.pdf",format='pdf',dpi=1000,bbox_inches = 'tight') 
plt.show()


'''
#任务固定,用户数量变时,第二个服务器的开销
x_data = [format(i) for i in range(5,11)]
y1_data = [0.000298,0.000259,0.000320,0.000330,0.000404,0.000409]
y2_data = [3.356,3.978,4.677,5.296,5.941,6.632]
y3_data = [7.434,8.718,9.882,11.022,12.242,13.439]
y4_data = [1.645,1.942,2.246,2.580,2.874,3.410]

x1_width = [i-0.3 for i in range(5,11)]
x2_width = [i-0.1 for i in range(5,11)]
x3_width = [i+0.1 for i in range(5,11)]
x4_width = [i+0.3 for i in range(5,11)]



ax1.bar(x1_width,y1_data,lw = 0.6,fc = "aquamarine",edgecolor = 'k',width=0.2)
ax2.bar(x1_width,y1_data,lw = 0.6,fc = "aquamarine",edgecolor = 'k',width=0.2,label = "RsAnonTD-DRC")
ax1.bar(x2_width,y2_data,lw = 0.6,fc = "lightskyblue",edgecolor = 'k',width=0.2)
ax2.bar(x2_width,y2_data,lw = 0.6,fc = "lightskyblue",edgecolor = 'k',width=0.2,label = "McFeKDeTD-DRC")
ax1.bar(x3_width,y3_data,lw = 0.6,fc = "lightpink",edgecolor = 'k',width=0.2)
ax2.bar(x3_width,y3_data,lw = 0.6,fc = "lightpink",edgecolor = 'k',width=0.2,label = "RPTD-Ⅱ-CSP")
ax1.bar(x4_width,y4_data,lw = 0.6,fc = "gold",edgecolor = 'k',width=0.2)
ax2.bar(x4_width,y4_data,lw = 0.6,fc = "gold",edgecolor = 'k',width=0.2,label = "L²-PPTD-Server\_{A}")

ax1.set_ylim(0, 0.01)
ax2.set_ylim(1, 15)
ax1.set_yticks(np.arange(0, 0.011, 0.002))
ax2.set_yticks(np.arange(1, 15, 2))
plot_broken(ax1, ax2)

ax1.set_xlabel('Number of workers',fontsize=48)
ax2.set_ylabel('Running time (ms)                          ',fontsize=48)  # 空格调节令ylabel居中
ax2.yaxis.set_label_coords(-0.1, 0.5)

ax2.legend(loc = 'upper left',fontsize=32)
ax1.tick_params(axis='x', labelsize=32)
ax1.tick_params(axis='y', labelsize=32)
ax2.tick_params(axis='y', labelsize=32)
plt.savefig("F:/研究生论文资料/群智感知/隐私保护真值发现算法构建/实验结果图/任务固定工人数量变-第二个服务器的开销.pdf",format='pdf',dpi=1000,bbox_inches = 'tight')  
plt.show()
'''

'''
#5用户10_15_20_25任务-工人端
x_data = [10,15,20,25]
y1_data = [47.475,52.944,48.725,53.904]
y2_data = [4050,5660,7725,8981]
y3_data = [6140,9166,12244,15141]
y4_data = [0.0127,0.0174,0.0135,0.0175]

x1_width = [i-1.2 for i in x_data]
x2_width = [i-0.4 for i in x_data]
x3_width = [i+0.4 for i in x_data]
x4_width = [i+1.2 for i in x_data]



ax1.bar(x1_width,y1_data,lw = 0.6,fc = "aquamarine",edgecolor = 'k',width=0.8)
ax2.bar(x1_width,y1_data,lw = 0.6,fc = "aquamarine",edgecolor = 'k',width=0.8,label = "RsAnonTD-Worker")
ax1.bar(x2_width,y2_data,lw = 0.6,fc = "lightskyblue",edgecolor = 'k',width=0.8)
ax2.bar(x2_width,y2_data,lw = 0.6,fc = "lightskyblue",edgecolor = 'k',width=0.8,label = "McFeKDeTD-Worker")
ax1.bar(x3_width,y3_data,lw = 0.6,fc = "lightpink",edgecolor = 'k',width=0.8)
ax2.bar(x3_width,y3_data,lw = 0.6,fc = "lightpink",edgecolor = 'k',width=0.8,label = "RPTD-Ⅱ-Worker")
ax1.bar(x4_width,y4_data,lw = 0.6,fc = "gold",edgecolor = 'k',width=0.8)
ax2.bar(x4_width,y4_data,lw = 0.6,fc = "gold",edgecolor = 'k',width=0.8,label = "L\u00B2-PPTD-Worker")

ax1.set_ylim(0, 0.1)
ax2.set_ylim(30, 20000)
ax1.set_yticks(np.arange(0, 0.11, 0.02))
ax2.set_yticks(np.arange(30, 20000, 5000))
plot_broken(ax1, ax2)

ax1.set_xlabel('Number of sensing tasks',fontsize=48)
ax2.set_ylabel('Running time (ms)                          ',fontsize=48)  # 空格调节令ylabel居中
ax2.yaxis.set_label_coords(-0.1, 0.5)
ax1.set_xticks(x_data)
ax2.legend(loc = 'upper left',fontsize=32)

ax1.tick_params(axis='x', labelsize=32)
ax1.tick_params(axis='y', labelsize=32)
ax2.tick_params(axis='y', labelsize=32)

plt.savefig("F:/研究生论文资料/群智感知/隐私保护真值发现算法构建/实验结果图/5_10_15_20_25_工人端.pdf",format='pdf',dpi=1000,bbox_inches = 'tight')        
plt.show()     
'''

'''
#5用户10_15_20_25任务-第一个服务器
x_data = [10,15,20,25]
y1_data = [0.125881,0.129296,0.136588,0.136829]
y2_data = [0.413501,0.615853,0.825880,1.010]
y3_data = [10.847,16.417,22.163,28.627]
y4_data = [1.873,2.738,3.627,4.538]

x1_width = [i-1.2 for i in x_data]
x2_width = [i-0.4 for i in x_data]
x3_width = [i+0.4 for i in x_data]
x4_width = [i+1.2 for i in x_data]



ax1.bar(x1_width,y1_data,lw = 0.6,fc = "aquamarine",edgecolor = 'k',width=0.8)
ax2.bar(x1_width,y1_data,lw = 0.6,fc = "aquamarine",edgecolor = 'k',width=0.8,label = "RsAnonTD-AS")
ax1.bar(x2_width,y2_data,lw = 0.6,fc = "lightskyblue",edgecolor = 'k',width=0.8)
ax2.bar(x2_width,y2_data,lw = 0.6,fc = "lightskyblue",edgecolor = 'k',width=0.8,label = "McFeKDeTD-KGC")
ax1.bar(x3_width,y3_data,lw = 0.6,fc = "lightpink",edgecolor = 'k',width=0.8)
ax2.bar(x3_width,y3_data,lw = 0.6,fc = "lightpink",edgecolor = 'k',width=0.8,label = "RPTD-Ⅱ-FN")
ax1.bar(x4_width,y4_data,lw = 0.6,fc = "gold",edgecolor = 'k',width=0.8)
ax2.bar(x4_width,y4_data,lw = 0.6,fc = "gold",edgecolor = 'k',width=0.8,label = "L²-PPTD-Server\_{B}")

ax1.set_ylim(0, 1.5)
ax2.set_ylim(1.5, 30)
ax1.set_yticks(np.arange(0, 1.6, 0.2))
ax2.set_yticks(np.arange(1.5, 31, 3))
plot_broken(ax1, ax2)

ax1.set_xlabel('Number of sensing tasks',fontsize=48)
ax2.set_ylabel('Running time (ms)                          ',fontsize=48)  # 空格调节令ylabel居中
ax2.yaxis.set_label_coords(-0.1, 0.5)
ax1.set_xticks(x_data)
ax2.legend(loc = 'upper left',fontsize=32)
ax1.tick_params(axis='x', labelsize=32)
ax1.tick_params(axis='y', labelsize=32)
ax2.tick_params(axis='y', labelsize=32)
plt.savefig("F:/研究生论文资料/群智感知/隐私保护真值发现算法构建/实验结果图/5_10_15_20_25_第一个服务器.pdf",format='pdf',dpi=1000,bbox_inches = 'tight')
plt.show()
'''

'''
#5用户10_15_20_25任务-第二个服务器
x_data = [10,15,20,25]
y1_data = [0.000486,0.000463,0.000621,0.000666]
y2_data = [3.402,3.471,3.424,3.432]
y3_data = [12.784,19.475,23.026,28.342]
y4_data = [3.200,4.767,6.337,7.904]

x1_width = [i-1.2 for i in x_data]
x2_width = [i-0.4 for i in x_data]
x3_width = [i+0.4 for i in x_data]
x4_width = [i+1.2 for i in x_data]
y_err = np.std(y1_data)
err_attr={"elinewidth":2,"ecolor":"black","capsize":6}

ax1.bar(x1_width,y1_data,lw = 0.6,fc = "aquamarine",edgecolor = 'k',width=0.8)
ax2.bar(x1_width,y1_data,yerr=y_err, error_kw=err_attr,lw = 0.6,fc = "aquamarine",edgecolor = 'k',width=0.8,label = "RsAnonTD-DRC")
ax1.bar(x2_width,y2_data,lw = 0.6,fc = "lightskyblue",edgecolor = 'k',width=0.8)
ax2.bar(x2_width,y2_data,lw = 0.6,fc = "lightskyblue",edgecolor = 'k',width=0.8,label = "McFeKDeTD-DRC")
ax1.bar(x3_width,y3_data,lw = 0.6,fc = "lightpink",edgecolor = 'k',width=0.8)
ax2.bar(x3_width,y3_data,lw = 0.6,fc = "lightpink",edgecolor = 'k',width=0.8,label = "RPTD-Ⅱ-CSP")
ax1.bar(x4_width,y4_data,lw = 0.6,fc = "gold",edgecolor = 'k',width=0.8)
ax2.bar(x4_width,y4_data,lw = 0.6,fc = "gold",edgecolor = 'k',width=0.8,label = "L²-PPTD-Server\_{A}")

ax1.set_ylim(0, 0.01)
ax2.set_ylim(1, 30)
ax1.set_yticks(np.arange(0, 0.011, 0.002))
ax2.set_yticks(np.arange(1, 31, 3))
plot_broken(ax1, ax2)

ax1.set_xlabel('Number of sensing tasks',fontsize=48)
ax2.set_ylabel('Running time (ms)                          ',fontsize=48)  # 空格调节令ylabel居中
ax2.yaxis.set_label_coords(-0.1, 0.5)
ax1.set_xticks(x_data)
ax2.legend(loc = 'upper left',fontsize=32)
ax1.tick_params(axis='x', labelsize=32)
ax1.tick_params(axis='y', labelsize=32)
ax2.tick_params(axis='y', labelsize=32)
plt.savefig("F:/研究生论文资料/群智感知/隐私保护真值发现算法构建/实验结果图/5_10_15_20_25_第二个服务器.pdf",format='pdf',dpi=1000,bbox_inches = 'tight')
plt.show()
'''




'''
#RMSE实验--任务数量固定为5
x_data = [format(i) for i in range(5,11)]
y2_data = [1.45,0.91,0.73,0.90,0.67,0.53]
y3_data = [1.46,0.91,0.74,0.90,0.67,0.53]
y1_data = [1.45,0.91,0.73,0.90,0.67,0.53]

x1_width = [i-0.3 for i in range(5,11)]
x2_width = [i-0.1 for i in range(5,11)]
x3_width = [i+0.1 for i in range(5,11)]
x4_width = [i+0.3 for i in range(5,11)]


plt.bar(x1_width,y1_data,lw = 0.6,fc = "lightsalmon",edgecolor = 'k',width=0.2,label = "CRH")
plt.bar(x2_width,y2_data,lw = 0.6,fc = "aquamarine",edgecolor = 'k',width=0.2,label = "RsAnonTD")
plt.bar(x3_width,y3_data,lw = 0.6,fc = "lightskyblue",edgecolor = 'k',width=0.2,label = "McFeKDeTD")



plt.xlabel('Number of workers',fontsize=11)
plt.ylabel('RMSE',fontsize=11) 
plt.tick_params(axis='x', labelsize=11)
plt.tick_params(axis='y', labelsize=11)

plt.legend(loc = 'upper right',fontsize=12)
plt.savefig("F:/研究生论文资料/群智感知/隐私保护真值发现算法构建/实验结果图/rmse.pdf",format='pdf',dpi=1000,bbox_inches = 'tight')
plt.show()
'''