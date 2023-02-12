import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
external_stylesheets=[dbc.themes.LUX]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

def description_card():
    """
    :return: A Div containing dashboard title & descriptions.
    """
    return html.Div(
        id="description-card",
        children=[
            html.H5("Clinical Analytics"),
            html.H3("Welcome to the Clinical Analytics Dashboard"),
            html.Div(
                id="intro",
                children="Explore clinic patient volume by time of day, waiting tim.",
            ),
        ],
    )

def description_card2():
    """
    :return: A Div containing dashboard title & descriptions.
    """
    return html.Div(
        id="description-card2",
        children=[
            html.Div(
                id="intro2",
                children="Explore clinic patient volume by timnts.",
            ),
        ],
    )


main_content = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H2("Solar Aircraft Design with AeroSandbox and Dash"),
                        html.H5("Peter Sharpe"),
                    ],
                    width=True,
                ),
                # dbc.Col([
                #     html.Img(src="assets/MIT-logo-red-gray-72x38.svg", alt="MIT Logo", height="30px"),
                # ], width=1)
            ],
            align="end",
        ),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Div(
                            [
                                html.H5("Filters"),
                                html.P("Number of booms:"),
                                dcc.Slider(
                                    id="n_booms",
                                    min=1,
                                    max=3,
                                    step=1,
                                    value=3,
                                    marks={1: "1", 2: "2", 3: "3",},
                                ),
                                html.P("Wing Span [m]:"),
                                dcc.Input(id="wing_span", value=43, type="number"),
                                html.P("Angle of Attack [deg]:"),
                                dcc.Input(id="alpha", value=7.0, type="number"),
                            ]
                        ),
                        html.Hr(),
                        html.Div(
                            [
                                html.H5("Aerodynamic Performance"),
                                dbc.Spinner(html.P(id="output"), color="primary",),
                            ]
                        ),
                    ],
                    width=3,
                ),
                dbc.Col(
                    [
                        #html.Div(id='display'),
                        dbc.Spinner(
                            dcc.Graph(id="display", style={"height": "80vh"}),
                            color="primary",
                        )
                    ],
                    width=True,
                ),
            ]
        ),
    ],
    fluid=True,
)

app.layout = main_content

if __name__ == '__main__':

    app.run_server(debug=True,)