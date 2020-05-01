import geopandas as gpd
import numpy as np
import pandas as pd
from shapely.geometry import LineString, MultiLineString
def shapefile_to_geojson(gdf, index_list, level = 1, tolerance=0.025): 
    # gdf - geopandas dataframe containing the geometry column and values to be mapped to a colorscale
    # index_list - a sublist of list(gdf.index)  or gdf.index  for all data
    # level - int that gives the level in the shapefile
    # tolerance - float parameter to set the Polygon/MultiPolygon degree of simplification
    
    # returns a geojson type dict 
   
    geo_names = list(gdf[f'NAME_{level}'])
    geojson = {'type': 'FeatureCollection', 'features': []}
    for index in index_list:
        geo = gdf['geometry'][index].simplify(tolerance)
    
        if isinstance(geo.boundary, LineString):
            gtype = 'Polygon'
            bcoords = np.dstack(geo.boundary.coords.xy).tolist()
    
        elif isinstance(geo.boundary, MultiLineString):
            gtype = 'MultiPolygon'
            bcoords = []
            for b in geo.boundary:
                x, y = b.coords.xy
                coords = np.dstack((x,y)).tolist() 
                bcoords.append(coords) 
        else: pass
        
        
       
        feature = {'type': 'Feature', 
                   'id' : index,
                   'properties': {'name': geo_names[index]},
                   'geometry': {'type': gtype,
                                'coordinates': bcoords},
                    }
                                
        geojson['features'].append(feature)
    return geojson
level = 1
gdf = gpd.read_file(f'C:\\Users\\rysza\\Desktop\\python data analysis\zajecia7\map switzerland\\swisscanton\\ch-cantons.shp', encoding='utf-8')
gdf['NAME_1']=['AG','AR','AI','BL','BS','BE','FR','GE','GL','GR','JU','LU','NE','NW','OW','SG','SH','SZ','SO','TG','TI','UR','VS','VD','ZG','ZH']
geojsdata = shapefile_to_geojson(gdf, list(gdf.index))