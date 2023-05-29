
from flask import Flask, render_template, request, redirect
from datetime import datetime

# FREE HTML TEMPLATES
# https://themewagon.com/author/mashuptemplate/
# https://html5up.net/
# https://www.creative-tim.com/bootstrap-themes/free
#

app = Flask(__name__)

def save_to_csv(data):
    email = data["email"]
    subject = data["subject"]
    message = data["message"]
    now = datetime.now()
    today = now.strftime(r"%Y/%m/%d %H:%M:%S")
    # writing a CSV document in database.csv
    with open(r"database.csv", mode="a") as database:
        file = database.write(f"\n{email},{subject},{message},{today}")
        database.close

# URL Parameters / variable rules
@app.route("/")
def my_home():
    return render_template("index.html")

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
# GET -> browser want to get info
# POST -> browser want to save info
def submit_form():
    if request.method == "POST":
        try:
            # transform the form answer into a dictionary
            data = request.form.to_dict()
            save_to_csv(data)
            return render_template("thankyou.html")
        except:
            return "data unsaved to database"
    else:
        return "EEROR: something went wrong"

# I'm using this way to mantain the Debug mode on
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)


# servidor do heroku


# python "D:\Documents\Coding\Curso Python 3\venv\0 Web Dev\server.py" $env:FLASK_APP = "server.py"
# $env:FLASK_DEBUG = "1"
# debug=True, use_reloader=False
# "D:\Documents\Coding\Curso Python 3>"set FLASK_APP=server.py

