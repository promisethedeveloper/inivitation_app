from flask import Flask, request, render_template, redirect
from flask import session, make_response


app = Flask(__name__)

app.config["SECRET_KEY"] = "4534gdghjk5d#$RGR^HDG"


@app.route("/")
def home():
    """Greet Users and ask them for their secret code"""
    return render_template("home.html")


@app.route("/login")
def check_secret_code():
    """Set secret code and check if the Users entered the correct one or not"""
    SECRET = "goodluck_245"
    entered_code = request.args["secret_code"]
    if entered_code == SECRET:
        session["entered-pin"] = True
        return redirect("/secret-invite")
    else:
        return redirect("/")
        

@app.route("/secret-invite")
def show_secret_invite():
    """ Check to see if session contains 'entered-pin' (if user entered the correct secret code)

    - If it does, render the invite template

    - If session['entered-pin'] is missing or False, redirect user to the form to enter the secret code
    """
    if session.get("entered-pin", False):
        return render_template("invite.html")
    else:
        return redirect("/")