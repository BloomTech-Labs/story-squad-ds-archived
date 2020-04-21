from sys import stdin, stdout
from json import loads, dumps
from decouple import config
from datauri import DataURI
import pandas as pd

from google.cloud import vision
from google.cloud.vision import types
from google.oauth2 import service_account

import urllib.request

api_key = config("GOOGLE_APPLICATION_CREDENTIALS")
api_key = loads(api_key)
api_key = service_account.Credentials.from_service_account_info(api_key)
client = vision.ImageAnnotatorClient(credentials=api_key)


def transcribe(uri):
    # Parses a URI and gets the encoded data string out
    data = DataURI(uri).data
    image = types.Image(content=data)
    response = client.document_text_detection(image)

    if response.text_annotations:
        return response.text_annotations[0].description.replace('\n', ' ')
    else:
        return "No Text"


# To be replaced with a function that gets the metadata out of the function
def nothing(transcript):
    return {"nada": "nothing"}


# Input list of URIs
def process_images(uris):
    # Map functions are used to take iterable data structures like list, maps, etc. and make a map
    # that consist of the data of the original data structure after being run through a function.
    # Outputs a map (list like data structure) of all the uris after being transcribed
    transcripts = map(transcribe, uris)
    # Outputs a map (list like data structure) of all the transcriptions after having the meta data parsed
    metadata = map(nothing, transcripts)
    return {'images': list(transcripts), 'metadata': list(metadata)}


df = pd.read_csv('Bad_words.csv')
bad_words_list = df['Bad_words'].to_list()


def flag_bad_words(transcriptions):
    # turn transcriptions into a string and assigns it to a different variable
    parsed_string = dumps(transcriptions) # + 'add profanity here to test'
    # determine if any words in the story are in the bad words list
    res = any(word in parsed_string for word in bad_words_list)
    # return dictionary with True or False for backend to send to admin
    if res == True:
        dict = {'bad_words': [True]}
        return transcriptions.update(dict)
    else:
        dict = {'bad_words': [False]}
        return transcriptions.update(dict)
    

# Input: JSON String in the transcribable data structure
# Output: JSON String of the data being processed into transcripts and metadata
def main(transcribable):
    json = loads(transcribable)
    transcriptions = process_images(json['images'])
    flag_bad_words(transcriptions)
    return dumps(transcriptions)
 

# Reads in from stdin the entire input as a string
data = stdin.read()

# Runs the main function using the input string and saving the output string
output = main(data)

# Prints the output string to stdout
stdout.write(output)


# Can be tested with this command
# pipenv run python3 dotPy/transcription.py < integration/src/transcription_test.json

# Notice how the `test.json` is piped into stdin with the `<`
