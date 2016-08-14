#!/bin/python
#
# written by: Joshua White
# contributions by: default FLASK Example
# contributions by: Jeremy Fields
#

from flask import Flask, render_template, redirect, url_for, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import networkx as nx
import matplotlib.pyplot as plt

# this is my library
import CreateUserJson

# this is the local nocache library
from nocache import nocache

# webpp  variable
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

# sets the variables to be used throughout
input_output_csv = "./data/spo-tool-data.csv"
CreateUserJson.create_json_graph_file()

# sets the reusable form class for the web app
class ReusableForm(Form):
    subject = TextField('Subject:', validators=[validators.required()])
    predicate = TextField('Predicate:', validators=[validators.required()])
    object = TextField('Object:', validators=[validators.required()])

    def reset(self):
        blankData = MultiDict([ ('csrf', self.reset_csrf() ) ])
        self.process(blankData)

@nocache

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('hello'))
    return render_template('login.html', error=error)


@app.route("/hello", methods=['GET', 'POST'])
# default example function from FLASK example that has been modified
def hello():
    form = ReusableForm(request.form)
    try:
        dataSet = request.args.get('data')
    except:
		pass
	
    if dataSet == "fam":
        dataSet = "graphFile-FamFriends"
    elif dataSet == "strong":
        dataSet = "graphFile-Strong"
    elif dataSet == "weak":
        dataSet = "graphFile-Weak"
    else:
        dataSet = "graphFile"
    print form.errors

    # looks for the POST request from the browser
    if request.method == 'POST':

	# these are the objects that get returned from the browser
        sub=request.form['subject']
        pred=request.form['predicate']
        obj=request.form['object']

        # prints what happened to the CLI
        print sub, ",", pred, ",", obj

        # opens output csv, creates the string to write, writes it, closes the output csv
	file = open(input_output_csv, "a")
	stringtowrite = str(sub + "," + pred + "," + obj)
        file.write(stringtowrite.lower())
	file.write("\n")
	file.close()

        if form.validate():
	    # sends the notice of what happened to the user in the browser
	    flash(stringtowrite.lower())
	    # calls the function in the other script to convert the csv to the json graphFile
            CreateUserJson.create_json_graph_file()

        else:
            # prints the error notice of what happened to the user in the browser
            flash('Error: All the form fields are required. ')

    # returns the index.html to the browser
    return render_template("index.html", form=form,text=dataSet.lstrip())

if __name__ == "__main__":
    app.run()
