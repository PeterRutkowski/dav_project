from pmdarima import auto_arima
from datetime import datetime
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path
import statsmodels.api as sm
from statsmodels.tsa.seasonal import seasonal_decompose 
from pathlib import Path

data_folder = Path("../data/")

data = pd.read_csv(data_folder/'che.csv')

dta = data[['new_deaths','date']]
dta=dta['new_deaths'].replace(to_replace=0, method='ffill')
dates=list(data['date'])

dta.index=[datetime.strptime(f"{date}{datetime.now().year}", "%d%b%Y") for date in dates]
result = seasonal_decompose(dta,  
                            model ='additive')

import warnings 
warnings.filterwarnings("ignore") 
  
# Fit auto_arima function to AirPassengers dataset 
stepwise_fit = auto_arima(dta, start_p = 1, start_q = 1, 
                          max_p = 3, max_q = 3, m = 1, 
                          start_P = 0, seasonal = False, 
                          d = None, D = None, trace = True, 
                          error_action ='ignore',   # we don't want to know if an order does not work 
                          suppress_warnings = True,  # we don't want convergence warnings 
                          stepwise = True)           # set to stepwise 
  
# To print the summary 
stepwise_fit.summary() 
arima_mod011 = sm.tsa.ARIMA(dta, (0,1,1),freq='D').fit(disp=False)
predict_= arima_mod011.predict(datetime(2020, 4, 30, 0, 0), datetime(2020, 5, 9, 0, 0))
fig, ax = plt.subplots(figsize=(12, 8))
ax = dta.loc['2020-02-26 00:00:00':].plot(ax=ax)
fig = arima_mod011.plot_predict('2020-04-30 00:00:00', '2020-05-09 00:00:00', dynamic=True, ax=ax, plot_insample=False)
plt.show()