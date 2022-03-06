from datetime import datetime, timedelta
import configs.config as config
from geopy.geocoders import Nominatim

config_obj = config.Config()
geolocator = Nominatim(user_agent='OpenWeather')

days_unix_timestamp = []
data_collection = []

def get_n_days_unix_timestamp(n):
    for i in range(1, n+1):
        yesterday = datetime.today() - timedelta(i)
        unix_time= yesterday.strftime("%s")
        days_unix_timestamp.append(unix_time)
    return days_unix_timestamp

def get_month_from_unix_timestamp(n):
    dt = datetime.fromtimestamp(n).strftime('%B')
    return dt

