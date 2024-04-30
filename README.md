# sqlalchemy_challenge
---
## Description
In this challenge I was able to utilize SQLalchemy with Python to get insight on SQLite data about Hawaiian Weather data.

### Jupyter Notebook
In this challenge I looked at temperature and precipitation data in Hawaii for the most recent year in the data. I then plotted a line graph using Matplotlib to represent the change in precipitation over the course of the last year and give a brief statistical summary using Pandas. 

In the second part of the notebook I looked at the most active station in Hawaii based upon the total entry count for each station. When looking at the most active station specifically I then found the minimum, maximum and average temperature. I then plotted a histogram based on frequency of temperatures for the last year of data.

### Python File
In the app.py python file I was able to use Flask to create an API route to access the Hawaii weather data from a local browser. I created multiple routes first of which is used to list the available routes. Second is to access the last year of precipitation data in JSON format. Third is to look at all the different stations in Hawaii where data was recorded. Fourth is a route to give jsonified temperature data for the last year of the most active station. Lastly I was able to code a route that takes in a start date in the address and gives a minimum, average and maximum temperature from the given start date to the last date in the data set. Also you can add an end date to shorten or get different results for different dates!

## Resources
In this challenge I relied heavily on the Xpert Learning Assistant AI along with all class material for this module. I occasionally used google to get help on SQLalchemy documentation.