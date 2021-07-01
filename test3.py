from pandas.core.reshape import tile
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input ,Output
import pandas as pd 
import plotly.express as px 
import plotly.graph_objs as go
import numpy as np

app=dash.Dash()
#creating data
np.random.seed(40)
random_x=np.random.randint(1,101,100)
random_y=np.random.randint(1,101,100)
app.layout=html.Div([
    dcc.Graph(
        id='scatterplot',
        figure={'data':[
            go.Scatter(x=random_x,y=random_y,mode='markers',
             marker={
                 'size':12,
                 'color':'rgb(51,203,153)',
                 'symbol':'pentagon',
                 'line':{'width':2}

            }
            )
           
        ],
        'layout':go.Layout(title='My scatter plot',xaxis={'title':'some title '})
        }
    ),
    dcc.Graph(
        id='scatterplot2',
        figure={'data':[
            go.Scatter(x=random_x,y=random_y,mode='markers',
             marker={
                 'size':12,
                 'color':'rgb(1,20,13)',
                 'symbol':'pentagon',
                 'line':{'width':2}

            }
            )
           
        ],
        'layout':go.Layout(title='My scatter plot',xaxis={'title':'some title '})
        }
    ),
]
)


if __name__=='__main__':
    app.run_server(debug=True)
