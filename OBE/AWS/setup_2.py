import boto3

def moderate_image(photo):

    client=boto3.client('rekognition')

    # response = client.detect_moderation_labels(Image={'S3Object':{'Bucket':bucket,'Name':photo}})
    with open(photo, 'rb') as image:
        # my_string = str(image.read())
        # test_pic = open("pen_29.txt", "w")
        # test_pic.write(my_string)
        # test_pic.close()
        response = client.detect_moderation_labels(Image={'Bytes': image.read()})


    print('Detected labels for ' + photo)    
    for label in response['ModerationLabels']:
        print (label['Name'] + ' : ' + str(label['Confidence']))
        print (label['ParentName'])
    return len(response['ModerationLabels'])



def main():
    photo='pen_29.jpg'
    bucket='bucket'
    label_count=moderate_image(photo)
    print("Labels detected: " + str(label_count))


if __name__ == "__main__":
    main()