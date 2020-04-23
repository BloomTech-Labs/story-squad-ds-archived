"""
converting image to base64 then writing that string to a text file
to copy-paste into a .json file
"""

import base64
# insert name of file HERE
with open("photo_3101.jpg", "rb") as img_file:
    my_string = base64.b64encode(img_file.read())
    my_string = my_string.decode()

test_pic = open("photo_3101.txt", "w")
test_pic.write(my_string)
test_pic.close()

# only use the following lines of code if the story is 2 pages long

# # insert name of file for second picture BELOW
# with open("photo_3101.jpg", "rb") as img_file:
#     my_string = base64.b64encode(img_file.read())
#     my_string = my_string.decode()

# # change name of .txt file to match second picture's name
# test_pic = open("photo_3101.txt", "w")
# test_pic.write(my_string)
# test_pic.close()