from flask import Flask, render_template, request, url_for, redirect, session
import requests
import os
import dotenv

# load env variables
dotenv.load_dotenv()

# read api key from env
API_KEY = os.getenv("API_KEY")

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")


@app.route("/")
def index():
    # retrieve data from session
    data = session.get("data")
    # make sure data is not empty
    if data:
        if 'code' in data:
            print(data)
            session.clear()
            # if error code in response, render error page
            return render_template("error.html", response=data['msg'])
        else:
            session.clear()
            # render content page
            return render_template("content.html", response=data)
    return render_template("index.html")


@app.route("/getimage", methods=["POST"])
def get_image():
    response = api_call(request.form.get("date"))
    # store response in session
    session["data"] = response
    # print response
    print(response)
    # return to referer
    return redirect(request.referrer)


def api_call(date: str, api_key: str = API_KEY) -> dict:
    # api call to nasa apotd api
    url = "https://api.nasa.gov/planetary/apod"
    params = {"date": date, "api_key": api_key}
    response = requests.get(url, params=params)
    return response.json()
