#!/usr/bin/python3
import numpy as np
from netCDF4 import Dataset

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.path as mpath

# cartopy
import cartopy.crs as crs
import cartopy.feature as cfeature
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
states_provinces = cfeature.NaturalEarthFeature(
    category='cultural', name='admin_0_boundary_lines_land', scale='10m', facecolor='none')


# 1. open netcdf
dataset = Dataset('geo.nc')
print(dataset.file_format)

# Variable
print(dataset.variables.keys())

geo_fld = dataset.variables['z']
print(f"Geopotential fiel:\n Shape: {np.shape(geo_fld)} Max: {np.max(geo_fld):.1f} Min: {np.min(geo_fld):.1f}")

# 2. Plotte das Geopotentialfeld
lat = dataset.variables['latitude'][:]
lon = dataset.variables['longitude'][:]

# 2.1 entry world
plt.figure(figsize=(6, 3))
ax = plt.axes(projection=crs.PlateCarree())
ax.coastlines(resolution='110m')
lons, lats= np.meshgrid(lon, lat)
clevs = np.arange(480, 600, 8)
cs=plt.contour(lons, lats, geo_fld[0, 0, :, :]/100.0, levels=clevs, transform=crs.PlateCarree(), colors='black', linewidths=1.7)
plt.clabel(cs, np.arange(480, 600, 8), fontsize=11, inline=True, inline_spacing=2, fmt='%.f')  # contour labels
plt.savefig('welt.png')

# 2.2 Nordhalbkugel
plt.figure(figsize=(6, 6))
ax = plt.axes(projection=crs.NorthPolarStereo())
ax.set_extent([-180, 180, 90, 60], crs.PlateCarree())
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.LAND)
ax.coastlines(resolution='110m')
theta = np.linspace(0, 2*np.pi, 100)
center, radius = [0.5, 0.5], 0.5
verts = np.vstack([np.sin(theta), np.cos(theta)]).T
circle = mpath.Path(verts * radius + center)

ax.set_boundary(circle, transform=ax.transAxes)

lons, lats= np.meshgrid(lon, lat)

cs=plt.contour(lons, lats, geo_fld[0, 0, :, :]/100.0, levels=clevs, transform=crs.PlateCarree(), colors='black', linewidths=1.7)
plt.clabel(cs, np.arange(480, 600, 8), fontsize=11, inline=True, inline_spacing=2, fmt='%.f') # contour labels
plt.savefig('nordpol.png')


# 2.3 Europa+Atlantik
plt.figure(figsize=(6, 5))
ax = plt.axes(projection=crs.Mercator())
ax.set_extent([-23.5, 45.0, 29.5, 67.5], crs.PlateCarree())
ax.coastlines(resolution='50m')
ax.gridlines()
ax.add_feature(cfeature.RIVERS)

cs=plt.contour(lons, lats, geo_fld[0, 0, :, :]/100.0, levels=clevs, transform=crs.PlateCarree(), colors='black', linewidths=1.7, zorder=5)
plt.clabel(cs, np.arange(480, 600, 8), fontsize=11, inline=True, inline_spacing=2, fmt='%.f') # contour labels
plt.savefig('europa.png')
