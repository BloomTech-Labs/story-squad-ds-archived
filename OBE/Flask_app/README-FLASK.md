## How to connect to the API

### To receive a transcription of an image:

Connect to the app at [https://ss-ds.herokuapp.com/](https://ss-ds.herokuapp.com/) by a POST request. In the JSON body of the request, include any number of base64-encoded images, with the initial metadata (e.g., `data:image/png;base64,`) stripped out. Format the JSON as follows:

```
{
  "images": {
    "length": 2,
    "0": "iVBORw0KGgo...",
    "1": "/9j/4AAQSkZJR..."
  }
}
```
Make sure that the "length" value is an accurate integer greater than zero. All keys for image encodings must be consecutive string integers starting with 0 and continuing to `length-1`. It is recommended that the keys accurately reflect the ordering of the pages of the story.

The app returns a JSON object structured as follows:
```
{
  "images": {
    "length": 2,
    "0": "transcribed text of image 0",
    "1": "transcribed text of image 1"
  }
  "metadata": {
    "length": 2,
    "0": {placeholder metadata of image 0},
    "1": {placeholder metadata of image 1}
  }
}
```

The API does not yet collect or return any metadata on the images it processes.

If the Google Vision API fails to detect any text in a passed image, the transcript for that image will read "No Text".