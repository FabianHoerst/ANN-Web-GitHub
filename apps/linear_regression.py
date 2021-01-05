# Import data modules
import numpy as np
import pandas as pd
import dash

# import plot modules
import plotly.express as px
import plotly.graph_objects as go

# import data generation function
from algorithms.data.data_generation_linear_regression import get_data_points
from algorithms.linear_regression_algorithm import regression

# import ml toolbox
from sklearn.linear_model import LinearRegression
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import dash_daq as daq

from app import app

parameter_input = [dbc.Row(children=[
    dbc.Col(className='md-6', children=[
        'offset',
        daq.NumericInput(
            id='offset',
            value=0,
            min=-1000,
            max=1000,
            disabled=True)
    ])]),
    dbc.Row(children=[
        dbc.Col(className='md-6', children=[
            'a',
            html.Sub(children=['1']),
            daq.NumericInput(
                id='param1',
                value=0,
                min=-1000,
                max=1000,
                disabled=True)
        ]),
        dbc.Col(className='md-6', children=[
            'a',
            html.Sub(children=['2']),
            daq.NumericInput(
                id='param2',
                min=-1000,
                max=1000,
                value=0,
                disabled=True)
        ]),
        dbc.Col(className='md-6', children=[
            'a',
            html.Sub(children=['3']),
            daq.NumericInput(
                id='param3',
                min=-1000,
                max=1000,
                value=0,
                disabled=True)
        ])]),
    dbc.Row(children=[
        dbc.Col(className='md-6', children=[
            'a',
            html.Sub(children=['4']),
            daq.NumericInput(
                id='param4',
                min=-1000,
                max=1000,
                value=0,
                disabled=True)
        ]),
        dbc.Col(className='md-6', children=[
            'a',
            html.Sub(children=['5']),
            daq.NumericInput(
                id='param5',
                min=-1000,
                max=1000,
                value=0,
                disabled=False)
        ]),
        dbc.Col(className='md-6', children=[
            'a',
            html.Sub(children=['6']),
            daq.NumericInput(
                id='param6',
                value=0,
                min=-1000,
                max=1000,
                disabled=False)
        ]),
    ])]

layout = html.Div([
    dbc.Container(className='center', children=[
        dbc.Row(children=[
            dbc.Col(className='center', children=[
                html.H1(children='Introduction to linear regression')
            ])
        ]),
        dbc.Progress(value=100, style={"height": "2px"}, className="mb-3"),
        dbc.Row(children=[
            dbc.Col(dbc.Card(color="dark", className="mb-4",
                children=[
                    dbc.CardHeader("Settings"),
                    dbc.CardBody([
                        dbc.Row(children=[dbc.Col(
                            html.H6(children=['Order of the ground-truth function']), )
                        ]),
                        dbc.Row(children=[dbc.Col(
                            dcc.Dropdown(
                                options=[
                                    {'label': '1 (linear regression)', 'value': 1},
                                    {'label': '2 (polynomial regression)', 'value': 2},
                                    {'label': '3 (polynomial regression)', 'value': 3},
                                    {'label': '4 (polynomial regression)', 'value': 4},
                                    {'label': '5 (polynomial regression)', 'value': 5},
                                    {'label': '6 (polynomial regression)', 'value': 6},
                                ],
                                clearable=False,
                                id='order',
                                style={'background-color': 'white',
                                       'color': 'black'}
                            ))]),
                        dbc.Row(children=[dbc.Col(
                            html.H6(children=['Select which regression should be shown']), )
                        ]),
                        dbc.Row(children=[dbc.Col(
                            dcc.Dropdown(
                                options=[
                                    {'label': '1 (linear regression)', 'value': 1},
                                    {'label': '2 (polynomial regression)', 'value': 2},
                                    {'label': '3 (polynomial regression)', 'value': 3},
                                    {'label': '4 (polynomial regression)', 'value': 4},
                                    {'label': '5 (polynomial regression)', 'value': 5},
                                    {'label': '6 (polynomial regression)', 'value': 6},
                                ],
                                multi=True,
                                id='order_reg',
                                style={'background-color': 'white',
                                        'color': 'black'}
                            ))
                        ]),
                        dbc.Row(children=[
                            dbc.Col(className='mb-4', md=4, children=[
                                dbc.Row(children=[dbc.Col(
                                    html.H6(children=[
                                        'Noise'
                                    ]))
                                ]),
                                dbc.Row(children=[dbc.Col(
                                    daq.NumericInput(
                                        id='noise',
                                        min=0,
                                        max=100,
                                        size=80,
                                        value=1,
                                        disabled=False
                                    ))
                                ])
                            ]),
                            dbc.Col(className='mb-4', md=4, children=[
                                dbc.Row(children=[dbc.Col(
                                    html.H6(children=[
                                        'Min x value'
                                    ]))
                                ]),
                                dbc.Row(children=[dbc.Col(
                                    daq.NumericInput(
                                        id='x-range1',
                                        max=0,
                                        min=-10000,
                                        size=80,
                                        value=-5,
                                        disabled=False
                                    ))
                                ]),
                            ]),
                            dbc.Col(className='mb-4', md=4, children=[
                                dbc.Row(children=[dbc.Col(
                                    html.H6(children=[
                                        'Max x value'
                                    ]))
                                ]),
                                dbc.Row(children=[dbc.Col(
                                    daq.NumericInput(
                                        id='x-range2',
                                        min=0.1,
                                        max=10000,
                                        size=80,
                                        value=5,
                                        disabled=False
                                    ))
                                ]),
                            ]),
                        ]),
                        dbc.Row(children=[
                            dbc.Col(className='md-12', children=[
                                html.H6(children=[
                                    'Number of Data Points'
                                ]),
                                dcc.Slider(
                                    id='data_point_number',
                                    min=10,
                                    max=1000,
                                    step=10,
                                    value=100,
                                    marks={
                                        10: '10',
                                        200: '200',
                                        400: '400',
                                        600: '600',
                                        800: '800',
                                        1000: '1000'
                                    },
                                ),
                                html.Br(),
                            ])
                        ]),
                        dbc.Row(children=[
                            dbc.Col(className='md-12', children=[
                                dbc.Progress(value=100, style={"height": "2px"}, className="mb-3"),
                                html.H6(children=[
                                    'Parameters of the ground-truth function'
                                ]),
                                html.Div(children=parameter_input)
                            ])
                        ]),
                        dbc.Row(children=[
                            dbc.Col(className='md-12', children=[
                                html.Br(),
                            ])]),
                        dbc.Row(children=[
                            dbc.Col(className='md-12', children=[
                                dbc.Button("Generate new random noise", color="primary", block=True, n_clicks=0, id="noise_button"),
                            ])
                        ])]
                    ),
                ]), md=4, className="mb-4"),
            dbc.Col(dbc.Card(color="dark", inverse=True, children=[
                    dbc.CardHeader("Plot"),
                    dbc.CardBody([
                        dbc.Row(children=[
                            dbc.Col(children=[
                                dcc.Graph(id='scatter-plot', config={'displayModeBar': True}, animate=True)
                            ])
                        ])
                    ]),
        ]), md=8, className="mb-8")
        ]),
    ])
])


# Callback for oder
@app.callback([Output('param6', 'disabled'), Output('param5', 'disabled'),
               Output('param4', 'disabled'), Output('param3', 'disabled'), Output('param2', 'disabled'),
               Output('param1', 'disabled'), Output('offset', 'disabled')],
              [Input('order', 'value')])
def update_output(value):
    if value == 1:
        return (True, True, True, True, True, False, False)
    elif value == 2:
        return (True, True, True, True, False, False, False)
    elif value == 3:
        return (True, True, True, False, False, False, False)
    elif value == 4:
        return (True, True, False, False, False, False, False)
    elif value == 5:
        return (True, False, False, False, False, False, False)
    elif value == 6:
        return (False, False, False, False, False, False, False)
    else:
        return (True, True, True, True, True, True, True)


# Callback for oder
@app.callback(Output('scatter-plot', 'figure'),
              [Input('order_reg', 'value'), Input('order', 'value'),
               Input('param6', 'value'), Input('param5', 'value'), Input('param4', 'value'),
               Input('param3', 'value'), Input('param2', 'value'), Input('param1', 'value'),
               Input('offset', 'value'), Input('data_point_number', 'value'),
               Input('x-range1', 'value'), Input('x-range2', 'value'), Input('noise', 'value'), Input('noise_button', 'n_clicks')
               ])
def update_output(order_reg, order, param6, param5, param4, param3, param2, param1, offset, data_point_number, x_min,
                  x_max, noise, n_clicks):
    # random_state
    # build the data
    x_val, y_val, x_ground_truth, y_ground_truth = get_data_points(param6, param5, param4, param3, param2, param1,
                                                                   offset,
                                                                   data_point_number, x_min, \
                                                                   x_max, noise, n_clicks)

    # build figure
    figure = px.scatter(template='plotly_dark', range_x=(1.2 * x_min, 1.2 * x_max),
                        range_y=(-1.2 * max(abs(y_val)), 1.2 * max(abs(y_val)))
                        ).update_layout(
        {'title': 'Dash Data Visualization'
         })
    figure.add_trace(go.Scatter(x=x_val, y=y_val, mode='markers', name='Data points'))
    figure.add_trace(go.Scatter(x=x_ground_truth, y=y_ground_truth, mode='lines', name='Ground Truth'))

    # regression
    if order_reg is None:
        order_reg = [0]
    if 1 in order_reg:
        theta_1, y_pred = regression(1, x_val, y_val, x_ground_truth)
        figure.add_trace(go.Scatter(x=x_ground_truth, y=y_pred, mode='lines', name='Reg 1st order'))
    if 2 in order_reg:
        theta_2, y_pred = regression(2, x_val, y_val, x_ground_truth)
        figure.add_trace(go.Scatter(x=x_ground_truth, y=y_pred, mode='lines', name='Reg 2nd order'))
    if 3 in order_reg:
        theta_3, y_pred = regression(3, x_val, y_val, x_ground_truth)
        figure.add_trace(go.Scatter(x=x_ground_truth, y=y_pred, mode='lines', name='Reg 3th order'))
    if 4 in order_reg:
        theta_4, y_pred = regression(4, x_val, y_val, x_ground_truth)
        figure.add_trace(go.Scatter(x=x_ground_truth, y=y_pred, mode='lines', name='Reg 4th order'))
    if 5 in order_reg:
        theta_5, y_pred = regression(5, x_val, y_val, x_ground_truth)
        figure.add_trace(go.Scatter(x=x_ground_truth, y=y_pred, mode='lines', name='Reg 5th order'))
    if 6 in order_reg:
        theta_6, y_pred = regression(6, x_val, y_val, x_ground_truth)
        figure.add_trace(go.Scatter(x=x_ground_truth, y=y_pred, mode='lines', name='Reg 6th order'))

    return figure