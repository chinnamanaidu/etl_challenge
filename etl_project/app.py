from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_costa

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/weather_app")


# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    # @TODO: YOUR CODE HERE!
    temperatures = mongo.db.temperature.find_one()
    #return render_template("index.html", listings=listings)
    # Return template and data
    return render_template("index.html", vacation=temperatures)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    # Run the scrape function and save the results to a variable
    # @TODO: YOUR CODE HERE!

    # Update the Mongo database using update and upsert=True
    # @TODO: YOUR CODE HERE!

    # Redirect back to home page
    temperatures = mongo.db.temperature
    temperatures_data = scrape_costa.scrape_info()
    temperatures.update({}, temperatures_data, upsert=True)
    return redirect("/", code=302)



if __name__ == "__main__":
    app.run(debug=True)
