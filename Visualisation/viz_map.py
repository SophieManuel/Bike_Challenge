#%%
import folium

map_mtp = folium.Map(location=[43.6162094554924, 3.87440800666809], zoom_start = 12)
folium.CircleMarker([43.60969924926758, 3.896939992904663],  color='purple', fill_color='purple', radius=29).add_to(map_mtp)
folium.CircleMarker([43.5907, 3.81324], color='green', fill_color='green', radius=6.1).add_to(map_mtp)
folium.CircleMarker([43.61465, 3.8336], color='blue', fill_color='blue', radius=15.8).add_to(map_mtp)
folium.CircleMarker([43.57926, 3.93327], color='cyan', fill_color='cyan', radius=2.64).add_to(map_mtp)
folium.CircleMarker([43.57883, 3.93324], color='grey', fill_color='grey', radius=13.8).add_to(map_mtp)
folium.CircleMarker([43.6157418, 3.9096322], color='yellow', fill_color='yellow', radius=5.4).add_to(map_mtp)
folium.CircleMarker([43.6138841, 3.8684671],  color='k', fill_color='k', radius=24.1).add_to(map_mtp)
folium.CircleMarker([43.6266977, 3.8956288],  color='orange', fill_color='orange', radius=15.6).add_to(map_mtp)
folium.CircleMarker([43.6266977, 3.8956288], color='k', fill_color='k', radius=2.04).add_to(map_mtp)
folium.CircleMarker([43.61620945549243, 3.874408006668091], color='pink', fill_color='pink', radius=30).add_to(map_mtp)

map_mtp.save("mapfix.html")
