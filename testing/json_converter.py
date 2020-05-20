import base64
import os

"""
Both path & path_2 will need to be changed based on users local environment. 

The deeply nested set of for loops below is sequentially finding each and only each .jpg file
of the student's written stories, converting the .jpg file to base64, and storing both the base64
and the name of the file as a .json object. That .json object is then being stored in path_2

"""

path = "C:/Users/micha/Desktop/Lambda/DS-Unit-5_Labs/Story_Squad_Dataset/Transcribed_Stories/"
path_2 = "C:/Users/micha/Desktop/Lambda/DS-Unit-5_Labs/story-squad-ds/testing/json_files"

path_list = []

for root, dirs, files in os.walk(path):
    for dir in dirs:
        input_path = os.path.join(path, dir)
        for root, dirs, files in os.walk(input_path):
            for dir_2 in dirs:
                input_path_2 = os.path.join(input_path, dir_2)
                for root, dirs, files in os.walk(input_path_2):
                    for name in files:
                        if name.endswith((".jpg")):
                            input_path_3 = os.path.join(input_path_2, name)
                            path_list.append(input_path_3)
                            
                            with open(input_path_3, "rb") as img_file:
                                my_string = base64.b64encode(img_file.read())
                                my_string = my_string.decode()

                                file_name = os.path.splitext(name)[0].replace(" ", "_")
                                json = f"{{\"images\": [\"data:image/jpg;base64,{my_string}\"], \"file_name\": \"{file_name}\"}}"

                                file_name = os.path.join(path_2, file_name+".json")
                                json_file = open(f"{file_name}", "w")
                                json_file.write(json)
                                json_file.close()