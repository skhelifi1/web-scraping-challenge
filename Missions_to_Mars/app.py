from flask import Flask, render_template, redirect
import pymongo
import scrape_mars

# set up Flask
app = Flask(__name__)

# connect to mongoclient
conn = "mongodb://localhost:27017/mars"
client = pymongo.MongoClient(conn)

# Route to render index.html template using data from Mongo
@app.route("/")
def index():

    # Find one record of data from the mongo database
    mars_collection_data = pymongo.db.collection.find_one()

    # Return template and data
    return render_template("index.html", mars_data_init=mars_collection_data)


@app.route("/scrape")
def scrape():

    # Run the scrape function
    mars_data = scrape_mars.scrape()

    
    pymongo.db.collection.update({}, mars_data, upsert=True)

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)