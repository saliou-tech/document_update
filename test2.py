from pandas.core.reshape import tile
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input ,Output
import pandas as pd 
import plotly.express as px 


app=dash.Dash()
colors={ 'background':'#111111','text':'#7FDBFF'}

app.layout=html.Div(children=[html.H1('Dash',style={'textAlign':'center','color':colors['text']}),html.Div('Dash:Dashbord for visualisartion using dash'),
dcc.Graph(id='example',
figure={'data':[{'x':[1,2,3],'y':[2,9,4],'type':'bar','name':'SF'},{'x':[1,2,3],'y':[2,6,4],'type':'bar','name':'NYC'}],
'layout':{'title':'BAR PLOT','plot_bgcolor':colors['background'],'paper_bgcolor':colors['background'],'font':colors['text']}})

],style={'backgroundColor':colors['background']})

if __name__=='__main__':
    app.run_server(debug=True)
