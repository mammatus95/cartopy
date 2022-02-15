# CartoPy

Cartopy is a new map plotting tool/package for python3.X
and will replace the basemap package in 2020 when the Python2.7 support is EoL’ed.
(More pieces of information further down.)


## Installation

See here:
https://scitools.org.uk/cartopy/docs/latest/installing.html#installing

### Conda
```bash
conda install -c conda-forge cartopy
```

### Requirements
Python 2.7 or higher 

##### required Packages
NumPy 1.10, 
GEOS 3.3.3, 
Shapely 1.5.6, 
pyshp 1.1.4, 
PROJ 4.9.0
and six 1.3.0

![Cartopy Example](images/de.png)


### Will Cartopy replace Basemap?

To answer this question a link to a official announcement from the Basemap site:
https://matplotlib.org/basemap/users/intro.html#cartopy-new-management-and-eol-announcement

Newer developments are not known ...  we will see.

### Shapes and shapereader

How to add a background to you plots like topography, boundaries of states 
or infrastructure are explained here:
https://scitools.org.uk/cartopy/docs/v0.15/tutorials/using_the_shapereader.html

A short summary what you have to do:
1. Chose a shapefile of you desire here: https://www.naturalearthdata.com/downloads/
2. Save the shapefile on any kind of hard disk.
2. Imoprt: `import cartopy.io.shapereader as shpreader`
3. Load the shapefile into your script and add it to you plot:

```python
shapename = 'your_shape_file'
adm1_shapes = list(shpreader.Reader(shapename).geometries())
ax.add_geometries(adm1_shapes, crs.PlateCarree(), edgecolor='?',facecolor='?')
```
or
```python
shapename = 'your_shape_file'
prob_shp = shpreader.natural_earth(resolution='110m', category='cultural', name=shapename)
ax.add_geometries(shpreader.Reader(prob_shp).geometries(),
        ccrs.PlateCarree())
```