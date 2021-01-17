'''
Code for the /home webapp
'''


import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc


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