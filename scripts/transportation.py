import os
import sys
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
df = pd.read_csv('applemobility.csv', sep=",", error_bad_lines=False, index_col=2)
#filter Switzerland
df=df[df['region']=='Switzerland']
df=df.drop(columns=['region','alternative_name','geo_type']).T
df=df.reset_index()
df=df.rename(columns={'index':'date'})
df=df.melt(id_vars=["date"], 
        var_name="transportation", 
        value_name="value")



fig = px.line(df, x='date',y='value',color='transportation',range_x=['2020-01-10','2020-05-20'],range_y=[0,165],
              color_discrete_sequence=['red','purple','orange'],hover_name='value',hover_data=['date'])

fig.update_yaxes(tickvals=[40, 80, 120, 160])
fig.update_xaxes(
    ticktext=['Jan 15 <br> 2020',"Feb 1",'Feb 15','Mar 1','Mar 15','Apr 1','Apr 15','May 1'],
    tickvals=['2020-01-15',"2020-02-01","2020-02-15","2020-03-01","2020-03-15","2020-04-01","2020-04-15","2020-05-01"],
)
fig.update_yaxes(
    ticktext=['-60%',"-20%",'+20%','+60%'],
    tickvals=[ 40,80,120,160]
)
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
        'text': "Switzerland mobility",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top',
        'font': dict(
        size=25)
        },
    shapes=[dict(
                type="line",
                yref='y1',
                y0=100,
                y1=100,
                xref='x1',
                x0='2020-01-10',
                x1='2020-04-28',
                line=dict(
                    color="grey",
                    width=2,
                    ))]
    )
fig.add_trace(go.Scatter(
    x=['2020-05-10','2020-05-10','2020-05-10','2020-05-10'],
    y=[100,73.68,38.42,58.86],
    text=['Baseline','driving -26%','transit -62%','walking -41%'],
    mode="text",
    textfont=dict(
    color=['black','red','purple','orange'],
    size=20,
    family="Arail",
    )
))
    
if len(sys.argv)==1:
    print('you have not given any argument')
elif sys.argv[1]==str(0):
    fig.show()

elif sys.argv[1]==str(1):
    fig.write_html('plot1plotly.html',include_plotlyjs='cdn')
    print(os.getcwd()+'\\plot1plotly.html')