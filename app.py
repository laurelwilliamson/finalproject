from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)


@app.route("/")
def index():
    # mars_record = mongo.db.mars.find_one()
    # print(mars_record)
    return render_template("index.html")


@app.route("/country")
def country():

    return render_template("country.html")

@app.route("/viz")
def viz():

    return render_template("viz.html")

@app.route("/processingmethod")
def processingmethod():

    return render_template("processingmethod.html")        

@app.route("/country_grouped")
def country_grouped():

    return render_template("country_grouped.html")

@app.route("/map")
def map():

    return render_template("map.html")
   


if __name__ == "__main__":
    app.run()
