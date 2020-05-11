import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
fp='C:/Users/rysza/Desktop/python data analysis/Project/Europe/Europe.shp'
map_df = gpd.read_file(fp)
countries=['France','Italy','Switzerland','Austria','Germany','Liechtenstein']
map_df=map_df.loc[map_df['NAME'].isin(countries) ]
map_df=map_df.rename(columns={'NAME':'Country'})
df = pd.read_csv('C:/Users/rysza/Desktop/python data analysis/Project/ourworldindatadeathetc.csv')

df = df.loc[df['date']=='2020-04-28']
df = df.loc[df['location'].isin(countries)]
df=df.rename(columns={'location':'Country'})

merged = map_df.set_index('Country').join(df.set_index('Country'))
merged=merged[['total_cases','total_deaths','geometry']]

newdf=pd.DataFrame({'Country':countries,'Latitude':[46.4,42.5176,46.8959,47.6093,51.1586,47.1420],'Longitude':[2.3522,12.5156,8.2457,13.7826,10.4459,9.5445]})
gdf = gpd.GeoDataFrame(
    newdf, geometry=gpd.points_from_xy(newdf.Longitude, newdf.Latitude))
variable = 'total_cases'
vmin, vmax = 83, 199414

fig, ax = plt.subplots()
merged.plot(column=variable, cmap='Blues', linewidth=0.8, ax=ax, edgecolor='white')
ax.axis('off')
ax.set_title('Total cases and deaths in Switzerland and its neighbours', fontdict={'fontsize': '12', 'fontweight' : '3'})
ax.annotate('Source: Ourworldindata',xy=(0.75, .08),
            xycoords='figure fraction', horizontalalignment='left',
            verticalalignment='top', fontsize=7, color='#555555')
sm = plt.cm.ScalarMappable(cmap='Blues', norm=plt.Normalize(vmin=vmin, vmax=vmax))
sm._A = []
cbar = fig.colorbar(sm)
gdf.plot(ax=ax,edgecolor='black',color='black', markersize=[232.3,269.7,13.52,5.5,59.13,0.01])
ax.text(x=-15, y=53,s='Deaths')
ax.text(x=-15, y=49.5,s='26.9k')
ax.text(x=-15, y=45.5,s='23.2k')
ax.text(x=-15, y=41.5,s='5.9k')
ax.text(x=-15, y=37.5,s='1.3k')
ax.text(x=-15, y=33.5,s='500')
ax.scatter(x=[-18,-18,-18,-18,-18,-18],y=[50,46,42,38,34,30], s=[269.7,232.3,59.13,13.52,5.5,0.01],c='black')
fig.set_size_inches(7,3)
fig.savefig('C:\\Users\\rysza\\Desktop\\python data analysis\\Project\\plots\\cases_deaths_neighbours.png', dpi=400)