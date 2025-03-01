#!/usr/bin/python3
"""
Flask web application that displays a page with filters
for states, cities, and amenities.
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """
    Display a HTML page with filters for states, cities, and amenities.
    """
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    amenities = storage.all(Amenity).values()
    sorted_amenities = sorted(amenities, key=lambda amenity: amenity.name)
    return render_template('10-hbnb_filters.html',
                           states=sorted_states,
                           amenities=sorted_amenities)


@app.teardown_appcontext
def teardown_db(exception):
    """
    Remove the current SQLAlchemy Session after each request.
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
