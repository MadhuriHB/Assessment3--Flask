from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"


@app.route("/")
def index_page():
    """Show an index page."""

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    
    return render_template("index.html")


@app.route("/application-form")
def fill_form():
    """show the form to user"""

    return render_template("application-form.html")


@app.route("/application", methods=["POST"])
def process_application():
    """Show the response message with details filled in. """
    first_name = request.form.get("firstname")
    last_name = request.form.get("lastname")
    salary = request.form.get("salary")
    job = request.form.get("select")
    return render_template("application-response.html", firstname=first_name,
                            lastname=last_name, salary=salary, jobskill=job)


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")

