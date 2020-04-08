# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 20:19:33 2020

@author: sunny
"""

import time
import urllib.request, json 
import requests
from datetime import datetime
import numpy as np
import matplotlib
import matplotlib.figure
from matplotlib.font_manager import FontProperties
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

plt.rcParams['font.sans-serif'] = ['FangSong']  # 设置默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像时'-'显示为方块的问题

def catch_daily():
    """抓取每日确诊和死亡数据"""

    with urllib.request.urlopen("https://covidtracking.com/api/us/daily") as url:
        data = json.loads(url.read().decode())
    data.sort(key=lambda x:x['date'])
    
    date_list = list() # 日期
    confirm_list = list() # 确诊
    suspect_list = list() # 疑似
    dead_list = list() # 死亡
    heal_list = list() # 治愈
    for item in data:
        date = item['dateChecked']
        month, day = date[6:10].split('-')
        date_list.append(datetime.strptime('2020-%s-%s'%(month, day), '%Y-%m-%d'))
        confirm_list.append(int(item['positive']))
        suspect_list.append(int(item['pending']))
        dead_list.append(int(item['death']))
        heal_list.append(item['hospitalizedCumulative'])
    
    return date_list, confirm_list, suspect_list, dead_list, heal_list

def plot_daily():
    """绘制每日确诊和死亡数据"""
    
    date_list, confirm_list, suspect_list, dead_list, heal_list = catch_daily() # 获取数据
    
    plt.figure('nCoV-US', facecolor='#f4f4f4', figsize=(10, 8))
    plt.title('nCoV-US', fontsize=20)
    
    plt.plot(date_list, confirm_list, label='确诊')
    plt.plot(date_list, suspect_list, label='疑似')
    plt.plot(date_list, dead_list, label='死亡')
    plt.plot(date_list, heal_list, label='治愈')
    
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d')) # 格式化时间轴标注
    plt.legend(loc='best') # 显示图例
    plt.show()
    
if __name__ == '__main__':
    plot_daily()