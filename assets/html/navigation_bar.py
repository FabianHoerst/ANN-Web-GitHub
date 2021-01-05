'''
This File contains the navigation_bar of the website
'''

# building the navigation bar
import dash_bootstrap_components as dbc
import dash_html_components as html

FIRM_LOGO = "assets/logo.png"
# make a reuseable navitem for the different examples
nav_item = dbc.NavItem(dbc.NavLink("Link", href="#"))

dropdown_lin_reg = dbc.DropdownMenu(
    children=[
        dbc.DropdownMenuItem("Regression analytical solution", href="/linear_regression"),
        dbc.DropdownMenuItem("Gradient descent basics", href="/gradient_descent"),
        dbc.DropdownMenuItem("Batch, Stochastic and Mini-Batch Regression", href="/stoch_gradient_descent"),
        dbc.DropdownMenuItem("Regularization", href="/Regularization"),
    ],
    nav = True,
    in_navbar = True,
    label = "Linear Regression",
)

dropdown_projects = dbc.DropdownMenu(
    children=[
        dbc.DropdownMenuItem("Project 1: MDP", href="/MDP"),
    ],
    nav = True,
    in_navbar = True,
    label = "Projects",
)

dropdown_ann = dbc.DropdownMenu(
    children=[
        dbc.DropdownMenuItem("ANN-Basics", href=""),
    ],
    nav = True,
    in_navbar = True,
    label = "Artifical Neural Networks (ANN)",
)

# this example that adds a logo to the navbar brand
navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=FIRM_LOGO, height="60px")),
                    ],
                    align="center",
                    no_gutters=True,
                ),
                href="/home",
            ),
            dbc.NavbarToggler(id="navbar-toggler2"),
            dbc.Collapse(
                dbc.Nav(
                    [dropdown_lin_reg, dropdown_ann, dropdown_projects], className="ml-auto", navbar=True
                ),
                id="navbar-collapse2",
                navbar=True,
            ),
        ]
    ),
    color="dark",
    dark=True,
    className="mb-5",
)
