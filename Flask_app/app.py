from decouple import config
from flask import Flask, jsonify, request
from google.cloud import vision
import urllib.request, json
from google.oauth2 import service_account


def create_app():
    app = Flask(__name__)
    data = config('GOOGLE_CREDS')
    data = json.loads(data)

    data = service_account.Credentials.from_service_account_info(data)
    print('outside')
    @app.route('/')
    def root(methods=['POST']):
        uri = request.args['image_location'].split(',')
        print('test')

        def transcribe(uri):
            """Detects document features in the file located in Google Cloud
            Storage."""
            client = vision.ImageAnnotatorClient(credentials=data)
            image = vision.types.Image()
            image.source.image_uri = uri
            response = client.document_text_detection(image=image)
            print(response)
            return response.text_annotations[0].description
        
        transcripts = []
        print(uri)
        for url in uri:
            print(url)
            transcripts.append(transcribe(url))
        full_text =  ' '.join(transcripts)
        full_text = full_text.replace('\n', ' ')
        response = {'Transcription': full_text}
        
        return jsonify(response)
        

    return app