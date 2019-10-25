import dash
import dash_core_components as dcc
import dash_daq as daq
import dash_html_components as html
from dash.dependencies import Input, Output

import dash_bootstrap_components as dbc
from app import app

# from pdpbox.pdp import pdp_isolate, pdp_plot
# import pandas as pd
# from joblib import load
# from xgboost import XGBClassifier
# import category_encoders as ce
# from sklearn.pipeline import make_pipeline
# from sklearn.model_selection import GridSearchCV, StratifiedKFold



# url = 'https://raw.githubusercontent.com/JeanFraga/DS8-Build_Week-1/master/notebooks/Restaurant_Consumer_Data_merged'

# df = pd.read_csv(url)
# pipeline1 = load('assets/xgboost_model_y1.joblib.compressed')
# pipeline2 = load('assets/xgboost_model_y2.joblib.compressed')
# pipeline3 = load('assets/xgboost_model_y3.joblib.compressed')
# pipelines = {}
# pipelines['pipeline1'] = pipeline1
# pipelines['pipeline2'] = pipeline2
# pipelines['pipeline3'] = pipeline3
# target1 = 'rating'
# target2 = 'food_rating'
# target3 = 'service_rating'

# X = df.drop(columns=[target1, target2, target3])
# y1 = df[target1]
# y2 = df[target2]
# y3 = df[target3]

# feature = 'height'

# isolated = pdp_isolate(
#     model=pipeline1.best_estimator_, 
#     dataset=X, 
#     model_features=X.columns, 
#     feature=feature
# )
# pdp_plot_height=pdp_plot(isolated, feature_name=feature)

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Predictions

            The machine learning software I used allowed me to make a prediction with varying degrees of success depending on what type of rating I'm trying to predict.

            The following percentages correspond to the level of accuracy I was able to compute with the machine learning algorithm.

            1. Overal rating : 62%
            2. Food rating: 60%
            3. Service rating: 59%
            
            Taking a closer look at what information each User chose to give in their profile and what information the dataset managed to gather about the restaurant itself we can see some trends arise.

            👉 We can start by taking a look at the numerical feature "Height" and it's effect on the "Overal rating". As you might recall it was top 5 for the features that had the highest effect
            on what rating the user might give a restaurant they rated.



            """
        ),
        dcc.Link(dbc.Button('There is more!', color='dark'), href='/insights')
    ],
    md=4,
)

column2 = dbc.Col(
    [
        html.Img(src=app.get_asset_url('pdp_heights_y1.PNG'), className='img-fluid')
    ]
)

layout = dbc.Row([column1, column2])
