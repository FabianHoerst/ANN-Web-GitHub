# Import data modules
import numpy as np
import pandas as pd
import dash
import dash_table

# import plot modules
import plotly.express as px
import plotly.graph_objects as go

# import data generation function
from algorithms.gradient_descent_algorithms import gradient_descent_alg

# import ml toolbox
from sklearn.linear_model import LinearRegression
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import dash_daq as daq
import dash_gif_component as Gif

from app import app

layout = html.Div([
    dbc.Container(className='center', children=[
        dbc.Row(children=[
            dbc.Col(className='center', children=[
                html.H1(children='Different realizations of linear Regression')
            ])
        ]),
        dbc.Progress(value=100, style={"height": "2px"}, className="mb-3"),
        dbc.Row(children=[
                dbc.Col(dbc.Card(html.H5(children='Batch-Regression, Stochastic Regression and Mini-Batch Regression '
                                                  'under the assumptions, that the number of features is known',
                                         className="text-center text-light bg-primary"), body=True, color="primary"))],
                className="mt-4 mb-4"),
        dbc.Row(children=[
            dbc.Col(dbc.Card(color="dark", className="mb-4", children=[
                 dbc.CardHeader("Settings"),
                    dbc.CardBody(children=[
                        dbc.Row(children=[dbc.Col(
                            html.H4(children=['Batch-Regression']), )
                        ]),
                        dbc.Row(children=[dbc.Col(
                            html.H6(children=['Learning Rate divided by 1000']), )
                        ]),
                        dbc.Row(children=[
                            dbc.Col(
                                daq.NumericInput(
                                    id='learning_rate_batch',
                                    min=1,
                                    max=1000,
                                    size=200,
                                    value=100,
                                    disabled=False
                                )
                            )
                        ]),
                        dbc.Row(children=[dbc.Col(
                            html.H6(id='learning_rate_batch_div'))
                        ]),
                        dbc.Row(children=[dbc.Col(
                            html.H6(children=['Number of Iterations']), )
                        ]),
                        dbc.Row(children=[
                            dbc.Col(
                                daq.NumericInput(
                                    id='iterations_batch',
                                    min=2,
                                    max=10000,
                                    size=200,
                                    value=100,
                                    disabled=False
                                )
                            )
                        ]),
                        dbc.Row(children=[dbc.Col(
                                                    html.Br())
                                                ]),
                        dbc.Row(children=[dbc.Col(
                            html.H4(children=['Stochastic-Regression']), )
                        ]),
                        dbc.Row(children=[dbc.Col(
                            html.H6(children=['Learning Rate divided by 1000']), )
                        ]),
                        dbc.Row(children=[
                            dbc.Col(
                                daq.NumericInput(
                                    id='learning_rate_batch',
                                    min=1,
                                    max=1000,
                                    size=200,
                                    value=100,
                                    disabled=False
                                )
                            )
                        ]),
                        dbc.Row(children=[dbc.Col(
                            html.H6(id='learning_rate_batch_div'))
                        ]),
                        dbc.Row(children=[dbc.Col(
                            html.H6(children=['Number of Iterations']), )
                        ]),
                        dbc.Row(children=[
                            dbc.Col(
                                daq.NumericInput(
                                    id='iterations_batch',
                                    min=2,
                                    max=10000,
                                    size=200,
                                    value=100,
                                    disabled=False
                                )
                            )
                        ]),
                        dbc.Row(children=[dbc.Col(
                                                    html.Br())
                                                ]),
                        dbc.Row(children=[dbc.Col(
                            html.H4(children=['Batch-Regression']), )
                        ]),
                        dbc.Row(children=[dbc.Col(
                            html.H6(children=['Learning Rate divided by 1000']), )
                        ]),
                        dbc.Row(children=[
                            dbc.Col(
                                daq.NumericInput(
                                    id='learning_rate_batch',
                                    min=1,
                                    max=1000,
                                    size=200,
                                    value=100,
                                    disabled=False
                                )
                            )
                        ]),
                        dbc.Row(children=[dbc.Col(
                            html.H6(id='learning_rate_batch_div'))
                        ]),
                        dbc.Row(children=[dbc.Col(
                            html.H6(children=['Number of Iterations']), )
                        ]),
                        dbc.Row(children=[
                            dbc.Col(
                                daq.NumericInput(
                                    id='iterations_batch',
                                    min=2,
                                    max=10000,
                                    size=200,
                                    value=100,
                                    disabled=False
                                )
                            )
                        ]),
                        dbc.Row(children=[dbc.Col(
                            html.Br())
                        ]),
                        dbc.Row(children=[
                            dbc.Col(className='md-12', children=[
                                dbc.Button("Generate new random noise", color="primary", block=True, n_clicks=0, id="noise_button"),
                            ])
                        ])
                 ]),
            ]), md=4, className="mb-4"),
            dbc.Col(children=[
                dbc.Card(color="dark", inverse=True, children=[
                    dbc.CardHeader("Plot"),
                    dbc.CardBody([
                        ])
                    ]),
                dbc.Row(children=[dbc.Col(
                    html.Br())
                ]),
                dbc.Card(color="dark", inverse=True, children=[
                    dbc.CardHeader("Plot"),
                    dbc.CardBody([
                        ])
                    ])
            ], md=8, className="mb-8")
        ]),
    ])
])

