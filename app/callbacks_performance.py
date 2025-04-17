from dash import Input, Output
import plotly.express as px
from database import query_db


def register_callbacks(app):
    @app.callback(
        Output("low-performing-stores-graph", "figure"),
        Input("low-performing-stores-graph", "id")
    )
    def update_graph(_):
        query = open("scripts/underperformers.sql").read()
        df = query_db(query)
        fig = px.bar(df, x = "Store", y = "avg_sales", title = "Underperforming Stores")
        return fig
    
