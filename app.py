from datetime import datetime, timedelta
import json
import configs.config as config
from pymongo import MongoClient
from http import client
import database.db_queries as dbq
import utils.utilities as ut
import services.service as sv

config_obj = config.Config()
collection = {}
DB_ATLAS_URI = "mongodb+srv://{0}:{1}@cluster0.koejp.mongodb.net/{2}?retryWrites=true&w=majority".format(config_obj.DB_USERNAME, config_obj.DB_PASSWORD, config_obj.DB_NAME)
client = MongoClient(DB_ATLAS_URI)
db = client.weather
collection = db.city_weather


def create_data_load(days_unix_timestamp):
    data_dump = []
    for el in config_obj.cities:
        loc = ut.geolocator.geocode(el['city']+','+ el['country'])
        for i in range(0, len(days_unix_timestamp)):
            data = sv.get_weather_data_city(loc.latitude, loc.longitude, days_unix_timestamp[i])
            if data != 'Error':
                data['year'] = datetime.fromtimestamp(data['current']['dt']).strftime('%Y')
                data['month'] = datetime.fromtimestamp(data['current']['dt']).strftime('%B')
                data['day'] = datetime.fromtimestamp(data['current']['dt']).strftime('%d')
                data['city'] = el['city']
                data['country'] = el['country']
                data_dump.append(data)
            else:
                print('Error fetching data from API call')
    return data_dump

def create_max_temp_stats_data_set(collection_cursor):
    max_temp_stats_city_month_dict = {}
    max_temp_stats_city_month = []
    for doc in collection_cursor:
        max_temp_stats_city_month_dict['city'] = doc['_id']['city']
        max_temp_stats_city_month_dict['country'] = doc['max_temp_collection']['country']
        max_temp_stats_city_month_dict['temp'] = doc['max_temp_collection']['current']['temp']
        max_temp_stats_city_month_dict['dt'] = datetime.fromtimestamp(doc['max_temp_collection']['current']['dt']).strftime('%Y-%m-%d')
        max_temp_stats_city_month.append(max_temp_stats_city_month_dict)
    return max_temp_stats_city_month

def create_stats_by_date_data_set(collection_cursor):
    stats_by_date_data_dict = {}
    stats_by_date_data = []
    for doc in collection_cursor:
        stats_by_date_data_dict['avg_temp'] = doc['avg_temp']
        stats_by_date_data_dict['min_temp'] = doc['min_temp']
        stats_by_date_data_dict['min_temp_loc'] = doc['min_temp_collection']['city']
        stats_by_date_data_dict['max_temp'] = doc['max_temp']
        stats_by_date_data_dict['max_temp_loc'] = doc['max_temp_collection']['city']
        stats_by_date_data.append(stats_by_date_data_dict)
    return stats_by_date_data

days_unix_timestamp = ut.get_n_days_unix_timestamp(config_obj.previous_days_no)
    
    
#make the API call to fetch data, create dump
data_dump = create_data_load(days_unix_timestamp)
#Load the data into DB
collection.insert_many(data_dump)    

#Fetch the collection cursors
max_temp_stats_city_month_cursor = collection.aggregate(dbq.max_temp_stats)
stats_date_cursor = collection.aggregate(dbq.get_stats)

#Data setcontaining the location, date and temperature of the highest temperatures reported by location and month.
max_temp_city_month_data = create_max_temp_stats_data_set(max_temp_stats_city_month_cursor)

with open('./output_data/max_temp_city_month.txt', 'a') as fp:
    json.dump(max_temp_city_month_data, fp)

#Dataset containing the average temperature, min temperature, location of min temperature, and location of max 
#temperature per day.
stats_data_day = create_stats_by_date_data_set(stats_date_cursor)

with open('./output_data/temp_stats_day.txt', 'a') as fp:
    json.dump(stats_data_day, fp)




   