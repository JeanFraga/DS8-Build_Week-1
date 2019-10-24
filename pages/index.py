import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
# import pandas as pd
# from joblib import load
# from xgboost import XGBClassifier
# import category_encoders as ce
# from sklearn.pipeline import make_pipeline
# from sklearn.model_selection import GridSearchCV, StratifiedKFold

from app import app

# url = 'https://raw.githubusercontent.com/JeanFraga/DS8-Build_Week-1/master/notebooks/Restaurant_Consumer_Data_merged'

# df = pd.read_csv(url)
# pipeline1 = load('assets/xgboost_model_y1.joblib')
# pipeline2 = load('assets/xgboost_model_y2.joblib')
# pipeline3 = load('assets/xgboost_model_y3.joblib')
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

            My project revolves around the data gathered from 130 restaurants in Mexico and subsequently the rating those received from 138 users. 

            👉 With the graph on the right you can choose one of the 3 ratings and see what features mattered the most when predicting what rating the restaurant would receive by each user.

            ❗ I have chosen to only display the top 25 features used to predict each rating from a list of 113.

            👇 If you would like to see how changing some of these features individually affect the rating the restaurant is likely to receive please click below.

            """
        ),
        dcc.Link(dbc.Button('Find Out!', color='dark'), href='/predictions')
    ],
    md=4,
)


# importances = pd.Series(pipeline1.best_estimator_.named_steps['xgbclassifier'].feature_importances_, X.columns)
# n=25
# importances = importances.sort_values()[-n:]
# importances = importances.to_frame().reset_index()
# importances.columns=['column1','column2']

# fig = px.bar(importances,y='column1',x='column2',title=f'Top {n} features',  orientation='h',width=700, height=700)

gapminder = px.data.gapminder()
fig = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
           hover_name="country", log_x=True, size_max=80)

column2 = dbc.Col(
    [
        dcc.Dropdown(
            id='rating_options',
            options=[
                {'label': '1. Overal Rating', 'value': 'pipeline1'},
                {'label': '2. Food Rating', 'value': 'pipeline2'},
                {'label': '3. Service Rating', 'value': 'pipeline3'}
                ],
            value='pipeline1'
            ),
        dcc.Graph(figure=fig), # figure=fig,id='feature_importance_graph'
    ]
)

layout = dbc.Row([column1, column2])

# @app.callback(
#     Output(component_id='feature_importance_graph',component_property='figure'),
#     [Input(component_id='rating_options', component_property='value')]
#     )
# def feature_importance_per_rating(what_pipeline):

#     importances = pd.Series(pipelines[what_pipeline].best_estimator_.named_steps['xgbclassifier'].feature_importances_, X.columns)
#     n=25
#     importances = importances.sort_values()[-n:]
#     importances = importances.to_frame().reset_index()
#     importances.columns=['features','importance']
#     return px.bar(importances,y='features',x='importance',title=f'Top {n} features',  orientation='h',width=700, height=700)

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
# Plot feature importances
# %matplotlib inline
# import matplotlib.pyplot as plt
