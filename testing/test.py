"""
converting image to base64 then writing that string to a text file
to copy-paste into a text.json file
"""

import base64
with open("photo_3101.jpg", "rb") as img_file:
    my_string = base64.b64encode(img_file.read())
    my_string = my_string.decode()

test_pic = open("photo_3101.txt", "w")
test_pic.write(my_string)
test_pic.close()


"""
attempting to automate the above process
"""

# from json import loads, dumps

# json_1 = {'images': list(my_string)}
# json_1 = dumps(json_1)

# import os
# string_1 = "pipenv run python dotPy/transcription.py < test_3.json"
# os.system(string_1)