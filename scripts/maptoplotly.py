import geopandas as gpd
import pandas as pd
import plotly.graph_objects as go
from utils import shapefile_to_geojson


gdf = gpd.read_file(f'C:\\Users\\rysza\\Desktop\\python data analysis\zajecia7\map switzerland\\swisscanton\\ch-cantons.shp', encoding='utf-8')
gdf['NAME_1']=['AG','AR','AI','BL','BS','BE','FR','GE','GL','GR','JU','LU','NE','NW','OW','SG','SH','SZ','SO','TG','TI','UR','VS','VD','ZG','ZH']
geojsdata = shapefile_to_geojson(gdf, list(gdf.index))
df = pd.read_csv('demographics_per_canton.csv', header=0)
df=df.sort_values('Canton')
df=df.reset_index(drop=True)

trace = go.Choroplethmapbox(z=df['Beds'],
                            locations = df.index, 
                            colorscale = 'Blues',
                            colorbar = dict(thickness=20, ticklen=3),
                            geojson = geojsdata,
                            text = df['Canton'],
                            hoverinfo='all',
                            marker_line_width=0.1, marker_opacity=0.7
                            )
layout = go.Layout(title_text= 'Choroplethmapbox',
                   title_x=0.5, width = 700, height=700,
                   mapbox = dict(center= dict(lat=47.3769,  lon=8.5417),
                                 accesstoken= 'pk.eyJ1Ijoic3pjem9yIiwiYSI6ImNrOW84MWVxbjA5OXAzZ3BwaG13NjZwc2EifQ.sqmpqVeuJYtZ21hGVJhqQw',
                                 zoom=2.650,
                               ))
fig=go.Figure(data=[trace], layout =layout)
fig.write_html('maptoplotly.html',include_plotlyjs='cdn')