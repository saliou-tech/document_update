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
import base64
df=pd.read_csv('wheels.csv')
print(df)
app=dash.Dash()
server=app.server
def encodeImage(imagefile):
    encoded=base64.b64encode(open(imagefile,'rb').read())
    return 'data:image/png;base64,{}'.format(encoded.decode())
app.layout=html.Div(
    [
        dcc.RadioItems(
            id='wheels',
            options=[{'label':i,'value':i} for i in df['wheels'].unique()],
            value=1
        ),
        html.Div(id='wheels-output'),
        html.Hr(),
        dcc.RadioItems(id='colors',options=[{'label':i,'value':i} for i in df['color'].unique()],
            value=1),
        html.Div(id='colors-output'),
        html.Img(id='display-image',src='children',height=300)



    ],style={'fontFamily':'helvetica','fontSize':15}
)
@app.callback(
    Output('wheels-output','children'),
    [Input('wheels','value')]
)
def calback_a(wheels):
    return "you choose :{} ".format(wheels)

@app.callback(
    Output('colors-output','children'),
    [Input('colors','value')]
)
def calback_b(colors):
    return "you choose :{} :".format(colors)


@app.callback(
    Output('display-image','src'),
    [Input('wheels','value'),Input('colors','value')]
)
def callback_image(whells,color):
    path='data/images/'
    print(df[(df['wheels'] == whells )& (df['color']==color)]['image'].values[0])
    return encodeImage(path+df[(df['wheels'] == whells )& (df['color']==color)]['image'].values[0])
if __name__=='__main__':
    app.run_server(debug=True)