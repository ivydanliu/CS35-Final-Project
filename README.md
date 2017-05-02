#Code Base of Reflection On Prediction of Yelp Review Star Rating 
This is a project by Hemeng Maggie Li, Chudan Ivy Liu, Jiawen Jasmine Zhu. 

(Since we can't select two partners on submission site, so two of us submit
one copy of the project, and the other one also submit one copy by herself. 
Please grade this content for all three of us)


#Install Required Dependencies
  1. Install package `TextBolb` 
     * Run with command 
       `pip install -U textblob`
       `python -m textblob.download_corpora`
  2. Install package `NLTK`
     * Run with commcand `sudo pip install -U nltk`
  3. Install package `geoplotlib`
     * Under the directory of `geoplotlib`, run with command:
       `pip install geoplotlib`


#Overview of Design Decisions

1. Machine Learning Part:
   * `main.py`:  
      is the executable of machine learning part
   * `data_processing_geo.py`:
      processes data from business json file of Yelp Dataset for data visualization
   * `data_processing_ml.py`:
      processes data from review json file of Yelp Dataset for machine learning 
      part of the project
   * `extract_features.py`:
      extracts features from a given review text
   * `training_tuning.py`:
      runs cross validation for the processed data using knn and decision tree 
      algorithm to determine the best parameters for training
   * `predict.py`:
      fits the model using training data, and predicts the test data
      There is also one function that predicts the review with knn.


2. Geographical Visualization Part:
   * `star_rating_geo.py`:  
      is the executable of star rating geographical plot
   * `price_range_geo.py`:  
      is the executable of price range geographical plot
