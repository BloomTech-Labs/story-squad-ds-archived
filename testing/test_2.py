import base64
import os

path = "C:/Users/micha/Desktop/Lambda/DS-Unit-5_Labs/story-squad-ds/testing/stories"
path_2 = "C:/Users/micha/Desktop/Lambda/DS-Unit-5_Labs/story-squad-ds/testing/json_files"

# iterate through the names of contents of the folder
for image_path in os.listdir(path): 

    # create the full input path and read the file
    input_path = os.path.join(path, image_path)

    with open(input_path, "rb") as img_file:
        my_string = base64.b64encode(img_file.read())
        my_string = my_string.decode()
        json = f"{{\"images\": [\"data:image/jpg;base64,{my_string}\"]}}"

        file_name = os.path.splitext(image_path)
        file_name = os.path.join(path_2, file_name[0]+".json")
        json_file = open(f"{file_name}", "w")
        json_file.write(json)
        json_file.close()

"""
Don't think the following directions are necessary after refactoring
Keeping temporarily as of 5-12-20
"""

# only use the following lines of code if the story is 2 pages long

# # insert name of file for second picture BELOW
# with open("photo_3101.jpg", "rb") as img_file:
#     my_string = base64.b64encode(img_file.read())
#     my_string = my_string.decode()

# # change name of .txt file to match second picture's name
# test_pic = open("photo_3101.txt", "w")
# test_pic.write(my_string)
# test_pic.close()