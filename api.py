from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "itty bitty test"

# run locally with gunicorn api:app