from flask import Flask, request, render_template
import requests
import re

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', results=[], err_msg="")

@app.route("/search")
def search():
    query = request.args.get('query')
    results = requests.get("http://dnd.hackdartmouth.org/%s" % query).json()

    if request.is_xhr:
        return render_template('search.html', results=results)
    else:
        return render_template('index.html', results=results)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False)
