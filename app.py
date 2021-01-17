'''
Starting the Appserver and loading the Stylesheet
'''

# import dash modules
import dash
import dash_bootstrap_components as dbc

# css theme, please see documentation here: https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/
external_css = [dbc.themes.DARKLY]

# start server
app = dash.Dash(__name__, external_stylesheets=external_css)
app.title = 'ANN'
server = app.server
app.config.suppress_callback_exceptions = True