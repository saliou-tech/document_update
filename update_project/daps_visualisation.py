"""
This app creates a simple sidebar layout using inline style arguments and the
dbc.Nav component.

dcc.Location is used to track the current location, and a callback uses the
current location to render the appropriate page content. The active prop of
each NavLink is set automatically according to the current pathname. To use
this feature you must install dash-bootstrap-components >= 0.11.0.

For more details on building multi-page Dash applications, check out the Dash
documentation: https://dash.plot.ly/urls
"""
import dash
import dash_table
from plotly.offline import init_notebook_mode, iplot
from getKoboData import GetKoboData
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

kobdata=GetKoboData()

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
server=app.server
data_canada = px.data.gapminder().query("country == 'Canada'")

labeld_results=kobdata.getAllData()
data=kobdata.getDapsDataFrame(labeld_results)
print(data)
#labeld_results=kobdata.getAllData()
#data=kobdata.getDapsDataFrame(labeld_results)
# print(data)
# print(data.columns)
# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f7f9f9",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}
link_nav={
"color":"#6D9CCC",
"fontSize":'20px'
}

# navbar = dbc.NavbarSimple(
    
#         dbc.NavItem(dbc.NavLink("Page 1", href="#")),
#         dbc.DropdownMenu(
#             [
#                 dbc.DropdownMenuItem("More pages", header=True),
#                 dbc.DropdownMenuItem("Base de Données", href="#"),
#                 dbc.DropdownMenuItem("Page 3", href="#")
#             ],
#             nav=True,
#             in_navbar=True,
#             label="More",
#         ),
    
#     brand="NavbarSimple",
#     brand_href="#",
#     color="primary",
#     dark=True,
# ),
sidebar = html.Div(
    [
        html.H2("DAPS", className="display-4"),
        html.Hr(),
        # html.P(
        #     "A simple sidebar layout with navigation links", className="lead"
        # ),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact",style=link_nav),
                dbc.NavLink("Base de Donnés ", href="/page-1", active="exact",style=link_nav),
                dbc.NavLink("Page ", href="/page-2", active="exact",style=link_nav),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([
    dcc.Location(id="url"),
    
    sidebar, 

    content])


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return dbc.Row(
            [
                dbc.Col(dbc.Card(
    [
        dbc.CardImg(src="/static/images/placeholder286x180.png", top=True),
        dbc.CardBody(
            [
                html.H4("Card title", className="card-title"),
                html.P(
                    "Some quick example text to build on the card title and "
                    "make up the bulk of the card's content.",
                    className="card-text",
                ),
                dbc.Button("Go somewhere", color="primary"),
            ]
        ),
    ],
    style={"width": "18rem"},
)),
                dbc.Col(dbc.Card(
    [
        dbc.CardImg(src="/static/images/placeholder286x180.png", top=True),
        dbc.CardBody(
            [
                html.H4("Card title", className="card-title"),
                html.P(
                    "Some quick example text to build on the card title and "
                    "make up the bulk of the card's content.",
                    className="card-text",
                ),
                dbc.Button("Go somewhere", color="primary"),
            ]
        ),
       px.bar(data_canada, x='year', y='pop')
#fig.show()
    ],
    style={"width": "18rem"},
)),
                dbc.Col(dbc.Card(
    [
        dbc.CardImg(src="/static/images/placeholder286x180.png", top=True),
        dbc.CardBody(
            [
                html.H4("Card title", className="card-title"),
                html.P(
                    "Some quick example text to build on the card title and "
                    "make up the bulk of the card's content.",
                    className="card-text",
                ),
                dbc.Button("Go somewhere", color="primary"),
            ]
        )
        # iplot([{'x': [1, 2, 3], 'y': [5, 2, 7]}]) 
    ],
    style={"width": "18rem"},
)),
            ]),
    elif pathname == "/page-1":
        return dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in data.columns],
    data=data.to_dict('records'),
)
    elif pathname == "/page-2":
        return html.P("Oh cool, this is page 2!")
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


if __name__ == "__main__":
    app.run_server(debug=True)