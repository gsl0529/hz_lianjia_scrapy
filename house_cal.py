# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 20:23:48 2018

@author: Administrator
"""
import json
import numpy as np
import matplotlib.pyplot as mp

with open('hz_house.json', 'r', encoding='utf-8') as f:
    house_size = []
    house_price = []
    for line in f:
        data = json.loads(line)
        try:
            size = float(data['size'][:-2])
            price = int(data['price'])
            house_size.append(size)
            house_price.append(price)
        except:
            pass

house_size = np.array(house_size)
house_price = np.array(house_price)

print('平均面积为：',round(house_size.mean(), 2), '平方米')
print('平均价格为：', round(house_price.mean(), 3), '万元')
print('面积标准差为：', house_size.std())
print('价格标准差为：', house_price.std())

mp.figure('house_hz', facecolor='lightgray')
mp.subplot(221)
mp.title('price distribution', fontsize=14)
mp.xlabel('price', fontsize=12)
mp.ylabel('count', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(axis='y', linestyle=':')
mp.hist(house_price, bins=20, color='deepskyblue', edgecolor='steelblue')
mp.tight_layout()
mp.subplot(222)
mp.title('size distribution', fontsize=14)
mp.xlabel('size', fontsize=12)
mp.ylabel('count', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(axis='y', linestyle=':')
mp.hist(house_size, bins=20, color='deepskyblue', edgecolor='steelblue')
mp.tight_layout()
mp.subplot(223)
mp.title('size-price distribution', fontsize=14)
mp.xlabel('size', fontsize=12)
mp.ylabel('price', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.scatter(house_size, house_price, s=3, alpha=0.5, c='limegreen')
mp.tight_layout()
mp.subplot(224)
mp.title('price/m2 distribution', fontsize=14)
mp.xlabel('price/m2', fontsize=12)
mp.ylabel('count', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(axis='y',linestyle=':')
house_m2_price = house_price/house_size * 10000
mp.hist(house_m2_price, bins=20, color='deepskyblue', edgecolor='steelblue')
mp.tight_layout()
mp.show()