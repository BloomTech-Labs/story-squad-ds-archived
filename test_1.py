import os
os.system("ls -l")

import base64
with open("example_4.jpg", "rb") as img_file:
    my_string = base64.b64encode(img_file.read())
    my_string = my_string.decode()

text_file = open("sample.txt", "w")
n = text_file.write(my_string)
text_file.close()

import json

# y = json.dumps('["data:image/jpg;base64,{}"]/}'.format(my_string))
x = {"images":["data:image/jpg;base64,' + f'{my_string}' + 'exit"]}
z = json.dumps(x)

print(z)
print(type(z))

string_1 = "pipenv run python dotPy/transcription.py < integration/src/transcription_test.json"

os.system(string_1)