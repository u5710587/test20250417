# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 15:37:02 2025

@author: USER
"""

num=eval(input("請輸入九九乘法表最大顯示的數值:"))
for i in range(1,num+1):
	for j in range(1,num+1):
		print("%d*%d=%d" %(i,j,i*j),end="\t")
	print()