# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

gdf = gpd.read_file("ev_chargers_ca.shp")

## Let's see our data's columns ##
#for column in gdf.columns:
#  print(column)
  
#print(gdf.head())
 
#gdf.plot()

fig, ax = plt.subplots(figsize = (10,8))
gdf.plot(ax=ax)
plt.show()
