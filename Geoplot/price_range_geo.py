# please use python2 and run 'pip install geoplotlib'
# in terminal to make sure you have the required
# dependencies
import pandas
import geoplotlib

# Load the data
data = pandas.read_csv('data/yelp_vegas_price_level.csv')

# Read the price range, latittude, longitude attributes
price_rangeL = (data['name'].tolist())
latL = (data['lat'].tolist())
lonL = (data['lon'].tolist())

# initialize the new data frames
lat1L= []
lon1L= []
lat2L= []
lon2L= []
lat3L= []
lon3L= []
lat4L= []
lon4L= []
colorl = []

# color the dots based on star rating
for idx in range(len(star_ratingL)):
    if price_rangeL[idx] == 1:
        lat1L.append(latL[idx])
        lon1L.append(lonL[idx])
    elif price_rangeL[idx] == 2:
        lat2L.append(latL[idx])
        lon2L.append(lonL[idx])
    elif price_rangeL[idx] == 3:
        lat3L.append(latL[idx])
        lon3L.append(lonL[idx])
    elif price_rangeL[idx] == 4:
        lat4L.append(latL[idx])
        lon4L.append(lonL[idx])

# add new dot layer
data1 = {'lat':lat1L, 'lon':lon1L}
geoplotlib.dot(data1, color = "black")

data2 = {'lat':lat2L, 'lon':lon2L}
geoplotlib.dot(data2, color = "blue")

data3 = {'lat':lat3L, 'lon':lon3L}
geoplotlib.dot(data3, color = "green")

data4 = {'lat':lat4L, 'lon':lon4L}
geoplotlib.dot(data4, color = "red")

# show the plot
geoplotlib.show()
