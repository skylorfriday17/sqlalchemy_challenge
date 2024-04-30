# Import the dependencies.
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

import datetime as dt


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///../Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################

app = Flask(__name__)

#################################################
# Flask Routes
#################################################

# List routes on homepage
@app.route('/')
def home():
    return(
        f'Here are a list of routes to use!<br/>'
        f'/api/v1.0/precipitation<br/>'
        f'/api/v1.0/stations<br/>'
        f'/api/v1.0/tobs<br/>'
        f'/api/v1.0/(input start date: yyyy-mm-dd)<br/>'
        f'/api/v1.0/(input start date: yyyy-mm-dd)/(input end date: yyyy-mm-dd)<br/>'
    )

# Create route for the last year of precipitation data in JSON format
@app.route('/api/v1.0/precipitation')
def precipitation():

    query_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    precipitation = session.query(measurement.date, measurement.prcp).\
    filter(measurement.date >= query_date).all()

    prcp_dict = {}

    for date, prcp in precipitation:
        prcp_dict[date] = prcp

    return jsonify(prcp_dict)

# Create route to list jsonified station data
@app.route('/api/v1.0/stations')
def station():

    stations = session.query(Station.station, Station.name, Station.latitude, Station.longitude,
                             Station.elevation).all()
    stations_list = []
    for station, name, latitude, longitude, elevation in stations:
        s_dict = {}
        s_dict['station'] = station
        s_dict['name'] = name
        s_dict['latitude'] = latitude
        s_dict['longitude'] = longitude
        s_dict['elevation'] = elevation

        stations_list.append(s_dict)

    return jsonify(stations_list)

# Create a route to give jsonified temperature data for the last year of the most active station
@app.route('/api/v1.0/tobs')
def tobs():

    query_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    most_active = session.query(measurement.date, measurement.tobs).\
                        filter(measurement.date >= query_date).\
                        filter(measurement.station == 'USC00519281').all()
    
    tobs_dict = {}
    for date, tobs in most_active:
        tobs_dict[date] = tobs

    return jsonify(tobs_dict)

# Create a route to take in a start date to find min, avg and max temp data
@app.route('/api/v1.0/<start>')
def start_date(start):
    start_data = session.query(func.min(measurement.tobs).label('min_temp'), 
                               func.avg(measurement.tobs).label('avg_temp'), 
                               func.max(measurement.tobs).label('max_temp')).\
                        filter(measurement.date >= start).first()
    
    min_temp = start_data.min_temp
    avg_temp = start_data.avg_temp
    max_temp = start_data.max_temp

    return jsonify({
        'Min Temp' : min_temp,
        'Average Temp' : avg_temp,
        'Max Temp' : max_temp
    })

# Create a route to take in a start and end date to find min, avg and max temp data
@app.route('/api/v1.0/<start>/<end>')
def date_range(start, end):
    date_data = session.query(func.min(measurement.tobs).label('min_temp'), 
                                   func.avg(measurement.tobs).label('avg_temp'), 
                                   func.max(measurement.tobs).label('max_temp')).\
                        filter(measurement.date >= start).\
                        filter(measurement.date <= end).first()
    
    min_temp = date_data.min_temp
    avg_temp = date_data.avg_temp
    max_temp = date_data.max_temp

    return jsonify({
        'Min Temp' : min_temp,
        'Average Temp' : avg_temp,
        'Max Temp' : max_temp
    })

if __name__ == '__main__':
    app.run(debug=True)                       