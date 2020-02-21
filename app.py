from Naked.toolshed.shell import execute_js, muterun_js
import requests
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


# call(["npm","start","cd ~/home_automation/index.js" ],shell=True)
@app.route("/")
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True, threaded = True)
    success = execute_js('../home_automation')


