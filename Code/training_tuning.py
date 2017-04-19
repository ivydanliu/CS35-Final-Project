import numpy as np
from sklearn import cross_validation
from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
from data_processing import *


def ten_fold_CV(classifier, x_train, y_train):
    """ This function takes three arguments:
            1) classifier, an just initialized classifier we want to train
            2) x_train, numpy array containing training data
            3) y_train, numpy array containing label for training data

        In this function, we want to do a ten_fold cross validation with
        the input classifier and training data.

        This function returns the average_train score, and average_test score
        after ten_fold.
    """

    # variables to keep track
    total_train_score = 0
    total_test_score = 0

    # cross validated 10 times
    for i in range(10):

        # split the training data to cross_validation data
        # the test_size is 0.1 since this is a 10-fold cross_validation
        cv_data_train, cv_data_test, cv_target_train, cv_target_test = \
            cross_validation.train_test_split(x_train, y_train, test_size=0.1) # random_state=0

        # fit the value and get the scores
        classifier.fit(cv_data_train, cv_target_train)
        train_score = classifier.score(cv_data_train,cv_target_train)
        test_score = classifier.score(cv_data_test,cv_target_test)

        # add both scores to total
        total_train_score += train_score
        total_test_score += test_score

    # calculate the average score
    average_train = total_train_score / float(10)
    average_test = total_test_score / float(10)

    return average_train, average_test





def dtree_tuning(x_train, y_train, num=20):
    """ This function takes in three arguments:
            1) x_train, numpy array containing training data
            2) y_train, numpy array containing label for training data
            3) num, a default input integer representing the number of depth
                    we will test. The default number is 20.

        In this function, we want to do ten-fold cross-validation using a
        dtree classifier with different depth. And choose the depth that produces
        best test accuracy.

        This function does not return anything, but reports the training_score,
        testing_score for each dtree classifier with different depth.
    """
    # keep track of final results
    final = []
    print("Currently cross-validating a Decision Tree Classfier...")
    print("The results are in shown in format: (training_score, testing_score, max-depth)")

    for i in range(num):
        # get max_depth and build the classifier
        max_depth = i+1
        dtree = tree.DecisionTreeClassifier(max_depth=max_depth)

        # cross-validation
        average_train,average_test = ten_fold_CV(dtree, x_train, y_train)

        # get result and report the result
        result = (average_train,average_test,max_depth)
        print(result)

        final.append(result)

    # sort result with testing score, report the best-performing max_depth
    L = sorted(final, key=lambda x: x[1], reverse = True)
    max_tree = L[0]

    print("The max_depth perform the best is", max_tree[2], "with testing score:", max_tree[1], "\n")
    return max_tree[2]




def knn_tuning(x_train, y_train, num=20):
    """ This function takes in three arguments:
            1) x_train, numpy array containing training data
            2) y_train, numpy array containing label for training data
            3) num, a default input integer representing the number of different
                    knn clasifiers we will test. The default number is 20.

        In this function, we want to do ten-fold cross-validation using a
        knn classifier with different number of neighbors. And choose the
        number of neighbors that produces best test accuracy.

        This function does not return anything, but reports the training_score,
        testing_score for each knn classifier.
    """
    # keep track of final results
    final = []
    print("Currently cross-validating a KNN Classfier...")
    print("The result in shown in format: (training_score, testing_score, k-value)")

    for i in range(num):
        # get k-value and build the classifier
        k = 2*(i+1)-1
        knn = KNeighborsClassifier(n_neighbors=k)

        # run cross_validation
        train, test = ten_fold_CV(knn, x_train, y_train)

        # get result and report the result
        result = (train,test,k)
        print(result)

        final.append(result)

    # sort result with testing score, report the best-performing k-value
    L = sorted(final, key=lambda x: x[1], reverse = True)
    max_knn = L[0]

    print("The k-value perform the best is", max_knn[2], "with testing score:", max_knn[1], "\n")
    return max_knn[2]
