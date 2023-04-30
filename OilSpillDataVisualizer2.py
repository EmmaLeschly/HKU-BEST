# import libraries
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import cartopy.feature as cfeature

# plot map
plt.figure(figsize = (12, 8))
ax = plt.axes(projection=ccrs.PlateCarree())
ax.coastlines()
ax.stock_img()
ax.gridlines(draw_labels=True)
ax.add_feature(cfeature.BORDERS)
ax.add_feature(cfeature.LAKES, alpha=0.5)
ax.add_feature(cfeature.RIVERS)
plt.show()

# oil spill coordinates
OS_lon, OS_lat = 2.73786024, 56.4239952
OS1_lon, OS1_lat = -122.1661, 37.4241

# plot oil spills
ax.plot([OS_lon, OS_lat], [OS1_lon, OS1_lat],
         color='blue', linewidth=2, marker='o')

# add labels
ax.text(OS_lon + 0.16, OS_lat - 0.02, 'Oil spill',
         horizontalalignment='right')

ax.text(OS1_lon + 0.02, OS1_lat - 0.02, 'Oil spill',
         horizontalalignment='left')

plt.show()
