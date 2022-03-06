class Config(object):

    api_base_path = "https://api.openweathermap.org/data/2.5/onecall/timemachine"
    api_key = "bba50800ee5c6220db84106d61b3c894"

    previous_days_no = 5

    cities = [{
        'country': 'Canada',
        'city': 'Ottawa'
    },
    {
        'country': 'Canada',
        'city': 'Toronto'
    },
    {
        'country': 'Canada',
        'city': 'Montreal'
    },
    {
        'country': 'Canada',
        'city': 'Calgary'
    },
    {
        'country': 'Canada',
        'city': 'Vancouver'
    },
    {
        'country': 'US',
        'city': 'New York'
    },
    {
        'country': 'US',
        'city': 'Chicago'
    },
    {
        'country': 'US',
        'city': 'Los Angeles'
    },
    {
        'country': 'US',
        'city': 'San Francisco Bay Area'
    },
    {
        'country': 'US',
        'city': 'Seattle'
    }]

    DB_NAME = "weather"
    DB_USERNAME = "metauser"
    DB_PASSWORD = "metadata"
