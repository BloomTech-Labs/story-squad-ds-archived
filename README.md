# Story Squad - Data Science

You can find the project at [https://story-squad.netlify.com/](https://story-squad.netlify.com/).

## Contributors

|                                              [Samantha Finley](https://srfinley.github.io/)                                              |                                   [Bhavani Rajan](https://bhavani-rajan.github.io/)                                    |                                    [Clay Roberts](claywaddell.com)                                     |                                                    [Ahmad Guenoun](https://personal-portfolio.amguenoun.now.sh/)                                                     |     |
| :--------------------------------------------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :-: |
|                  [<img src="https://srfinley.github.io/img/headshot.jpg" width = "200" />](https://srfinley.github.io/)                  |      [<img src="https://bhavani-rajan.github.io/img/RB.jpeg" width = "200" />](https://bhavani-rajan.github.io/)       |        [<img src="http://www.claywaddell.com/img/slack.jpg" width = "200" />](claywaddell.com)         | [<img src="https://www.dalesjewelers.com/wp-content/uploads/2018/10/placeholder-silhouette-male.png" width = "200" />](https://personal-portfolio.amguenoun.now.sh/) |     |
|                           [<img src="https://github.com/favicon.ico" width="15">](https://github.com/srfinley)                           |               [<img src="https://github.com/favicon.ico" width="15">](https://github.com/Bhavani-Rajan)                |         [<img src="https://github.com/favicon.ico" width="15">](https://github.com/HakujouRyu)         |                                        [<img src="https://github.com/favicon.ico" width="15">](https://github.com/amguenoun)                                         |     |
| [<img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15">](https://www.linkedin.com/in/samantha-finley-1a7ab6143/) | [<img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15">](linkedin.com/in/bhavani-rajan-585645) | [<img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15">](linkedin.com/in/ccrw) |                             [<img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15">](https://www.linkedin.com/)                              |     |

🚫 5️⃣ Optional examples of using images with links for your tech stack, make sure to change these to fit your project

![MIT](https://img.shields.io/packagist/l/doctrine/orm.svg)
![Typescript](https://img.shields.io/npm/types/typescript.svg?style=flat)
[![Netlify Status](https://api.netlify.com/api/v1/badges/b5c4db1c-b10d-42c3-b157-3746edd9e81d/deploy-status)](https://story-squad.netlify.com/)
[![code style: prettier](https://img.shields.io/badge/code_style-prettier-ff69b4.svg?style=flat-square)](https://github.com/prettier/prettier)

🚫 more info on using badges [here](https://github.com/badges/shields)

## Project Overview

[Trello Board](https://trello.com/b/95gq0QEF/labs-20-story-squad)

[Product Canvas](https://www.notion.so/Story-Squad-a5bff36c779a44bd91fa97e9af27a944)

Story Squad is a creative competition platform that encourages children to sharpen their language, drawing, teamwork, and critical thinking skills through an engaging, weekly battle.

[Deployed Front End](https://story-squad.netlify.com/)

### Tech Stack

Crossed-out listings indicate deprecated packages.

- Python
  - ~~Flask~~
  - Pandas
  - Textstat
  - scikit-learn
- Google Cloud Vision services

### 2️⃣ Predictions

🚫 Describe your models here

### 2️⃣ Explanatory Variables

- Explanatory Variable 1
- Explanatory Variable 2
- Explanatory Variable 3
- Explanatory Variable 4
- Explanatory Variable 5

### Data Sources

Due to COPPA compliance, all data scources are private.

### Python Notebooks

See the "Notebooks" directory.

### How to connect to the API

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

## Contributing

When contributing to this repository, please first discuss the change you wish to make via issue, email, or any other method with the owners of this repository before making a change.

Please note we have a [code of conduct](./code_of_conduct.md.md). Please follow it in all your interactions with the project.

### Issue/Bug Request

**If you are having an issue with the existing project code, please submit a bug report under the following guidelines:**

- Check first to see if your issue has already been reported.
- Check to see if the issue has recently been fixed by attempting to reproduce the issue using the latest master branch in the repository.
- Create a live example of the problem.
- Submit a detailed bug report including your environment & browser, steps to reproduce the issue, actual and expected outcomes, where you believe the issue is originating from, and any potential solutions you have considered.

### Feature Requests

We would love to hear from you about new features which would improve this app and further the aims of our project. Please provide as much detail and information as possible to show us why you think your new feature should be implemented.

### Pull Requests

If you have developed a patch, bug fix, or new feature that would improve this app, please submit a pull request. It is best to communicate your ideas with the developers first before investing a great deal of time into a pull request to ensure that it will mesh smoothly with the project.

Remember that this project is licensed under the MIT license, and by submitting a pull request, you agree that your work will be, too.

#### Pull Request Guidelines

- Ensure any install or build dependencies are removed before the end of the layer when doing a build.
- Update the README.md with details of changes to the interface, including new plist variables, exposed ports, useful file locations and container parameters.
- Ensure that your code conforms to our existing code conventions and test coverage.
- Include the relevant issue number, if applicable.
- You may merge the Pull Request in once you have the sign-off of two other developers, or if you do not have permission to do that, you may request the second reviewer to merge it for you.

### Attribution

These contribution guidelines have been adapted from [this good-Contributing.md-template](https://gist.github.com/PurpleBooth/b24679402957c63ec426).

## Documentation

See [Backend Documentation](https://github.com/Lambda-School-Labs/story-squad-be/blob/master/README.md) for details on the backend of our project.

See [Front End Documentation](https://github.com/Lambda-School-Labs/story-squad-fe/blob/master/README.md) for details on the front end of our project.
