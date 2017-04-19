from training_tuning import *

def predict_tree(X_train, Y_train, X_test, Y_test, depth):
    """ This function fit the DT model with all training data for test set (first
        10 data points) output the final prediction.

        Report the final prediction in order.
        Report the actual results
    """
    # Choose max_depth=13, build appropriate classifier
    dtree = tree.DecisionTreeClassifier(max_depth=depth)

    # fit the model
    dtree.fit(X_train, Y_train)
    print("\nCreated and trained a DT classifier")  #, knn

    pred = dtree.predict(X_test)

    # Report the features importances
    print("\nFeature Importance of DT:")
    print(dtree.feature_importances_)

    count = 0
    total_error = 0
    for i in range(len(pred)):
        guess = pred[i]
        true = Y_test[i]
        if guess == true:
            count += 1

        error_sq = (guess-true)**2
        total_error += error_sq

    MSE = float(total_error / len(Y_test))

    print("\nThe total number of review we are testing is:", len(Y_test))
    print("The total number of correct predict using current DT classifier is:", count)
    print("The mean square error is:", MSE)

    return dtree


def predict_knn(X_train, Y_train, X_test, Y_test, neighbors):
    """ This function fit the DT model with all training data for test set (first
        10 data points) output the final prediction.

        Report the final prediction in order.
        Report the actual results
    """
    # Choose max_depth=13, build appropriate classifier
    knn = KNeighborsClassifier(n_neighbors=neighbors)

    # fit the model
    knn.fit(X_train, Y_train)
    print("\nCreated and trained a KNN classifier")  #, knn

    pred = knn.predict(X_test)

    count = 0
    total_error = 0
    for i in range(len(pred)):
        guess = pred[i]
        true = Y_test[i]
        if guess == true:
            count += 1

        error_sq = (guess-true)**2
        total_error += error_sq

    MSE = float(total_error / len(Y_test))

    print("\nThe total number of review we are testing is:", len(Y_test))
    print("The total number of correct predict using current KNN classifier is:", count)
    print("The mean square error is:", MSE)

    return knn


def predict_review(review, knn, dtree):
    """ This function takes in three arguements:
            1) review, a string containing the text of a review
            2) knn, a KNN classifier trained using our training data
            3) dtree, a Decision tree Classifier trained using our training data

        In this function we want to predict star rating of the input review
        using both classifier inputed.

        This function does not return anything, but it report the predicted
        star rating using both classifier
    """
    features = process_review(review)

    v = DictVectorizer(sparse = False)
    test = v.fit_transform(features)

    pred_knn = knn.predict(test)
    pred_dtree = dtree.predict(test)

    print("\nGiven the review test:\n\n", review)
    print("\nThe star rating for this review predicted using our trained KNN Classifier is:", pred_knn[0])
    print("\nThe star rating for this review predicted using our trained Decision Tree Classifier is:", pred_dtree[0])
