import json
import base64
d = {"alg": "ES256"} 
s = json.dumps(d)  # Turns your json dict into a str
print(s)
print(type(s))

base64.b64encode(s)

x = base64.b64encode(s.encode('utf-8'))
print(x)