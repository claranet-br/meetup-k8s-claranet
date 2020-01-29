import flask
from flask import Flask


app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/api/v1/k8s', methods=['GET'])
def home():
     return "Meetup k8s - Claranet V2"

app.run(debug=True,host='0.0.0.0', port=80)
