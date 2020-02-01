from sys import argv, stdout
from json import loads, dumps
from decouple import config

from google.cloud import vision
from google.cloud.vision import types
from google.oauth2 import service_account

import urllib.request
import base64

api_key = config('GOOGLE_CREDS')
api_key = loads(api_key)
api_key = service_account.Credentials.from_service_account_info(api_key)


def processImages(body):
    raw_images = body['images']
    length = raw_images['length']
    images = []

    try:
        for key in range(length):
            images.append(base64.b64decode(raw_images[str(key)]))
    except:
        print("Encoding error")
    # build list of images (still assuming urls for now)
    # images = []
    # for key in body.keys():
    #     images.append(base64.b64decode(body[key]))

    def transcribe(encoded_image):
        """Detects document features in the file located in Google Cloud
        Storage."""
        client = vision.ImageAnnotatorClient(credentials=api_key)
        image = types.Image(content=encoded_image)
        try:
            response = client.document_text_detection(image)
        except:
            return "Error in Google API"
        if response.text_annotations:
            return response.text_annotations[0].description
        else:
            return "No Text"

    transcripts = []
    for item in images:
        transcripts.append(transcribe(item).replace('\n', ' '))
        # transcripts.append((f'testing\n{item}').replace('\n', ' '))

    # Build response dict
    dic = {}
    dic['length'] = length

    for key in range(length):
        dic[str(key)] = transcripts[key]

    metadata = {}
    metadata['length'] = length

    for key in range(length):
        metadata[str(key)] = {"nothing": "nada"}
    return {'images': dic, 'metadata': metadata}


incoming = loads(argv[1])
processed = processImages(incoming)
stringified = dumps(processed)
stdout.write(stringified)
