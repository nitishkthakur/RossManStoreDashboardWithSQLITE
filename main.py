from dash import Dash
from app.layout import layout
from app.callbacks import register_callbacks
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets = [dbc.themes.BOOTSTRAP], suppress_callback_exceptions = True)
app.layout = layout
register_callbacks(app)

server = app.server  # for gunicorn

if __name__ == "__main__":
    app.run_server(debug=True, port = 8050)
