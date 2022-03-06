# openweathermap

### Create Workflow in Python according to the following requirements:


Extract the last 5 days of data from the free API: https://api.openweathermap.org/data/2.5/onecall/timemachine (Historical weather data) from 10 different locations to choose by the candidate.

a. Build a repository of data where we will keep the data extracted from the API. This repository should only have deduplicated data. Idempotency should also be guaranteed.

b. Build another repository of data that will contain the results of the following calculations from the data stored in step 2.

**Q1: _A dataset containing the location, date and temperature of the highest temperatures reported by location and month_.**

**Q2: _A dataset containing the average temperature, min temperature, location of min temperature, and location of max temperature per day_.**

### Approach:
- Dockerized Python app
- Database: MongoDB Atlas (Cloud)
    - Load the data with date transformations into a colleciton
    - Build the Query in the backed for Q1, Q2 
    - Since its cloud, there aren't any dependencies to Dockerize
    - User access can be given as requested to the DB
