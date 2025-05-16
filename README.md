# Mtcars-Flask-Api
STATS 418 - Homework creating a flask API, creating an image and deploying with google cloud run

in this repo: dockerfile, requirements file with the needed python packages, docker compose file, server.py with the Flask app, linmodel.py with the functions to 
fit the linear regression model, mtcars which is the dataset

created a flask API which builds a linear regression model to predict mpg based on all the other numeric variables. can predict mpg based on test data. this API
is deployed with Google Cloud Run. 

to download the Docker image, use the following command: `docker compose up -d`

The API is deployed at the following link: https://mtcars-lennemann-26302743692.europe-west1.run.app where you can see the coefficients for the model. 

You can also make a POST request to the API with the following curl command, i.e.: 

curl -H "Content-Type: application/json" -X POST -d '{"cyl":4,"disp":140.0,"hp":95,"drat":3.70,"wt":2.800,"qsec":19.00,"vs":1,"am":1,"gear":5,"carb":2}' https://mtcars-lennemann-26302743692.europe-west1.run.app/predict 
