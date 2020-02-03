from sys import stdin, stdout
from json import load, loads, dumps
from decouple import config
from datauri import DataURI

from google.cloud import vision
from google.cloud.vision import types
from google.oauth2 import service_account

import urllib.request

api_key = config('GOOGLE_CREDS')
api_key = loads(api_key)
api_key = service_account.Credentials.from_service_account_info(api_key)
client = vision.ImageAnnotatorClient(credentials=api_key)


def transcribe(uri):
    data = DataURI(uri).data
    image = types.Image(content=data)
    response = client.document_text_detection(image)

    if response.text_annotations:
        return response.text_annotations[0].description.replace('\n', ' ')
    else:
        return "No Text"


def nothing(transcript):
    return {"nada": "nothing"}


def process_images(uris):
    transcripts = map(transcribe, uris)
    metadata = map(nothing, transcripts)
    return {'images': list(transcripts), 'metadata': list(metadata)}


def main(transcribable):
    loaded = load(transcribable)
    transcriptions = process_images(loaded['images'])
    return dumps(transcriptions)


output = main(stdin)
stdout.write(output)
