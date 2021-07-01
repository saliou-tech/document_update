from pandas.core.reshape import tile
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input ,Output
import pandas as pd 
import plotly.express as px 
import plotly.graph_objs as go
import numpy as np
import pandas as pd 
df=pd.read_csv('faithful.csv')
print(df)
app=dash.Dash()
app.layout=html.Div([
    dcc.Graph(id='old_faithful',
    figure={'data':[go.Scatter(x=df['eruptions'],y=df['waiting'],mode='markers')], 
    'layout':go.Layout(title='exercice with dash')}
    )

])


if __name__=='__main__':
    app.run_server(debug=True)