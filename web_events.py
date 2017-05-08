from flask import Flask, render_template, request
import facebook_run
#import os

app = Flask(__name__)

@app.route("/")  
def home():
    return render_template('home.html')

@app.route("/results")  # crea otra pagina. Esta es el About
def results():   #name of the function to call the page about in html
    city = request.values.get('city')
    num_results = request.values.get('num_results')
    if city and num_results:
        events_list = facebook_run.search_events(city, num_results) #run the facebook api function
    else:
        city = "New York"
        num_results = 5
        events_list = facebook_run.search_events(city, num_results)
    return render_template('results.html', city = city, num_results = num_results, events_list= events_list )	#calls the html file

@app.route("/about")  # crea otra pagina. Esta es el About
def about():   #name of the function to call the page about in html
    return render_template('about.html')  #calls the html file	

if __name__ == "__main__":
    app.run()  #when wokring on a local port
    #port = int(os.environ.get("PORT", 5000))  #when deploying it to Heroku
    #app.run(host="0.0.0.0", port=port)


