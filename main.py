'''
Main Application

Modules are loaded, base website Structure is defined (navbar)

Contains the logical structure of the website and the callback to change to different website views
'''

# Import data modules
import numpy as np
import pandas as pd

# import plot modules
import plotly.express as px
import plotly.graph_objects as go

# Import dash modules
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_daq as daq
from dash.dependencies import Input, Output, State

# import design
import dash_bootstrap_components as dbc

# import ml toolbox
from sklearn.linear_model import LinearRegression

# import app module
from app import server
from app import app

# import apps
from apps import home, linear_regression, gradient_descent, regression_stochastic, markov_decision_process

# import navigation bar
from assets.html.navigation_bar import navbar



def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

for i in [2]:
    app.callback(
        Output(f"navbar-collapse{i}", "is_open"),
        [Input(f"navbar-toggler{i}", "n_clicks")],
        [State(f"navbar-collapse{i}", "is_open")],
    )(toggle_navbar_collapse)

# embedding the navigation bar
app.layout = html.Div(children=[
        dcc.Location(id='url', refresh=False),
        navbar,
        html.Div(id='page-content')
    ])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/home':
        return home.layout
    if pathname == '/linear_regression':
        return linear_regression.layout
    if pathname == '/gradient_descent':
        return gradient_descent.layout
    if pathname == '/stoch_gradient_descent':
        return regression_stochastic.layout
    if pathname == '/MDP':
        return markov_decision_process.layout
    else:
        return home.layout

if __name__ == '__main__':
    app.run_server(debug=True)