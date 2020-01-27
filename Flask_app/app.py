from decouple import config
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from google.cloud import vision


load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config['GOOGLE_APPLICATION_CREDENTIALS'] = config('GOOGLE_APPLICATION_CREDENTIALS')

    @app.route('/')
    def root(methods=['POST']):
        uri = request.args['image_location']

        def transcribe(uri):
            """Detects document features in the file located in Google Cloud
            Storage."""
            client = vision.ImageAnnotatorClient()
            image = vision.types.Image()
            image.source.image_uri = uri
            response = client.document_text_detection(image=image)

            return response.text_annotations[0].description
        
        response = {'Transcription':  transcribe(uri)}
        return jsonify(response)
        

    return app