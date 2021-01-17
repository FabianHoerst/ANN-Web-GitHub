'''
Code for the /gradient_descent webapp
'''

# Import data modules
import numpy as np

# import plot modules
import plotly.express as px
import plotly.graph_objects as go

# import data generation function
from algorithms.gradient_descent_algorithms import gradient_descent_alg

# import ml toolbox
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import dash_daq as daq

from app import app

# build the layout
layout = html.Div([
    dbc.Container(className='center', children=[
        dbc.Row(children=[
            dbc.Col(className='center', children=[
                html.H1(children='Gradient descent algorithms')
            ])
        ]),
        dbc.Progress(value=100, style={"height": "2px"}, className="mb-3"),
        dbc.Row(children=[
                dbc.Col(dbc.Card(html.H3(children='Example with one local minimum',
                                         className="text-center text-light bg-primary"), body=True, color="primary"))],
                className="mt-4 mb-4"),
        dbc.Row(children=[
            dbc.Col(dbc.Card(color="dark", className="mb-4", children=[
                 dbc.CardHeader("Settings"),
                 dbc.CardBody(children=[
                    dbc.Row(children=[dbc.Col(
                        html.H5(children=['Starting point']))
                    ]),
                    dbc.Row(children=[
                        dbc.Col(
                            daq.NumericInput(
                                id='starting_point',
                                min=-5,
                                max=5,
                                size=200,
                                value=2,
                                disabled=False
                            )
                        )
                    ]),
                    dbc.Row(children=[dbc.Col(
                        html.Br())
                    ]),
                    dbc.Row(children=[dbc.Col(
                        html.H5(children=['Learning Rate divided by 1000']))
                    ]),
                    dbc.Row(children=[
                        dbc.Col(
                            daq.NumericInput(
                                id='learning_rate',
                                min=1,
                                max=1200,
                                size=200,
                                value=100,
                                disabled=False
                            )
                        )
                    ]),
                    dbc.Row(children=[dbc.Col(
                        html.H6(id='learning_rate_div'))
                    ]),
                    dbc.Row(children=[dbc.Col(
                        html.Br())
                    ]),
                    dbc.Row(children=[dbc.Col(
                        html.H5(children=['Number of Iterations']))
                    ]),
                    dbc.Row(children=[
                        dbc.Col(
                            daq.NumericInput(
                                id='iterations',
                                min=2,
                                max=10000,
                                size=200,
                                value=5,
                                disabled=False
                            )
                        )
                    ]),
                    dbc.Row(children=[dbc.Col(
                        html.Br())
                    ]),
                    dbc.Row(children=[dbc.Col(
                        html.H5(children=['Example configuration parameters']))
                    ]),
                    dbc.Row(children=[
                        dbc.Col(children=[
                            dcc.Markdown('''
                            | Starting Point | Learning Rate | Iterations |
                            |:--------------:|:-------------:|:----------:|
                            |        4       |      950      |     20     |
                            |        4       |      1000     |     20     |
                            |        1       |      1100     |     10     |
                            ''')
                        ])
                    ])
                 ]),
            ]), md=4, className="mb-4"),
            dbc.Col(dbc.Card(color="dark", inverse=True, children=[
                dbc.CardHeader("Plot"),
                dbc.CardBody([
                    dbc.Row(children=[
                        dbc.Col(children=[
                            dcc.Graph(id='gradient-plot-1', config={'displayModeBar': True}, animate=True)
                        ])
                    ])
                ]),
            ]), md=8, className="mb-8")
        ]),
        dbc.Row(children=[
                dbc.Col(dbc.Card(html.H3(children='Example with two different local minima',
                                         className="text-center text-light bg-primary"), body=True, color="primary"))],
                className="mt-4 mb-4"),
        dbc.Row(children=[
            dbc.Col(dbc.Card(color="dark", className="mb-4", children=[
                dbc.CardHeader("Settings"),
                dbc.CardBody(children=[
                    dbc.Row(children=[dbc.Col(
                        html.H5(children=['Starting point']))
                    ]),
                    dbc.Row(children=[
                        dbc.Col(
                            daq.NumericInput(
                                id='starting_point2',
                                min=-15,
                                max=9,
                                size=200,
                                value=2.5,
                                disabled=False
                            )
                        )
                    ]),
                    dbc.Row(children=[dbc.Col(
                        html.Br())
                    ]),
                    dbc.Row(children=[dbc.Col(
                        html.H5(children=['Learning Rate divided by 1000']), )
                    ]),
                    dbc.Row(children=[
                        dbc.Col(
                            daq.NumericInput(
                                id='learning_rate2',
                                min=1,
                                max=1000,
                                size=200,
                                value=100,
                                disabled=False
                            )
                        )
                    ]),
                    dbc.Row(children=[dbc.Col(
                        html.H6(id='learning_rate_div2'))
                    ]),
                    dbc.Row(children=[dbc.Col(
                        html.Br())
                    ]),
                    dbc.Row(children=[dbc.Col(
                        html.H5(children=['Number of Iterations']), )
                    ]),
                    dbc.Row(children=[
                        dbc.Col(
                            daq.NumericInput(
                                id='iterations2',
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
                        html.H5(children=['Example configuration parameters']))
                    ]),
                    dbc.Row(children=[
                        dbc.Col(children=[
                            dcc.Markdown('''
                            | Starting Point | Learning Rate | Iterations |
                            |:--------------:|:-------------:|:----------:|
                            |        -2      |      100      |     100    |
                            |        -15     |      150      |     100    |
                            |         9      |      350      |     100    |
                            ''')
                        ])
                    ])
                ]),
            ]), md=4, className="mb-4"),
            dbc.Col(dbc.Card(color="dark", inverse=True, children=[
                dbc.CardHeader("Plot"),
                dbc.CardBody([
                    dbc.Row(children=[
                        dbc.Col(children=[
                            dcc.Graph(id='gradient-plot-2', config={'displayModeBar': True}, animate=True)
                        ])
                    ])
                ]),
            ]), md=8, className="mb-8")
        ]),
    ])
])

# function1
def function1(x):
    return x**2
def dfunction1(x):
    return 2*x

# function2
def function2(x):
    return 0.01 * x ** 4 + 0.1 * x ** 3 - x ** 2 - 4 * x + 12
def dfunction2(x):
    return 0.04*x**3 + 0.3*x**2 -2*x -4

# Callbacks

# Callback 1 for visualization 1
@app.callback([Output('gradient-plot-1', 'figure'), Output('learning_rate_div', 'children')],
              [Input('starting_point', 'value'), Input('learning_rate', 'value'), Input('iterations', 'value')])
def update_output(starting_point1, learning_rate1, iterations1):
    # build x and y values
    x1 = np.linspace(-5, 5, 1000)
    y1 = function1(x1)

    # plot function
    figure1 = px.scatter(template='plotly_dark', range_x=(-5, 5),
                        range_y=(-2, 1.2 * max(y1))
                        ).update_layout(
        {'title': 'Dash Data Visualization',
         'xaxis_title': "theta",
         'yaxis_title': "Loss",
         })
    figure1.add_trace(go.Scatter(x=x1, y=y1, mode='lines', name='L(theta,x,y)'))

    # plot ground truth
    figure1.add_trace(go.Scatter(x=[0], y=[0], mode='markers', marker_symbol='x',
                                 marker=dict(size=[20]), name='Minimum ground truth'))

    # plot starting point
    figure1.add_trace(go.Scatter(x=[starting_point1], y=[function1(starting_point1)], mode='markers', marker_symbol='x',
                                 marker=dict(size=[20]), name='Starting point'))

    # perform gradient descent algorithm and plot the results
    try:
        theta_min1, theta1, y_iterations1 = gradient_descent_alg(function1, dfunction1, starting_point1, learning_rate1/1000, iterations1)
        figure1.add_trace(go.Scatter(x=[theta_min1], y=[function1(theta_min1)], mode='markers', marker_symbol='x',
                                     marker=dict(size=[20]), name='Minimum gradient descent'))
        figure1.add_trace(go.Scatter(x=theta1, y=y_iterations1, mode='markers+lines', name='Iteration steps'))
        return figure1, ['Learning Rate: ', learning_rate1/1000]
    except:
        return figure1, [html.Div(className="alert alert-dismissible alert-danger", children=[
            'Value selected to high! No convergence! Gradient descent failed'])]


# Callback 2 for visualization 2
@app.callback([Output('gradient-plot-2', 'figure'), Output('learning_rate_div2', 'children')],
              [Input('starting_point2', 'value'), Input('learning_rate2', 'value'), Input('iterations2', 'value')])
def update_output(starting_point2, learning_rate2, iterations2):
    # build x and y values
    x2 = np.linspace(-15, 10, 1000)
    y2 = function2(x2)
    # set optimal values for plotting
    x2_min = np.array([-11.173717371737, 5.347134713471])
    y2_min = function2(x2_min)

    # plot function
    figure2 = px.scatter(template='plotly_dark', range_x=(-15, 10),
                         range_y=(1.2*min(y2), 1.2*max(y2))
                         ).update_layout(
        {'title': 'Dash Data Visualization',
         'xaxis_title': "theta",
         'yaxis_title': "Loss",
         })
    figure2.add_trace(go.Scatter(x=x2, y=y2, mode='lines', name='L(theta,x,y)'))

    # plot ground truth
    figure2.add_trace(go.Scatter(x=x2_min, y=y2_min, mode='markers', marker_symbol='x',
                                 marker=dict(size=[20]), name='Minimum ground truth'))

    # plot starting point
    figure2.add_trace(go.Scatter(x=[starting_point2], y=[function2(starting_point2)], mode='markers', marker_symbol='x',
                                 marker=dict(size=[20]), name='Starting point'))

    # perform gradient descent algorithm and plot the results
    try:
        theta_min2, theta2, y_iterations2 = gradient_descent_alg(function2, dfunction2, starting_point2,
                                                                 learning_rate2 / 1000, iterations2)
        figure2.add_trace(go.Scatter(x=[theta_min2], y=[function2(theta_min2)], mode='markers', marker_symbol='x',
                                     marker=dict(size=[20]), name='Minimum gradient descent'))
        figure2.add_trace(go.Scatter(x=theta2, y=y_iterations2, mode='markers+lines', name='Iteration steps'))
        return figure2, ['Learning Rate: ', learning_rate2 / 1000]
    except:
        return figure2, [html.Div(className="alert alert-dismissible alert-danger", children=[
            'Value selected to high! No convergence! Gradient descent failed'])]