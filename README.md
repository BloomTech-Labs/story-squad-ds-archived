## README 

- The primary files are in `dotPY` - `matchmaking`, `readability`, and `transcription`
- These files are integrated into the back-end [here](https://github.com/Lambda-School-Labs/story-squad-be/tree/master/src/util/scripts)
- Each files contains docstrings attempting to explain what it does, but the best way (obviously) is to read and understand the code itself
- The `OBE` file above contains decremented files from previous StorySquad DS cohorts




 |                                              [Samantha Finley](https:srfinley.github.io)                                              |                                              [Bhavani Rajan](https://bhavani-rajan.github.io/)                                              |                                             [Clay Roberts](claywaddell.com)                                              |                                                           [Ahmad Guenoun](https://personal-portfolio.amguenoun.now.sh/)                                                           |                                                           [Marilyn Landim Esko](https://marilynle.github.io/)                                                           |
| :-------------------------------------------------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| [<img src="https://srfinley.github.io/img/headshot.jpg" width = "200" />](https://srfinley.github.io/) |        [<img src="https://bhavani-rajan.github.io/img/RB.jpeg" width = "200" />](https://bhavani-rajan.github.io/)         | [<img src="http://www.claywaddell.com/img/slack.jpg" width = "200" />](claywaddell.com) | [<img src="https://www.dalesjewelers.com/wp-content/uploads/2018/10/placeholder-silhouette-male.png" width = "200" />](https://marilynle.github.io/) | [<img src="https://marilynle.github.io/img/IMG1.jpg" width = "200" />](https://github.com/allie-rae) |
|                     [<img src="https://github.com/favicon.ico" width="15">](https://github.com/srfinley)                      |                         [<img src="https://github.com/favicon.ico" width="15">](https://github.com/Bhavani-Rajan)                         |                                       [<img src="https://github.com/favicon.ico" width="15">](https://github.com/HakujouRyu)                                        |                                       [<img src="https://github.com/favicon.ico" width="15">](https://github.com/amguenoun)                                        |                                       [<img src="https://github.com/favicon.ico" width="15">](https://github.com/marilynle)                                        |
|       [<img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15">](https://www.linkedin.com/in/samantha-finley-1a7ab6143/)       | [<img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15">](linkedin.com/in/bhavani-rajan-585645) |                    [<img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15">](linkedin.com/in/ccrw)                    |                     [<img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15">](https://www.linkedin.com/)                      |                    [<img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15">](https://www.linkedin.com/in/marilyn-landim-esko-612ab6197/)                     |

## Project Overview

Story Squad is a creative competition platform that encourages children to sharpen their language, drawing, teamwork, and critical thinking skills through an engaging, weekly battle.

[Deployed Front End](https://story-squad.netlify.com/)

### Tech Stack

- Python
  - Pandas
  - Textstat
  - scikit-learn
- Google Cloud Vision services

### Data Sources

Due to COPPA compliance, all data sources are private. Contact the project stakeholder for access.

### Python Notebooks

See the "Notebooks" directory.

#### To receive a transcription of an image

Pipe in JSON data to transcription.py via stdin. In the input, include any number of base64-encoded images, with the initial metadata (e.g., `data:image/png;base64,`) stripped out. Format the JSON as follows:

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

When necessary, the app will also generate a small number of one-on-one and two-on-one matches.

## Documentation

See [Backend Documentation](https://github.com/Lambda-School-Labs/story-squad-be/blob/master/README.md) for details on the backend of our project.

See [Front End Documentation](https://github.com/Lambda-School-Labs/story-squad-fe/blob/master/README.md) for details on the front end of our project.

