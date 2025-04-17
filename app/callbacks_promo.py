from dash import Input, Output
import plotly.express as px
from database import query_db


def register_callbacks(app):
    @app.callback(
        Output("promo-stores-graph", "figure"),
        Input("low-performing-stores-graph", "id")
    )
    def update_graph(_):
        query = open("scripts/promo_top_effected.sql").read()
        df = query_db(query)
        fig = px.bar(df, x = "Store", y = "total_sales", title = "Top Stores - with Promo")
        return fig
    
