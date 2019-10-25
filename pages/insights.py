import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Insights

            The dataset I worked with came separated into 7 different CSV files that contained the following.
            
            Restaurants
            R1 = 1 chefmozaccepts.csv

            R2 = 2 chefmozcuisine.csv

            R3 = 3 chefmozhours4.csv

            R4 = 4 chefmozparking.csv

            R5 = 5 geoplaces2.csv

            User
            U6 = 6 usercuisine.csv

            U7 = 7 userpayment.csv

            U8 = 8 userprofile.csv

            User-Item-Rating
            U9 = 9 rating_final.csv

            👉 please take a look at some interesting interactions I found before I even started to model the data.

            """
        ),
    ],
    md=4,
)


column2 = dbc.Col(
    [
        html.Img(src=app.get_asset_url('restaurant_payments.png'), className='img-fluid'),
        html.Img(src=app.get_asset_url('user_payments.png'), className='img-fluid')
    ]
)

layout = dbc.Row([column1, column2])