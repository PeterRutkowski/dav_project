import pandas as pd
import plotly.express as px
import numpy as np

data = pd.read_csv('../data/che.csv')
dates = data['date']
data = data[['new_cases', 'new_deaths']]
x = np.asarray(data['new_cases'])
throwback = 30




# ARMA
from statsmodels.tsa.arima_model import ARMA
model = ARMA(x, order=(1,5))
model_fit = model.fit(disp=False)
pred = model_fit.predict(len(x), len(x)+throwback-1)

print(model_fit.params)

#fig = px.bar(df, x='Date', y='Growth factor')
#fig.write_html('plotly_growth.html', include_plotlyjs='cdn')