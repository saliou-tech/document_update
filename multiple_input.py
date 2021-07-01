from os import name
from pandas.core.algorithms import mode
from pandas.core.reshape import tile
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input ,Output
import pandas as pd 
import plotly.express as px 
import plotly.graph_objs as go

df=pd.read_csv('mpg.csv')
app=dash.Dash()
features=df.columns 
app.layout=html.Div([
    html.Div([(
        dcc.Dropdown(
            id='xaxis',
            options=[{'label':i,'value':i} for i in features],
            value='displacement'
            )
            )],style={'width':'48%','display':'inline-block'}
            ),
    html.Div([dcc.Dropdown(
        id='yaxis',
        options=[{'label':i,'value':i} for i in features],
        value='mpg'

    )],style={'width':'48%','display':'inline-block'}),
    dcc.Graph(id='feature-graphic')
])
@app.callback(
    Output('feature-graphic','figure'),
    [Input('xaxis','value'),Input('yaxis','value')]
)
def update_graph(xaxis_valus,yaxis_value):
    return {'data':[
        go.Scatter(
            x=df[xaxis_valus],
            y=df[yaxis_value],
            text=df['name'],
            mode='markers',
            marker={'size':15}
        )
    ],'layout':go.Layout(title='My dashboard for MPG',xaxis={'title':xaxis_valus},yaxis={'title':yaxis_value})}

if __name__=='__main__':
    app.run_server(debug=True)