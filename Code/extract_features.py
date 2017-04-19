import textblob
from nltk.corpus import opinion_lexicon

def extract_features_posneg(review_blob, features):
    """ This function takes in two arguments:
            1) review_blob, a textblob object creating from the string of review text
            2) features, a dictionary holding the features of input review

        In this function, we want to extract three features from the input review:
            1) total number of positive words
            2) total number of negative words
            3) whether positive words outcount negative words. If True, the value
               is 1. If same, the value if 0. Otherwise, the value is -1.

        Note: we use the opinion lexicon from the nltk library

        This function returns the features (dictionary) with these three features
        added to it.
    """

    all_words = list(review_blob.words)

    pos_words = list(opinion_lexicon.words('positive-words.txt'))
    neg_words = list(opinion_lexicon.words('negative-words.txt'))

    pos_set = set(pos_words)
    neg_set = set(neg_words)

    pos_count = 0
    neg_count = 0

    for word in all_words:

        if word in pos_set:
            pos_count += 1

        if word in neg_set:
            neg_count += 1

    features["positive"] = pos_count
    features["negative"] = neg_count

    value = None
    if pos_count > neg_count:
        value = 1
    elif pos_count == neg_count:
        value = 0
    else:
        value = -1

    features["more_pos"] = value

    return features



def extract_features_sentiment(review_blob, features):
    """ This function takes in two arguments:
            1) review_blob, a textblob object creating from the string of review text
            2) features, a dictionary holding the features of input review

        In this function, we want to extract two features from the input review:
            1) average subjectivity score per sentence
            2) average polarity score per sentence

        Note: the sentiment score is computed using textblob functionality

        This function returns the features (dictionary) with these two features
        added to it.
    """
    all_sentences = review_blob.sentences

    total_subjectivity = 0
    total_polarity = 0

    for sentence in all_sentences:
        total_subjectivity += sentence.sentiment.subjectivity
        total_polarity += sentence.sentiment.polarity

    average_subjectivity = float( total_subjectivity / len(all_sentences) )
    average_polarity = float( total_polarity / len(all_sentences) )

    features["subjectivity"] = average_subjectivity
    features["polarity"] = average_polarity

    return features
