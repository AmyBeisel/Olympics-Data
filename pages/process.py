# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [   
        dcc.Markdown(
            """
            For this project I chose Olympics data because I live in Olympic City, or Colorado Springs, home of the Olympic and Paralymic
            Committee Headquaters.  I am also an athlete myself and this area really is the perfect place for training grounds.
            
            ## Process

            My data exploration was fairly straight forward.  As it was fairly clean.  I decided to drop all athletes that didn't medal in the olympics. I was orginally 
            going to try and predict which counties would have the most medals in 2020, but with where I am in ability, and talking to experts, this would have been
            fairly difficult.  So, I decided to predict which sport one would most likely medal in based on there own stats.  

            I went down a few rabbit holes with some feature engineeing, that in the end I ended up not even using.  After cleaning up the data, mainly reducing my Sport features cardinality to 40 from 65, and getting the features I needed, I 
            was ready to split my data. I used a 3 way split into train, val and test.  Here is an example of my target 'Sport' based on one feature 'Age'. 

            """
            ),
             html.Img(src='assets/sports_based_on_age.png', 
                 className='sport_age', 
                 style={'display': 'block', 'margin-left': 'auto','margin-right': 'auto','width' : '70%'}
            
            ), 
            
        dcc.Markdown(
            """
            ## Machine Learning

            I did a logisic model as my majority base classifier, since this is a multi classification problem. My training accuracy was only 17%.  This means that 
            without doing any machine learning on my model, it would only guess correctly 17% of the time.  For my machine learning models, I tired both Random Forest Classifer
            and an XGboost model.  I ended up using the Random Forest as my final pipeline as it produced slightly better results.  
            ```
            {
                final_pipeline = make_pipeline(
                    ce.OrdinalEncoder(), 
                    RandomForestClassifier(n_estimators=100, 
                                           max_features='auto', random_state=42, 
                                           n_jobs=-1)
                )
                # Fit on train, score on val
                final_pipeline.fit(X_train, y_train)
                print('Validation Accuracy', final_pipeline.score(X_val, y_val))
            }
            ```
            """
            ),
            
        dcc.Markdown(
            """
            Below are the permutation imporatances of the features. Or bagging, which is used for Random Forests.  The most imporant feature in my model was weight.  This makes sense
            as a weightlifter, for example will be way heavier than an athete such as cycling who will be more lean. It's interesting that sex is the least
            important feature.   

            """

            ),
             html.Img(src='assets/permutaion_importance.png', 
                 className='permutaion_importance', 
                 style={'display': 'block', 'margin-left': 'auto','margin-right': 'auto','width' : '40%'}

             ),
        dcc.Markdown(
            """
            Gradient Boosting, which is used for xgboost.  Below is the graph, athough it is slighly less interruptible than the 
            bagging of random forest above.



            """
        ),   

          html.Img(src='assets/xgboost.png', 
                 className='xgboost', 
                 style={'display': 'block', 'margin-left': 'auto','margin-right': 'auto','width' : '40%'}
          ),
    dcc.Markdown(
            """        
            ## Results

            For the Random Forest Classifer, my accuracy ending up being 42%!  Still not the best score, but it 
            did increase from my base by 25%.  So what this means, is my model can correcly identify which sport 
            you would most likely medal in 42% of the time in this data.  With 40 sports, or classes to choose from, I'd say this is pretty darn good. 

            Xgboost was only 36% accuracy, which is why I went with the Random Forest. 

            To gain furhter insights into how the different features impacted my predictions, I created
            Shapley values on two examples:
            * A Cyclist - 
            """
            ),
            html.Img(src='assets/shap_cyclist.png', 
                 className='cyclist', 
                 style={'display': 'block', 'margin-left': 'auto','margin-right': 'auto','width' : '70%'} 
            ),
    dcc.Markdown(
            """
            * An Ice Hockey Player
            
            """
    
            ),
            html.Img(src='assets/shap_IceHockey.png', 
                 className='IceHockey', 
                 style={'display': 'block', 'margin-left': 'auto','margin-right': 'auto','width' : '70%'}
            ), 
    dcc.Markdown(
            """
            Each example interacts differenly. For the first example: season, year and weight helped the probability for the cyclist.
            But for the Ice Hockey player, only height helped. And season, year, age and weight lowered it. 
            """    
    ),
    ],
)

layout = dbc.Row([column1])