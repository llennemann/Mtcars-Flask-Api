from flask import Flask, request, jsonify
from linmodel import build_linreg_model, predict

# PUT request needs a header, expecting content type to be json 
# response should be plain text
HEADERS = {'Content-type': 'application/json', 'Accept': 'text/plain'}

def flask_app():
    app = Flask(__name__)

    @app.route('/', methods=['GET'])
    def build_model():
        mod = build_linreg_model('mtcars.csv')
        return mod.coef_.tolist()

    @app.route('/predict', methods=['POST'])
    def predict_mpg():
        payload = request.json
        pred = predict(payload)
        # jsonify: easily return JSON-formatted data from routes
        return jsonify({
            "prediction for given dataset": pred
        })
    
    return app


if __name__ == '__main__':
    app = flask_app()
    app.run(debug=True, host='0.0.0.0',port=5001)