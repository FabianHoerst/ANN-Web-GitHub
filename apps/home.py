'''
Code for the /home webapp
'''

import plotly.graph_objects as go
import pandas as pd

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from app import app
import dash_gif_component as Gif
card_content = [
    dbc.CardHeader("In Progress"),
    dbc.CardBody(
        [
            html.H5("In Progress", className="card-title"),
            html.P(
                "This page is not ready yet",
                className="card-text",
            ),
        ]
    ),
]

cards = html.Div(
    [dbc.Row(
            [
                dcc.Markdown('''
                ## Website for Visualizing some basic Artifical Intelligence and Machine Learning Algorithms
                
                
                
                #### Acknowledgement: This site is not ready yet. The current state corresponds to a basic concept, which will be gradually expanded.
                ''')
            ]
        ),
    ]
)

layout = dbc.Container(className='center', children=[
    cards
    ])