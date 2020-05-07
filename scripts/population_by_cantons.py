import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
fp='C:\\Users\\rysza\\Desktop\\python data analysis\zajecia7\map switzerland\\swisscanton\\ch-cantons.shp'
map_df = gpd.read_file(fp)
map_df.plot()
map_df['Canton']=['AG','AR','AI','BL','BS','BE','FR','GE','GL','GR','JU','LU','NE','NW','OW','SG','SH','SZ','SO','TG','TI','UR','VS','VD','ZG','ZH']
df = pd.read_csv('C:/Users/rysza/Desktop/python data analysis/Project/demographics_per_canton.csv', header=0)

df=df[['Canton','Population']]
merged = map_df.set_index('Canton').join(df.set_index('Canton'))

variable = 'Population'
vmin, vmax = 16145, 1520968

fig, ax = plt.subplots(1, figsize=(10, 6))

merged.plot(column=variable, cmap='Blues', linewidth=0.8, ax=ax, edgecolor='0.5')
ax.axis('off')
ax.set_title('Population by cantons', fontdict={'fontsize': '10', 'fontweight' : '3'})
ax.annotate('Source: Kaggle COVID19 Switzerland',xy=(0.1, .08),
            xycoords='figure fraction', horizontalalignment='left',
            verticalalignment='top', fontsize=8, color='#555555')
sm = plt.cm.ScalarMappable(cmap='Blues', norm=plt.Normalize(vmin=vmin, vmax=vmax))
sm._A = []
cbar = fig.colorbar(sm)
fig.set_size_inches(7,3)
fig.savefig('C:\\Users\\rysza\\Desktop\\python data analysis\\Project\\plots\\population_by_cantons.png', dpi=300)