from os import name
from pandas.core.reshape import tile
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input ,Output
import pandas as pd 
import plotly.express as px 
import plotly.graph_objs as go

app=dash.Dash()
df=pd.read_csv('data.csv')
print(df.head())
year_options=[]
for year in df['year'].unique():
    year_options.append({'label':str(year),'value':year})
app.layout=html.Div(
    [
        dcc.Graph(id='graph'),
        dcc.Dropdown(
            id='year-picker',
            options=year_options,
            value=df['year'].min()
        )
    ]
)
@app.callback(
    Output('graph','figure'),
    [Input('year-picker','value')]
)
def update_year(selected_year):
    filtered_df=df[df['year']==selected_year]
    traces=[]
    for continent in filtered_df['continent'].unique():
        df_by_continent=filtered_df[filtered_df['continent']==continent]
        traces.append(
            go.Scatter(
                x=df_by_continent['gdpPercap'],
                y=df_by_continent['lifeExp'],
                mode='markers',
                opacity=0.7,
                marker={'size':15},
                name=continent

            )
        )
    return {'data':traces,'layout':go.Layout(title='My plot',
    xaxis={'title':'GDP par cap','type':'log'},
    yaxis={'title':'life expectency'})
    }
   

# app.layout=html.Div(
#     [
#         dcc.Input(
#             id="my-id",
#             type='text',
         
#             value='initial texte'
#         ),
#         html.Div(id='my-div',style={'border':'2px blue solid '})
#     ]
# )
# @app.callback(
#     Output(component_id='my-div',component_property='children'),
#     [  Input(component_id='my-id',component_property='value'),]

# )
# def update_output_div(input_value):
    #return "you enterred {}".format(input_value)


if __name__=='__main__':
    app.run_server(debug=True)