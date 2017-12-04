import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Create our session (link) from Python to the DB
session = Session(engine)

# Save references to the invoices and invoice_items tables
Station = Base.classes.Stations
Measurement = Base.classes.Measurements

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


@app.route("/")
def welcome():
     """List all available api routes."""
     return (
         f"Avalable Routes:<br/>"
         f"/api/v1.0/precipitation <br/>"
         f"- Dates and temperature observations from the last year<br/>"

         f"/api/v1.0/stations"
         f"- List of stations<br/>"

         f"/api/v1.0/tobs"
         f"- Temperature Observations from the past year<br/>"

         f"/api/v1.0/<start>"
         f"- Minimum temperature, the average temperature, and the max temperature for a given start day<br/>"

         f"/api/v1.0/<start>/<end>"
         f"- Minimum temperature, the average temperature, and the max temperature for a given start-end range<br/>"
     )

@app.route("/api/v1.0/precipitation")

@app.route("/api/v1.0/stations")

@app.route("/api/v1.0/tobs")

@app.route("/api/v1.0/<start>")

@app.route("/api/v1.0/<start>/<end>")

if __name__ == '__main__':
    app.run(debug=True)