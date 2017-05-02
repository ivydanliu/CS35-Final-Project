from predict import *

if __name__ == '__main__' :

    # read and process data
    print("Reading files...")
    data = read_json(10000)

    print("\nProcess data...")
    X_train, X_test, Y_train, Y_test = get_processed_data(data)

    # cross validation without modifying label
    print("\nStart Cross Validation without modifying Label...")
    depth1 = dtree_tuning(X_train,Y_train)
    k_val1 = knn_tuning(X_train, Y_train)

    # predict withour modifying label
    print("\nStart testing with test set without modifying label...")
    dtree1 = predict_tree(X_train, Y_train, X_test, Y_test, depth)
    knn1 = predict_knn(X_train, Y_train, X_test, Y_test, k_val)


    # Modify the label, originally 5 stars, now into three catagories
    # non-favorable (-1), neutral (0), favorable (1)
    print("\nModifying the label of the data...")
    print("The original labels have five stars: 1,2,3,4,5")
    print("Now we classify the five kinds of labels into three catagories:")
    print("Non-favorable (-1): 1 star or 2 star")
    print("Neutral (0): 3 star")
    print("Favorable (-1): 4 star or 5 star")
    Y_train_new = process_label(Y_train)
    Y_test_new = process_label(Y_test)

    # cross validation with modified label
    print("\nStart Cross Validation after modifying label...")
    depth2 = dtree_tuning(X_train,Y_train_new)
    k_val2 = knn_tuning(X_train, Y_train_new)

    # predict with modified
    print("\nStart testing with test set after modifying label...")
    dtree2 = predict_tree(X_train, Y_train, X_test, Y_test, depth)
    knn2 = predict_knn(X_train, Y_train, X_test, Y_test, k_val)


    # ask for user input
    YorN = input("\nDo you want to test a review? Y/N : ")

    if YorN != "N":
        review = input("\nGreat! Please enter the review you want to test: ")
        print("\nNow predict the label of the review:")
        predict_review(review, knn1, dtree1)
        print("\nNow predict the catagory of the review:")
        predict_review(review, knn2, dtree2)
