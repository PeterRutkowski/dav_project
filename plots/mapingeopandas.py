import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
fp='C:\\Users\\rysza\\Desktop\\python data analysis\zajecia7\map switzerland\\swisscanton\\ch-cantons.shp'
map_df = gpd.read_file(fp)
map_df.plot()
map_df['Canton']=['AG','AR','AI','BL','BS','BE','FR','GE','GL','GR','JU','LU','NE','NW','OW','SG','SH','SZ','SO','TG','TI','UR','VS','VD','ZG','ZH']
df = pd.read_csv('demographics_per_canton.csv', header=0)

merged = map_df.set_index('Canton').join(df.set_index('Canton'))

variable = 'Beds'
vmin, vmax = 0, 4500

fig, ax = plt.subplots(1, figsize=(10, 6))

merged.plot(column=variable, cmap='Blues', linewidth=0.8, ax=ax, edgecolor='0.8')
ax.axis('off')
ax.set_title('Number of beds', fontdict={'fontsize': '25', 'fontweight' : '3'})
ax.annotate('Source: Kaggle COVID19 Cases Switzerland',xy=(0.1, .08),
            xycoords='figure fraction', horizontalalignment='left',
            verticalalignment='top', fontsize=12, color='#555555')
sm = plt.cm.ScalarMappable(cmap='Blues', norm=plt.Normalize(vmin=vmin, vmax=vmax))
sm._A = []
cbar = fig.colorbar(sm)
fig.savefig('beds.png', dpi=300)