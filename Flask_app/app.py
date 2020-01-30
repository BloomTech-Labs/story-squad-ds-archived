from decouple import config
from flask import Flask, jsonify, request
from google.cloud import vision
from google.cloud.vision import types
import urllib.request, json
from google.oauth2 import service_account
import base64

def create_app():
    app = Flask(__name__)
    # api_key = config('GOOGLE_CREDS')
    api_key = '{"type": "service_account", "project_id": "story-squad", "private_key_id": "b9d53c5fd5d4f3da800bdcc713d9b88a3ad06258", "private_key": "-----BEGIN PRIVATE KEY-----\\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC1LOK4GfnTcNhd\\nSyYjqf1UmJzO5ThUVBdWwAbsf+L9u6Xij7xoIKPdlZHRS54i1k6ZgD3Gimptg5Md\\n0OAHGtdHjH95QqFhdTa/mJQtW09/Ya8S15SRMaTLp9AN8tpWXxE4PgPuzx9a4MiK\\ntTzFjVrQ9/dVxY7Pc0SCEggcd1SxnGTMGP3b4l1wfFyK4/kx1SIVwyANpABxx5QN\\nf221KGEcoZAGSLlMGB0Vt70pFZswO3F53WHm/BVwUgDT0ES2dseXpr/P+xmAHHt0\\nXKg7Igh31KIAl51o/0U8SppDDhoTMjMfha8yM0Np6EnknPM5Y2nDtg0BRyWJWfGq\\nVh5Yc2vxAgMBAAECggEAKXm0EUdJDOGJdpoMih+RMfuZ8jdBVPTHPwHI0/1W3pVF\\nnX8gN4o5WTGzZwFzmzAKYFOeUMRBJv72/91gW+AGJogAaqcZQLFPrj7ktRlxMo0P\\nQjX9+dsuibzKAVd2Kk2rKH/x8IqT9/77id2BowwAHVSW15jZX55YsZolJzceOWZc\\nhWThpBb1eDgidS33v0BupGyd2psAaeFW5yFjeBM7hknf5qxJ430Ry4igl1LWcKRk\\nEGU5KDp88/Qdr7V2bqtzXjrcxKwdYGeuGGKo12h+N2NdBGeSYi255BD6kN96r+7Q\\npJAPSmww2B6UHgkADnU6tAlqFscpVAhXwnKrHaKuUQKBgQDY+wDjpP8o3DgO+i+O\\nz5ImDILkPdbi0DDQ5GfA8Y2j8MLPRELzFMBKD2+bTwR85YhLDZ3It2k8saprrS2n\\nuMjvMZffGZaFY4NUOFe7D7vmfZHcfT74PQkc/rVPQKrilDLImyxLRUXv7ADxfFJz\\nSIxBBAfHrgrOC8dOmDzSyqeC/QKBgQDVwYrrodjJidBUXj3PZQF7AZom+UR0sKA4\\nFkRI+GLdFnup1SWwpuufEt4Dg6JZA+yfx8VUq04p+bE6wLa+15iMuoRtM8I0LFi/\\nfR6nae4ZYTXqfjv7iHoFVSq0g5Kb46UxXZ7kN0NwmK+PwAc8H6PdQaHqND6b/wUv\\nqI4m2HxhBQKBgDYFwIHtKa5FrhtkhQS8f3nDsa8cCm1sQkswIvjx6z7/CbHLIBQf\\nfYSy9Smo8cga6eUt3bQEnkoDPhgTBQP2SOjs4xAj8csCLMeCQ62KTFElwHQyJsRt\\nheBXNlMmGaXSGhbCM7QF6lTC4LU/K9QSIwFo/HrlxUDpw9S4qKQe2rgNAoGBAISi\\n9erEoNpd05GmcMAyMrr7AYZRgjLOLnzfBDwrNF1vyAhYJGz7BpXMhUq08ZY+oyN6\\nOG4TZgsRzvFgB4VgDl60lduVFFp/cgpQPycuyfmhom0BK4Mm6mBIupkMU3q7xRNe\\nvmtqB0Tk2Xtfcp3SHEH8qdXD2V2+3p71/k8IYhVpAoGBALIrh4kEDQbFcPty/ppA\\nV9HydYYb8jjIYvmRm02Oa0GpJHWuRFeRNwSvUe1RZ7pW5MH2Drb5iJvrw/ywXTUw\\nuvZbVT3ixON4ozA3FS4EZ2kp55q/OO+QRZDO2Ufc2z4aSDf4/sxZ3yV+0BilsYjj\\nUNSuQFAMPLUO5s5Brk1O8dg3\\n-----END PRIVATE KEY-----\\n", "client_email": "admin-251@story-squad.iam.gserviceaccount.com", "client_id": "114377165489943689625", "auth_uri": "https://accounts.google.com/o/oauth2/auth", "token_uri": "https://oauth2.googleapis.com/token", "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs", "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/admin-251%40story-squad.iam.gserviceaccount.com"}'
    api_key = json.loads(api_key)
    api_key = service_account.Credentials.from_service_account_info(api_key)
    @app.route('/', methods=['POST']) # just read that this is where the methods list actually goes
    def root():
        # Get json objects
        body = request.get_json()
        # print(body)
        raw_images = body['images']
        length = raw_images['length']
        images = []
        try:
            for key in range(length):
                images.append(base64.b64decode(raw_images[str(key)]))
        except:
            print("Encoding error")
        #build list of images (still assuming urls for now)
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
        
        #Get transcrtipt (currently just returning diagnostis!)
        transcripts = []
        for item in images:
            transcripts.append(transcribe(item).replace('\n', ' '))
            # transcripts.append((f'testing\n{item}').replace('\n', ' '))

        #Build response dict
        dic = {}
        dic['length'] = length

        for key in range(length):
            dic[str(key)] = transcripts[key]
        
        metadata = {}
        metadata['length'] = length
        
        for key in range(length):
            metadata[str(key)] = {"nothing": "nada"}
        jason = {'images': dic, 'metadata': metadata}

        return jsonify(jason)


    return app