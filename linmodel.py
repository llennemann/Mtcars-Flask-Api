'''
The function build_linreg_model create a simple linear regression model with the dataset 
mtcars that predicts mpg (miles per gallon) based on various predictors. The function predict
takes in a dictionary of features and returns a prediction for mpg using the model. 
'''
import pandas as pd 
import numpy as np
from sklearn.linear_model import LinearRegression

# csv dataset input -> outputs linear regression model
def build_linreg_model(dataset):
    df = pd.read_csv(dataset)
    X = df.drop(['model', 'mpg'], axis=1) # 1 is columns
    print('Fitting model...')
    reg_mod = LinearRegression().fit(X, df['mpg'])
    return reg_mod

# dict of features for one datapoint (cyl, disp, hp, drat, wt, qsec, vs, am, gear, carb) 
# -> prediction
def predict(test_dict):
    mod = build_linreg_model('mtcars.csv')
    pred_data = pd.DataFrame(test_dict, index=[0])
    return mod.predict(pred_data)[0]