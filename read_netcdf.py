import netCDF4
import numpy as np
from dataDownload import getFile, getFolder



f = netCDF4.Dataset('./data/pr_day_ACCESS-CM2_historical_r1i1p1f1_gn_1950.nc')
pre=f.variables['pr']
mytime=f.variables['time']
myt=mytime[:]
lat, lon = f.variables['lat'], f.variables['lon']
latvals = lat[:]; lonvals = lon[:] # extract lat/lon values (in degrees) to numpy arrays


# a function to find the index of the point closest (in squared distance) to give lat/lon value.
def getclosest_ij(lats,lons,latpt,lonpt):
    mindis=99999.00
    for ila, la in enumerate(lats):
        for ilo,lo in enumerate(lons):
            dist=(la-latpt)**2+(lo-lonpt)**2
            if dist < mindis:
               mindis=dist
               min_y=ila
               min_x=ilo
    return(min_y,min_x)
#    dist_sq = (lats-latpt)**2 + (lons-lonpt)**2  # find squared distance of every point on grid
#    minindex_flattened = dist_sq.argmin() # 1D index of minimum dist_sq element
    # Get 2D index for latvals and lonvals arrays from 1D index
#    return np.unravel_index(minindex_flattened)
#    return np.unravel_index(minindex_flattened, latvals.shape)
#iy_min, ix_min = getclosest_ij(latvals, lonvals, 41.2, -89, min_y,min_x)
#min_y,min_x=getclosest_ij(latvals, lonvals, 41.2, -89)
min_y,min_x=getclosest_ij(latvals, lonvals, 41.2, 271) #long from 0 to 360. convert -89 to 0-360
pre.set_auto_mask(False)
mypre=pre[:,min_y,min_x]

# print(lon[min_x],lat[min_y])

print (mypre[:])
# print(myt[:])
#print (pre[:,iy_min,ix_min])

"""

point format: _place
time output format: 1956/01/01
pr/tas
convert lon/lat


"""