import os

# Will need to change the path based on User's local environment
path = "C:/Users/micha/Desktop/Lambda/DS-Unit-5_Labs/story-squad-ds/testing/json_files/"

"""
After images of handwritten text have been converted to JSON objects, this loops over each file and pipes
it into the transcription.py file which sends it to the Google API . 

When testing, remember to uncomment the path and block of code in the main() function in transcription.py 
"""


for image_path in os.listdir(path): 

    # create the full input path and read the file
    input_path = os.path.join(path, image_path)
    print(input_path)
    os.system(f"pipenv run python dotPy/transcription.py < {input_path}")
    print("--------------------------------------------")S