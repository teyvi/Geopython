#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 22:25:41 2023

@author: angelateyvi
"""

basename = "Station_"
filenames = []

for number in range(21):
    station = f"{basename}{number}.txt"
    filenames.append(station)

print(filenames)
