from flask import Flask, render_template, request



from icecream import ic
ic.configureOutput(prefix=f'----- | ', includeContext=True)

app = Flask(__name__)


@app.get("/")
def view_index():
    return "Janus"

# 127.0.0.1/search?first-name
# in flask, args is everything after the questionmark
@app.get("/search")
def view_search():
    name = request.args.get("first-name", "")
    last_name = request.args.get("last-name", "")
    year = request.args.get("year", "")
    fav_color = request.args.get("fav-color", "")
    return f"Hi {name} {last_name}, the year is {year}. My favorite color is {fav_color}"

