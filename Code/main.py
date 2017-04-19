from predict import *

if __name__ == '__main__' :

    # read and process data
    print("Reading files...")
    data = read_json(5000)

    print("\nProcess data...")
    X_train, X_test, Y_train, Y_test = get_processed_data(data)

    # cross validation
    print("\nStart Cross Validation...")
    depth = dtree_tuning(X_train,Y_train)
    k_val = knn_tuning(X_train, Y_train)

    # predict
    print("\nStart testing with test set...")
    dtree = predict_tree(X_train, Y_train, X_test, Y_test, depth)
    knn = predict_knn(X_train, Y_train, X_test, Y_test, k_val)

    # ask for user input
    YorN = input("\nDo you want to test a review? Y/N : ")

    if YorN != "N":
        review = input("\nGreat! Please enter the review you want to test: ")
        predict_review(review, knn, dtree)
