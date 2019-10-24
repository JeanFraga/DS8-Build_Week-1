import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_daq as daq
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Predictions


            """
        ),
        dcc.Slider(
            id='slider1',
            min=0,
            max=100,
            step=0.5,
            value=0,
            marks={
                0:'0',
                20:'20',
                40:'40',
                60:'60',
                80:'80',
                100:'100'
            },
            className='mb-5'
            )  
        #dcc.Markdown("Here is some sample text"),
    ],
    md=6,
)

column2 = dbc.Col(
    [
        daq.Gauge(
            id='my-daq-gauge',
            max=10,
            value=6,
            min=0
        )     
    ]
)

layout = dbc.Row([column1, column2])

# @app.callback(
# [Output(component_id='out1',component_property='value')],
# [Output(component_id='slider1',component_property='value')]
# )