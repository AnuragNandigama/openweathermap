import json, requests
import configs.config as config

config_obj = config.Config()

def get_weather_data_city(lat, lon, unix_date):
    url = "{0}?lat={1}&lon={2}&dt={3}&appid={4}".format(config_obj.api_base_path,lat, lon, unix_date, config_obj.api_key)
    response = requests.get(url)
    if (response.status_code==200):
        data = json.loads(response.text)
        return data
    else:
        return 'Error'