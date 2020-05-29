## Project Overview

Story Squad is a creative competition platform that encourages children to sharpen their language, drawing, teamwork, and critical thinking skills through an engaging, weekly battle.

[Deployed Front End](https://story-squad.netlify.com/)

### Data Sources

Due to COPPA compliance, all data scources are private. Contact the project stakeholder for access.

#### To receive a transcription of an image

Pipe in JSON data to transcription.py via stdin (the terminal or bash). In the input, include any number of base64-encoded images, with the initial metadata (e.g., `data:image/png;base64,`) stripped out. Example of what this commands looks like: `pipenv run python matchmaking.py < matchmaking_test.json`

Format the JSON as follows:

```json
{
  "images": ["iVBORw0KGgo...", "/9j/4AAQSkZJR..."]
}
```

The app returns a JSON object structured as follows via stdout:

```json
{
  "images": [
    "transcribed text of image 0",
    "transcribed text of image 1"
  ],
  "metadata": [
    {placeholder metadata of image 0},
    {placeholder metadata of image 1},
  ]
}
```

The API does not yet collect or return any metadata on the images it processes.

If the Google Vision API fails to detect any text in a passed image, the transcript for that image will read "No Text".

#### To receive the readability scores of a text

Pipe in JSON data containing the text of the story to readability.py via stdin. Format the JSON as follows:

```json
{
    "story": "Once upon a time, ..."
}
```

The app returns a JSON object structured as follows via stdout:

```json
{
    "flesch_reading_ease": score,
    "smog_index": index,
    "flesch_kincaid_grade": grade,
    "coleman_liau_index": index,
    "automated_readability_index": index,
    "dale_chall_readability_score": score,
    "difficult_words": number of words,
    "linsear_write_formula": formula,
    "gunning_fog": index,
    "consolidated_score": score,
    "doc_length": length,
    "quote_count": count 
}
```

#### To receive the matches for a set of competitors

Pipe in JSON data containing each competitor's ID and the statistics for that week's story to matchmaking.py. There must be at least two competitors for any matches to be set up. Format the JSON as follows:

```json
{"ID_0": 
  {"quote_count": count, 
  "doc_length": length, 
  "flesch_reading_ease": score, 
  "smog_index": index, 
  "flesch_kincaid_grade_level": score, 
  "coleman_liau_index": index, 
  "automated_readability_index": index, 
  "dale_chall_readability score": score, 
  "difficult_words": count, 
  "linsear_write_formula": score, 
  "gunning_fog": score, 
  "consolidated_score": score, 
  "grade": grade}, 
"ID_1": 
  {"quote_count": count, 
  "doc_length": length, 
  "flesch_reading_ease": score, 
  "smog_index": index, 
  "flesch_kincaid_grade_level": score, 
  "coleman_liau_index": index, 
  "automated_readability_index": index, 
  "dale_chall_readability score": score, 
  "difficult_words": count, 
  "linsear_write_formula": score, 
  "gunning_fog": score, 
  "consolidated_score": score, 
  "grade": grade},
...
```

The app returns the matches in a JSON object structured as follows via stdout:

```json
{"match_0": 
  {"team_1": ["ID_0", "ID_1"], "team_2": ["ID_2", "ID_3"]}, 
"match_1": 
  {"team_1": ["ID_4", "ID_5"], "team_2": ["ID_6", "ID_7"]},
...
```

When necessary, the app will also generate a small number of one-on-one, two-on-one, and two-on-three matches.

## Documentation

See [Backend Documentation](https://github.com/Lambda-School-Labs/story-squad-be/blob/master/README.md) for details on the backend of our project.

See [Front End Documentation](https://github.com/Lambda-School-Labs/story-squad-fe/blob/master/README.md) for details on the front end of our project.

