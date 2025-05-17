# Mtcars-Flask-Api

## Getting Started
This repository includes a basic flask API which has been deployed with Google Cloud Run at the following [link](https://mtcars-lennemann-26302743692.europe-west1.run.app). You can make a request to the API to predict miles per gallon (mpg) based on the numerical features in the dataset. Information about this dataset and its features can be found [here](https://www.rdocumentation.org/packages/datasets/versions/3.6.2/topics/mtcars). 

If you navigate to the deployed model's URL or make a GET request, the API returns information about the model's coefficients. 

To use the deployed model for prediction on a single test datapoint, you can make a POST request to the API. One example curl command is:

`curl -H "Content-Type: application/json" -X POST -d '{"cyl":4,"disp":140.0,"hp":95,"drat":3.70,"wt":2.800,"qsec":19.00,"vs":1,"am":1,"gear":5,"carb":2}' https://mtcars-lennemann-26302743692.europe-west1.run.app/predict`

output: `{
  "prediction for given dataset": 25.509194647213448
}`

The payload, which should be in dictionary format, specifies the features that should be passed in so that the API can predict a mpg value for a single test datapoint. The API outputs a single value which predicts the miles per gallon for the test datapoint. 

To break it down further, my process involved:
- creating functions to fit a linear regression model on the `mtcars` dataset and predict using that model (`linmodel.py`)
- writing a Flask app (`server.py`)
- building a Docker image and pushing to DockerHub using `docker-compose.yml` and the Dockerfile
- deploying the API to Google Cloud Run

## How to Run Locally
This process can be replicated by cloning the repository. Then, install dependencies by running `pip install -r requirements.txt`. To set up the Docker environment, use the following command: `docker compose up -d`. 

Run the Flask app locally with the following command: `python server.py`.

