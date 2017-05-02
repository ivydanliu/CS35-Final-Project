import json
import csv

def read_json_geo(filename_to_read="yelp_academic_dataset_business.json"):
    """ This function takes in one arguments:
            1) filename_to_read, this is a default argument, the name of the dataset file

        The json objects we read are business object from the Yelp Dataset. We
        want to extract the latitude, longitude and price range for each business
        in the dataset. If yelp does not provide the price range for this business,
        we will ignore that business.

        This function returns a list of list, with the form [price range, lat, long]
    """
    # header for each column, name actually stands for price range, but geoplotlib
    # only takes in data with this formate
    result = [['name', 'lat', 'lon']]

    # loop through all the lines of the file, each line is a json object
    with open(filename_to_read, "r") as f:
        for line in f:

            # load the data
            data = json.loads( line )

            # get the price range of the business, some of the business does not
            # have this infomation, we will ignore this business
            price = None
            attributes = data['attributes']
            if attributes != None:
                for a in attributes:
                    if a.startswith('RestaurantsPriceRange2'):
                        price = a[-1]

            if price == None:
                continue

            # get the latitude, and longitude of the business
            latitude = data['latitude']
            longitude = data['longitude']

            # append to the result
            row = [price, str(latitude), str(longitude)]
            result.append(row)

    return result



def read_json_vegas(filename_to_read="yelp_academic_dataset_business.json"):
    """ This function takes in one arguments:
            1) filename_to_read, this is a default argument, the name of the dataset file

        The json objects we read are business object from the Yelp Dataset. We
        want to extract the latitude, longitude and price range for each business
        in Las Vegas. If the business is not Las Vegas or yelp does not provide
        the price range, we will ignore that business

        This function returns a list of list, with the form [price range, lat, long]
    """
    # header for each column, name actually stands for price range, but geoplotlib
    # only takes in data with this formate
    result = [['name', 'lat', 'lon']]

    # loop through all the lines of the file, each line is a json object
    with open(filename_to_read, "r") as f:
        for line in f:

            # load the data
            data = json.loads( line )

            # get the city and state of the business, if it is not in Las Vegas
            # or the state is not NV, we will ignore the city
            city = data['city']
            state = data['state']

            if city != "Las Vegas" or state != "NV":
                continue

            # get the price range of the business, some of the business does not
            # have this infomation, we will ignore this business
            price = None
            attributes = data['attributes']
            if attributes != None:
                for a in attributes:
                    if a.startswith('RestaurantsPriceRange2'):
                        price = a[-1]

            if price == None:
                continue

            # get the latitude, and longitude of the business
            latitude = data['latitude']
            longitude = data['longitude']

            # append to the result
            row = [price, str(latitude), str(longitude)]
            result.append(row)

        return result



def read_json_vegas_rating(filename_to_read="yelp_academic_dataset_business.json"):
    """ This function takes in one arguments:
            1) filename_to_read, this is a default argument, the name of the dataset file

        The json objects we read are business object from the Yelp Dataset. We
        want to extract the latitude, longitude and ratings for each business
        in Las Vegas.

        This function returns a list of list, with the form [ratings, lat, long]
    """
    # header for each column, name actually stands for price range, but geoplotlib
    # only takes in data with this formate
    result = [['name', 'lat', 'lon']]

    # loop through all the lines of the file, each line is a json object
    with open(filename_to_read, "r") as f:
        for line in f:

            # load the data
            data = json.loads( line )

            # get the city and state of the business, if it is not in Las Vegas
            # or the state is not NV, we will ignore the city
            city = data['city']
            state = data['state']

            if city != "Las Vegas" or state != "NV":
                continue


            # get the latitude, longitude and ratings of the business
            latitude = data['latitude']
            longitude = data['longitude']

            # get star rating, and classify it into three catagories
            star = data['stars']

            if 0 <= star <= 2.0:
                rating = 1
            elif 2.5 <= star <= 3.5:
                rating = 2
            else:
                rating = 3

            # append to the result
            row = [rating, str(latitude), str(longitude)]
            result.append(row)

        return result



def write_to_csv( list_of_rows, filename):
    """ This function takes in two arguments:
            1) list_of_rows, list of list with [price range, lat, long] information
                             for each business
            2) filename_to_read, this is a default argument, the name of the csv
                                 file we want at the end

        This function does not return anything, but it writes all the information
        in the input list of list, with the form [price range, lat, long], to
        a csv file with appropriate headers (heads include in the list_of_rows).

        The csv file is then used for data visualization
    """
    try:
        # open the csv file
        csvfile = open( filename, "w", newline='' )
        filewriter = csv.writer( csvfile, delimiter=",")

        # loop though each row in the input list
        for row in list_of_rows:
            filewriter.writerow( row )

        # close the file
        csvfile.close()

    except:
        print("File", filename, "could not be opened for writing...")
