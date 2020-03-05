# Wrapup Notes from the Labs 20 Data Science Team

As Labs 20 ends, the three of us -- Clay, Samantha, and Bhavani -- thought it would be best to try and record our thoughts about the state of the project as we're leaving it and what the future will look like. 

## Transcription

The Google Cloud Vision service is a great fit for Story Squad's needs, with low costs and a high degree of accuracy. To cut costs even further, or because OCR is an exciting application of neural networks, we anticipate future DS teams may be tempted, as we once were, to create a homemade handwriting recognition model or adapt an open source one (pre-trained or untrained) for Story Squad's use.

Pitfalls:
- Pre-trained models we identified during our tenure were either trained on printed text or adult _cursive_ handwriting. In these cases, the layers dedicated to identifying text blocks and lines may still be effective, but the character-level accuracy when applied to the handwriting of today's young people (who do not seem to handwrite recreationally in cursive, nor in any computer typeface) is very low.
- We believe a truly enormous sample of stories -- each of which must be annotated by hand to be used as training data -- would be needed, either for an all-new model or retraining of an existing one. During Labs 20, we only had access to 167 stories collected by Graig, and while some of those were multiple pages, it was clearly inadequate for the purpose.

## Story Scoring

This is a huge growth area. Right now, our analysis of the text of the stories is very low-level, e.g., how long is it? And by necessity, we have very limited information about the user submitting the story -- in the sample data, only their grade in school. Graig has lots of ideas about what features signal sophisticated storytelling in child authors, and we were only able to implement one. Beyond that, it seems likely that NLP will offer some exciting possibilities in training a "story rating algorithm" of sorts.

Pitfalls:
- Beware using an NLP package's built-in vectorization for "similarity rating" functions. The similarities identified through these means are topical, which is not the intended axis of similarity for our purposes.
- In general, be mindful of when and how your tools assume clean data. The stories are uncommonly "dirty," as text data goes, since children make many errors when they write and more errors will be introduced by machine transcription. If a metric is very sensitive to missing punctuation or poor spelling, it's likely to be a bad fit for Story Squad.

## Matching

Our white whale during the final period of Labs 20 was the implementation of a clustering algorithm that did a seemingly simple thing: produced clusters of a specific size (four players per match) rather than a specific number of clusters. This is a kind of off-brand use of clustering, so it's not too surprising that we didn't find a pre-written Python implementation of it. 

Regardless of whether the algorithm itself is changed or not, the best way to improve a model's output is to improve its input. Generate better story scores (and incorporate illustration scores as well), maybe scale them by importance in a meaningful way, and watch well-paired teams fall out.

# Have fun and good luck!