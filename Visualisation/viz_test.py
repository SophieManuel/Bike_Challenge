# %%
#read json files
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import data

datas = {}
for i in np.arange(1,9):
    datas[i] = pd.read_json(f'loc{i}.json')

#%%
#Map
import folium
pt = []
map_mtp = {}
for j in np.arange(0,datas[1].shape[0]):
    map_mtp[j] = folium.Map(location = [43.6162094554924, 3.87440800666809], zoom_start = 12)
    for i in np.arange(1,9):
        loc = list(location[i].values())
        loc = loc[-1:]
        folium.CircleMarker(location = loc,radius = datas[i]['intensity'][j]).add_to(map_mtp[j])
    map_mtp[j].save(f"mtp_day_{str(datas[i]['Date'][j])[0:10]}.svg")
