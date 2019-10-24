import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
from joblib import load
#import shap
from xgboost import XGBClassifier
import category_encoders as ce
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import GridSearchCV, StratifiedKFold

from app import app


# df = pd.read_csv('assets/restaurant_data_with_consumer_ratings_merged',index_col=0)
url = 'https://raw.githubusercontent.com/JeanFraga/DS8-Build_Week-1/master/notebooks/Restaurant_Consumer_Data_merged'

df = pd.read_csv(url)
pipeline = load('assets/xgboost_model_y1.joblib.compressed')
target1 = 'rating'
target2 = 'food_rating'
target3 = 'service_rating'

X = df.drop(columns=[target1, target2, target3])
y1 = df[target1]
y2 = df[target2]
y3 = df[target3]


"""
https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout

Layout in Bootstrap is controlled using the grid system. The Bootstrap grid has 
twelve columns.

There are three main layout components in dash-bootstrap-components: Container, 
Row, and Col.

The layout of your app should be built as a series of rows of columns.

We set md=4 indicating that on a 'medium' sized or larger screen each column 
should take up a third of the width. Since we don't specify behaviour on 
smaller size screens Bootstrap will allow the rows to wrap so as not to squash 
the content.
"""

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## What rating will your restaurant receive?

            This data allows us to predict the possible rating a user might give based on his profile and the information available about the restaurant. The ratings we can predict are:
            
            1. Overal rating
            2. Food rating
            3. Service rating

            👉 With the graph on the right you can choose a row from the total data and see what my model predicts he/she will vote.

            My project revolves around the data gathered from 130 restaurants in Mexico and subsequently the rating those received from 138 users. 
            
            This data has a lot of information we can use to make a prediction. Listed below are just a few I have picked out to show the ones that had the most impact on all three ratings.

            'ulatitude', 'height', 'upays_cash', 'upays_visa', 'ucuisine_cafeteria',
            'ucuisine_family', 'ucuisine_pizzeria', 'utotal_cuisine', 'franchise',
            'rcuisine_bar_pub_brewery', 'rcuisine_burgers', 'rtotal_cuisine'

            """
        ),
        dcc.Link(dbc.Button('Find Out!', color='dark'), href='/predictions')
    ],
    md=4,
)

# row= X.iloc[[200]]
# explainer = shap.TreeExplainer(pipeline.best_estimator_.named_steps['xgbclassifier'])
# row_processed = pipeline.best_estimator_.named_steps['ordinalencoder'].transform(row)
# shap_values = explainer.shap_values(row_processed)

# shap.initjs()
# fig = shap.force_plot(
#         base_value=explainer.expected_value[1], 
#         shap_values=shap_values[1], 
#         features=row
#         )

# Get feature importances
#pipeline.best_estimator_.named_steps['xgbclassifier']
importances = pd.Series(pipeline.best_estimator_.named_steps['xgbclassifier'].feature_importances_, X.columns)
n=50
importances = importances.sort_values()[-n:]
importances = importances.to_frame().reset_index()
importances.columns=['column1','column2']

# Plot feature importances
# %matplotlib inline
# import matplotlib.pyplot as plt



fig = px.bar(importances,y='column1',x='column2',title=f'Top {n} features',  orientation='h',width=700, height=700)

# gapminder = px.data.gapminder()
# fig = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
#            hover_name="country", log_x=True, size_max=80)

column2 = dbc.Col(
    [
        dcc.Graph(figure=fig),
    ]
)

layout = dbc.Row([column1, column2])
