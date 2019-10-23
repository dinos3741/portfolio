from flask import Flask, render_template
from flask import request
import csv

application = Flask(__name__)

# we create an environment variable: export FLASK_APP=application.py, and then we run the server: flask run
# we enter the development mode by setting the environment variable: export FLASK_ENV=development

# this is a root route, ie. the server sends only data when accessing its root / directory
@application.route('/')
def my_home():
    # we can return a specific html file we created as long as its located in the /templates folder.
    # Also javascript and css files should be located in the /static folder. Favicon (the icon to be displayed in
    # the browser window) should be also in the static folder. All the assets (images etc) should be placed in the
    # static folder also.

    # the home method returns the rendering of the index.html file to render the home page:
    return render_template('index.html')

# this is a /blog directory with a different content:
@application.route('/blog')
def blog():
    return 'These are my thoughts on blogs in general!'
# flask converts the text in html format

def write_to_file(data):
    # open file to append new emails received:
    with open("./database.txt", 'a') as file:
        mail = "New mail received from: " + data['email'] + ", subject: " + data['subject'] + ", Message: " \
               + data['message'] + "\n"
        file.writelines(mail)

def write_to_cs(data):
    # open a .csv file to store data row by row
    with open("./database2.csv", 'a', newline='') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        fieldnames=['email', 'subject', 'message']
        #csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer = csv.DictWriter(database, fieldnames)  # writes a dictionary format directly
        #csv_writer.writeheader()
        #csv_writer.writerow([email,subject,message])
        csv_writer.writerow(data)

# we create a new method that runs when we hit the submit_form end point.
# a url end point (submit_form) needs to exist with the same name in the index.html
@application.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":  # we specified the method as post in the html in the form action
        data = request.form.to_dict()  # request.form gets the data from the front end and we transform it to dictionary
        # write all emails received to a file
        #write_to_file(data)
        write_to_cs(data)
        return 'form submitted!'
    else:
        return "Something went wrong... try again"

# to deploy the webpage to a host, we need to run: pip freeze > requirements.txt, and this automatically
# captures the package installed in the current environment and creates the requirements and dependencies
# needed in order to run the web app in any environment.
# we create a new empty repository in github, we clone it (get the address from the url of the repository), and
# then open a terminal, and run: git clone <http of github account>. This copies the github structure onto the local
# computer and creates a directory with the repository name. Then we copy to this directory the server.py, the
# database.csv, the static and templates directories and the requirements.txt file. 
