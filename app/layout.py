from dash  import html, dcc
import dash_bootstrap_components as dbc

layout = html.Div(
    [
        dbc.Navbar(
            children = [
                        html.H2("Rossman Store")
            ]
        ),
        html.H1("Underperforming Stores"),
        dcc.Graph(id = "low-performing-stores-graph")
    ]
)