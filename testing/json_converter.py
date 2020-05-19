import base64
import os

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

print(len(path_list))
            
    # for name in files:
    #     if name.endswith((".jpg")):
    #         print("NAME:", name)
    #         input_path = os.path.join(path, name)




            # print("INPUT:", input_path) 
            # with open(input_path, "rb") as img_file:
            #     my_string = base64.b64encode(img_file.read())
            #     my_string = my_string.decode()

                # file_name = os.path.splitext(name)[0].replace(" ", "_")
                # json = f"{{\"images\": [\"data:image/jpg;base64,{my_string}\"], \"file_name\": \"{file_name[0]}\"}}"

                # file_name = os.path.join(path_2, file_name+".json")
                # json_file = open(f"{file_name}", "w")
                # json_file.write(json)
                # json_file.close()


# iterate through the names of contents of the folder
# for image_path in os.listdir(path): 

#     # create the full input path and read the file
#     file_name = os.path.splitext(image_path)
#     if file_name[1] != ".jpg":
#         continue 
#     else:
#         input_path = os.path.join(path, image_path)
#         print(image_path)
#         print("INPUT:", input_path)



#         with open(input_path, "rb") as img_file:
#             my_string = base64.b64encode(img_file.read())
#             my_string = my_string.decode()
#             json = f"{{\"images\": [\"data:image/jpg;base64,{my_string}\"], \"file_name\": \"{file_name[0]}\"}}"

#             file_name = os.path.splitext(image_path)[0].replace(" ", "_")
#             file_name = os.path.join(path_2, file_name+".json")
#             json_file = open(f"{file_name}", "w")
#             json_file.write(json)
#             json_file.close()

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