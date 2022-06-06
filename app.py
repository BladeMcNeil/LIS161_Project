from flask import Flask, render_template
from groups import *

app = Flask(__name__)

@app.route('/') #homepage routing to index.html
def index():
    return render_template('index.html')

@app.route('/about') #about page of the admmins
def about():
    return render_template('about.html')

@app.route('/author') #about page of the author
def author():
    return render_template('author.html')

@app.route('/Survey_Corps/<c_name>') #list of characters of a certain group
def display(c_name):
    chars = squads[c_name]

    return render_template('characters.html',c_name_template = c_name, chars_template = chars)

@app.route('/Survey_Corps/<c_name>/<int:c_id>')  #accessing profiles within the array
def individual(c_name,c_id):
    c_profile = squads[c_name][c_id]
    
    return render_template('profiles.html', c_profile_template = c_profile)


if __name__ == "__main__":
    app.run(debug=True)