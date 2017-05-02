# please use python2 and 'pip install geoplotlib'
# to make sure you have the required dependencies
import pandas
import geoplotlib

# Load the data
data = pandas.read_csv('data/yelp_vegas_star_rating.csv')

# Read the star rating, latittude, longitude attributes
star_ratingL = (data['name'].tolist())
latL = (data['lat'].tolist())
lonL = (data['lon'].tolist())

# initialize the new data frames
lat1L= []
lon1L= []
lat2L= []
lon2L= []
lat3L= []
lon3L= []
colorl = []

# color the dots based on price range
for idx in range(len(star_ratingL)):
    if star_ratingL[idx] == 1:
        lat1L.append(latL[idx])
        lon1L.append(lonL[idx])
    elif star_ratingL[idx] == 2:
        lat2L.append(latL[idx])
        lon2L.append(lonL[idx])
    elif star_ratingL[idx] == 3:
        lat3L.append(latL[idx])
        lon3L.append(lonL[idx])


# add new dot layer
data1 = {'lat':lat1L, 'lon':lon1L}
geoplotlib.dot(data1, color = "blue")

data2 = {'lat':lat2L, 'lon':lon2L}
geoplotlib.dot(data2, color = "green")

data3 = {'lat':lat3L, 'lon':lon3L}
geoplotlib.dot(data3, color = "red")

# show the plot
geoplotlib.show()
