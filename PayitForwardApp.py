from flask import Flask, render_template

app=Flask(__name__)

@app.route('/home')
def home(): 
	return render_template("home.html")

@app.route('/donate')
def donate(): 
	return render_template("donate.html")

@app.route('/map')
def map(): 
	return render_template("map.html")

@app.route('messaging')
def messaging(): #Hello!
	return render_template("messaging.html")
	