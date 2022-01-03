# imports
from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# use flask pymongo to set up connection to database
app.config["MONGO_URI"] = "mongodb://localhost:27017/marsData_db"
mongo = PyMongo(app)

@app.route("/")
def index():
    # access information from database
    marsData = mongo.db.marsData.find_one()
    #print(marsData)
    return render_template("index.html", mars=marsData)

@app.route("/scrape")
def scrape():
    # reference to database collection
    marsTable = mongo.db.marsData

    # drop table if exists
    mongo.db.marsData.drop()

    # scrape mars script
    marsData = scrape_mars.scrape_all()

    #load dictionary into mongoDB
    marsTable.insert_one(marsData)

    # go back to index route
    return redirect("/")

if __name__== "__main__":
    app.run()