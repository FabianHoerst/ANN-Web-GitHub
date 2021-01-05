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
import plotly.figure_factory as ff

from app import app
from algorithms import mdp
from algorithms.data.robot_mdp import *


layout = html.Div([
    dbc.Container(className='center', children=[
        dbc.Row(children=[
            dbc.Col(className='center', children=[
                html.H1(children='Project 1: MDP')
            ])
        ]),
        dbc.Row(children=[
            dbc.Col(className='center', children=[
                dcc.Markdown(
                    '''
                    ## Decision Making under uncertainty: Markov Decision Process

                    Decision making and planning are core problems in the field of Artificial Intelligence. Decision making describes the cognitive process of taking the best action in a given environment. If a sequence of actions is executed, this is called sequential decision making. 
                    It is important to consider uncertainty in decision making. Real environments behave stochastically and are only partially observable. For example, during a measurement, the measured values may be noisy, resulting in an uncertain measured value about which no 100% reliable statements can be made. On the other hand, processes can also have a non-deterministic outcome, whereby the desired result is not achieved with a certain probability when an action is performed. In order to represent these uncertainties, the concept of the Markov Decision Processes (MDPs) was introduced.
                    
                    ### Mathematical description
                    Definition: A markov decision process is defined as a tupel
                    
                    ![def](assets/pictures/1.png)
                    
                    with: 
                     - S a finite set of states
                     - A a finite set of actions
                     - P: S x A x S -> R, transition probabilities
                     - R: S x A x S -> R, rewards
                     - discount factor between 0 and 1
                     
                    Please notice:
                    
                    ![mdp_tupel](assets/pictures/2.png)
                    
                    
                    ### Policy
                    A policy is a mapping from states to actions. A policy thus specifies which action a is to be executed when one 
                    is in a state s.
                    ### Evaluation of a policy: Bellman Equation
                    The value function V assigns to each states the value V(s) = E(Gt|st=s), where st is the state at time step t.
                    Writing V and R as vectors the above equation becomes 
                    
                    ![def](assets/pictures/5_1.png)
                    
                    and hence
                    
                    ![definition](assets/pictures/4.png)
                    
                    This is called the Bellman equation.
                    
                    ### Find the optimal policy: Value iteration
                    Given a MDP, we want to find the policy such that the corresponding value function is maximal and hence, 
                    the expected reward. 
                    To achieve that goal, an algorithm called value iteration is used.
                    You can find it in the source below.
                    
                    Thanks to: https://ipvs.informatik.uni-stuttgart.de/mlr/wp-content/uploads/2016/04/02-MarkovDecisionProcess.pdf
                    
                    The source code for the MDP can be found here: https://github.com/FabianHoerst/MDP
                    '''
                )
            ])
        ]),
        dbc.Progress(value=100, style={"height": "2px"}, className="mb-3"),
        dbc.Row(children=[
            dbc.Col(className='center', children=[
                dcc.Markdown(
                    '''
                    ## Example: Grid Robot MDP
                    Consider a grid with a robot. The robot can move from one cell to another cell. 
                    The robot can move in the directions 'up', 'down', 'left' and 'right'. These are the executable 
                    actions. The state set contains the discrete coordinates (grid coordinates) and describes the 
                    position of the robot. Due to different environmental conditions, the robot moves only with 
                    the probability p=0.8 in the desired direction. However, with each probability p=0.1 the robot moves
                    into the laterally adjacent fields. If there is no adjacent field or if this field is a wall, 
                    the robot remains in its current state. The fields with the values +1 and -1 describe rewards that 
                    the robot receives when it reaches this field. These fields(states) are absorbing and are modeled 
                    by the robot always staying on these fields when performing an action. 
                    The movement of the robot is assigned a cost, which can be set variably. 

                    '''
                )
            ])
        ]),
        dbc.Row(children=[
            dbc.Col(dbc.Card(color="dark", className="mb-4",
                children=[
                    dbc.CardHeader("Settings"),
                    dbc.CardBody([
                        dbc.Row(children=[
                            dbc.Col(className='md-12', children=[
                                html.H6(children=[
                                    'Discount Factor'
                                ]),
                                dcc.Slider(
                                    id='gamma',
                                    min=0.001,
                                    max=0.999,
                                    step=0.001,
                                    value=0.9,
                                    marks={
                                        0.1: '0.1',
                                        0.2: '0.2',
                                        0.3: '0.3',
                                        0.4: '0.4',
                                        0.5: '0.5',
                                        0.6: '0.6',
                                        0.7: '0.7',
                                        0.8: '0.8',
                                        0.9: '0.9',
                                    },
                                ),
                            ])
                        ]),
                        dbc.Row(children=[dbc.Col(
                            html.H6(id='gamma_div'))
                        ]),
                        dbc.Row(children=[
                            dbc.Col(className='md-12', children=[
                                html.Br()
                            ])
                        ]),
                        dbc.Row(children=[
                            dbc.Col(className='md-12', children=[
                                html.H6(children=[
                                    'Step costs'
                                ]),
                                dcc.Slider(
                                    id='costs',
                                    min=-1,
                                    max=0,
                                    step=0.01,
                                    value=-0.04,
                                    marks={
                                        -0.1: '-0.1',
                                        -0.2: '-0.2',
                                        -0.3: '-0.3',
                                        -0.4: '-0.4',
                                        -0.5: '-0.5',
                                        -0.6: '-0.6',
                                        -0.7: '-0.7',
                                        -0.8: '-0.8',
                                        -0.9: '-0.9',
                                    },
                                ),
                            ])
                        ]),
                        dbc.Row(children=[dbc.Col(
                            html.H6(id='cost_div'))
                        ]),
                        dbc.Row(children=[
                            dbc.Col(className='md-12', children=[
                                html.Br()
                            ])
                        ]),
                        dbc.Row(children=[dbc.Col(
                            html.H6(children=['Policy']), )
                        ]),
                        dbc.Row(children=[dbc.Col(
                            dcc.Dropdown(
                                options=[
                                    {'label': 'Policy 1', 'value': 1},
                                    {'label': 'Policy 2', 'value': 2},
                                    {'label': 'Policy 3', 'value': 3},
                                    {'label': 'Optimal Policy', 'value': 4},
                                ],
                                clearable=False,
                                id='policy_selection',
                                style={'background-color': 'white',
                                       'color': 'black'}
                            ))]),
                    ]),
                ]), md=4, className="mb-4"),
            dbc.Col(dbc.Card(color="dark", inverse=True, children=[
                    dbc.CardHeader("Grid"),
                    dbc.CardBody([
                        dbc.Row(children=[
                            dbc.Col(children=[
                                dcc.Graph(id='heatmap-plot', config={'displayModeBar': True}, animate=False)
                            ])
                        ])
                    ]),
            ]), md=8, className="mb-8")
        ]),
    ])
])

# Callback for oder
@app.callback([Output('heatmap-plot', 'figure'), Output('cost_div', 'children'), Output('gamma_div', 'children'),],
              [Input('gamma', 'value'), Input('costs', 'value'), Input('policy_selection', 'value')])
def update_output(gamma, costs, policy_selection):

    markov_Robot = generate_Robot_MDP(costs)
    z_text = [['', '', '', ''],
              ['', '', '', '-1'],
              ['', '', '', '1']]

    if policy_selection == 1:
        policy_value = markov_Robot.bellman_eq_policy(policy1, gamma)
        z_text = plot_z(policy1, z_text, policy_value)
    elif policy_selection == 2:
        policy_value = markov_Robot.bellman_eq_policy(policy2, gamma)
        z_text = plot_z(policy2, z_text, policy_value)
    elif policy_selection == 3:
        policy_value = markov_Robot.bellman_eq_policy(policy3, gamma)
        z_text = plot_z(policy3, z_text, policy_value)
    elif policy_selection == 4:
        policy, value_function = markov_Robot.value_iteration(gamma, 10000, 0.0001)
        z_text = plot_z(policy, z_text, value_function)

    z = [[0, 0, 0, 0],
         [0, 10, 0, 5],
         [0, 0, 0, 5]]

    x = ['1', '2', '3', '4']
    y = ['1', '2', '3']

    figure = ff.create_annotated_heatmap(z, x=x, y=y, annotation_text=z_text, colorscale='Greys')
    figure.update_layout(template='plotly_dark', showlegend=False, font=dict(size = 16))
    figure.add_trace(go.Scatter(x=[1.5, 1.5],
               y=[0.5,3.5],
               mode='lines',
               line_color='black', line_width=2.5))
    figure.add_trace(go.Scatter(x=[2.5, 2.5],
                y=[0.5, 3.5],
                mode='lines',
                line_color='black', line_width=2.5))
    figure.add_trace(go.Scatter(x=[3.5, 3.5],
                y=[0.5, 3.5],
                mode='lines',
                line_color='black', line_width=2.5))
    figure.add_trace(go.Scatter(x=[0.5, 4.5],
                                y=[1.5, 1.5],
                                mode='lines',
                                line_color='black', line_width=2.5))
    figure.add_trace(go.Scatter(x=[0.5, 4.5],
                                y=[2.5, 2.5],
                                mode='lines',
                                line_color='black', line_width=2.5))

    return figure, ['Cost per step: ', costs], ['Gamma: ', gamma]