from pandas.core.reshape import tile
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input ,Output
import pandas as pd 
import plotly.express as px 
avocado =pd.read_csv('avocado-updated-2020.csv')

app=dash.Dash()
app.layout=html.Div(
    children=[html.H1(children="Avocado dashboard "),
    dcc.Dropdown(
        id='geo-dropdown',
        options=[{'label':i,'value':i  }
        for i in avocado['geography'].unique()
        ],
        value='new York',
        

    ),dcc.Graph(id='price-graph')]

)
@app.callback(
    Output(
        component_id='price-graph',
        component_property='figure'
    ),
    Input(component_id='geo-dropdown',
        component_property='value'))
def update_graph(selected_geography):
    #print(selected_geography)
    filtered_avocado=avocado[avocado['geography']==selected_geography]
    print(filtered_avocado)
    line_fig=px.line(
        filtered_avocado,
        x='date',y='average_price'
        ,title=f'avocado Price in {selected_geography}'
    )
    return line_fig

if __name__=='__main__':
    app.run_server(debug=True)





