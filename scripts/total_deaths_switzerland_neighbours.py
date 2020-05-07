import os
import sys
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

df=pd.read_csv('ourworldindatadeathetc.csv', header=0)
countries=['Switzerland','France','Italy','Austria','Germany','Liechtenstein']


df=df[df['location'].isin(countries)]
df=df[['location','date','total_deaths']]


fig = px.line(df, x='date',y='total_deaths',color='location',range_x=['2020-01-10','2020-05-20'],
              color_discrete_sequence=['red','purple','orange','blue','green','yellow'],hover_name='total_deaths',hover_data=['date'])


fig.update_layout(
    xaxis_title="",
    yaxis_title="",
    xaxis=dict(
        showline=True,
        showgrid=False,
        showticklabels=True,
        linecolor='black',
        linewidth=2,
        ticks='outside',
        tickfont=dict(
            family='Arial',
            size=12,
            color='black',
        ),
    ),
    yaxis=dict(
        showgrid=True,
        gridcolor='grey',
        zeroline=True,
        showline=True,
        showticklabels=True
    ),
    margin=dict(
        autoexpand=False,
        l=100,
        r=20,
        t=110,
    ),
    showlegend=False,
    plot_bgcolor='white',
    title={
        'text': "Total deaths from COVID-19 in Switzerland and its neighbours",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top',
        'font': dict(
        size=25)
        }
    )
fig.add_trace(go.Scatter(
    x=['2020-05-02','2020-05-04','2020-05-02','2020-05-02','2020-05-02','2020-05-04'],
    y=[1000,2500,7000,23660,27359,-500],
    text=['Austria','Switzerland','Germany','France','Italy','Liechtenstein'],
    mode="text",
    textfont=dict(
    color=['red','purple','orange','blue','green','yellow'],
    size=20,
    family="Arail",)
    ))    
if len(sys.argv)==1:
    print('you have not given any argument')
elif sys.argv[1]==str(0):
    fig.show()

elif sys.argv[1]==str(1):
    fig.write_html('plot5plotly.html',include_plotlyjs='cdn')
    print(os.getcwd()+'\\plot5plotly.html')