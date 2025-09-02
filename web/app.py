from flask import Flask, render_template, request

from icecream import ic
ic.configureOutput(prefix=f'----- | ', includeContext=True)


import x



app = Flask(__name__)

# Main page
# friendly url inspired by twitter.com
# 127.0.0.1/whatever 
@app.get("/<username>")
def view_index(username):
    db, cursor = x.db()
    q = "SELECT * FROM users WHERE user_username = %s"
    cursor.execute(q, (username,))
    user = cursor.fetchone()
    ic(user)
    if user:
        return render_template("index.html", user = user)
    return "Ja der findes jo ikk en bruger med det username din FUCKING idiot"

# 127.0.0.1/search?first-name
# in flask, args is everything after the questionmark
# @app.get("/search")
# def view_search():
#     name = request.args.get("first-name", "")
#     last_name = request.args.get("last-name", "")
#     year = request.args.get("year", "")
#     fav_color = request.args.get("fav-color", "")
#     return f"Hi {name} {last_name}, the year is {year}. My favorite color is {fav_color}"

