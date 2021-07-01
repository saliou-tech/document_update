import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import dash
import dash_table




app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
server=app.server
# labeld_results=kobdata.getAllData()
# data=kobdata.getDapsDataFrame(labeld_results)
# print(data)
