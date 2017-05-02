import json
import textblob
from sklearn.feature_extraction import DictVectorizer
from extract_features import *

def read_json(num, filename_to_read = "yelp_academic_dataset_review.json"):
    """ This function takes in two arguments:
            1) num, the number of json object from the dataset that we want
            2) filename_to_read, this is a default argument, the name of the dataset file

        The json objects we read are review object from the Yelp Dataset. We
        want to extract the review text and star rating for each review.

        This function returns a list of tuples, with the form (review, stars)
    """
    f = open(filename_to_read, "r")

    result = []
    for i in range(num):
        string_data = f.readline()
        data = json.loads( string_data )

        review = data["text"]
        stars = data["stars"]

        result.append( (review, stars) )

    return result



def process_review(review):
    """ This function takes in one argument:
            1) review, the text of review we get by reading the json file

        In this function, we want to extract all the features we want from
        the input review.

        This function returns a dictionary contraining all the features
        extracted from the review.
    """
    blob = textblob.TextBlob(review)
    features = extract_features_posneg(blob, {})
    features = extract_features_sentiment(blob, features)

    return features




def get_processed_data(LoR):
    """ This function takes in one argument:
            1) LoR, a list of tuples with each tuple in the form of (review, stars)

        We want to processed each review, extract features, and stores all
        information in numpy array for furthur processing.

        This function returns data splitted in train and test set.
        X are all features extracted from each review, and Y are the true labels
        with the corresponding review.
    """
    features_L = []
    Y = []

    # extract features from all reviews
    for review, stars in LoR:

        features = process_review(review)
        features_L.append(features)
        Y.append(stars)

    # vectorize features to numpy array
    v = DictVectorizer(sparse=False)
    X = v.fit_transform(features_L)

    # split the data
    size_train = int(3 * len(LoR) / 4)

    # get X and Y data
    X_train = X[:size_train]
    X_test = X[size_train:]

    Y_train = Y[:size_train]
    Y_test = Y[size_train:]

    return X_train, X_test, Y_train, Y_test


def process_label(Y):
    """ This function takes in one argument:
            1) Y, the label of the data

        This function modifies the labels from five catagories to three catagories.
        The original labels are star ratings from 1 to 5. Now we classify the
        labes into three catagories:
            1) non-favorable(-1), if 1 or 2 star
            2) neutral, if 3 star
            3) favorable, if 4 or 5 star

        This function then returns the modified label of the data.
    """
    # create a new list to hold the label
    new_Y = []

    # loop through all labels
    for label in Y:
        # if 1 or 2, non-favorable
        if label == 1 or label == 2:
            new_Y.append(-1)
        # if 3, neutral
        elif label == 3:
            new_Y.append(0)
        # otherwise, it's favorable
        else:
            new_Y.append(1)

    return new_Y
