#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 04:37:28 2023

@author: angelateyvi
"""

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
temperature = [-3.5, -4.5, -1.0, 4.0, 10, 15, 18, 16, 11.5, 6.0, 2.0, -1.5]
selectedMonth = 'March'
monthIndex = months.index(selectedMonth)
print('The average temperature in Helsinki in', selectedMonth, 'is', temperature[monthIndex])