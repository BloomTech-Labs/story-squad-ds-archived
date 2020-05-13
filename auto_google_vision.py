import os

path = "C:/Users/micha/Desktop\Lambda\DS-Unit-5_Labs\story-squad-ds/testing\json_files"

for image_path in os.listdir(path): 

    # create the full input path and read the file
    input_path = os.path.join(path, image_path)
    print(input_path)
    os.system(f"pipenv run python dotPy/transcription.py < {input_path}")