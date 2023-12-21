#Importing flask module in the project
from flask import Flask

#Create an object of the Flask class
app = Flask(__name__)

#The route() function of the Flask class 
@app.route("/")

#‘/’ URL is bound with first_flask function.
def first_flask():

    return "This is my first flask program"
@app.route("/Shobhit")
def shobhit_page():
    return " Hello All, welllllcome to shobhit WEB page"

#run the application on local server
app.run()
