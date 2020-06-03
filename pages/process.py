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
        
            ## Process

            The process of cleaning up the feautres and engineering new ones from columns I had to drop took the longest. I originally had 500 columns for
            a dataset that contained only 1161 rows. This would not work for generalizing and tended to overfit. When I got around to engineer features I was 
            able to go to 116 colums. This many columns allowed me to have a fair set ready to model.

            XGBoost allowed me to get the best accuracy for my mult class target. Beause I wanted to be thorough I ended up running a gridsearchcv that fit 2560 
            models over a period of three hours. After finding the settings that gave me the best results on my model I got a 25% improvement over my baseline across
            all of the ratings I wanted to be able to predict.

            I go more into more depth in my notebooks but here is a shapely graphs that shows how my model interacted with row "432".

            A link to my notebook is included below where the GitHub link resides. 

            Thank you for taking your time to read my through my second project. I'm looking forward to what comes next. 😊

            """
        ),
        html.Img(src=app.get_asset_url('shapely_graph_row_432.PNG'), className='img-fluid'),
    ],
)

layout = dbc.Row([column1])