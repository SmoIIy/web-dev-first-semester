from flask import Flask, render_template, request

from icecream import ic
ic.configureOutput(prefix=f'----- | ', includeContext=True)


import x

app = Flask(__name__)


##############################
@app.get("/")
def view_index():
    try:
        return render_template("view_login.html")
    except:
        # wrong
        pass
    finally:
        # happens after try or except
        pass

##############################
@app.get("/signup")
def view_signup():
    try:
        return render_template("signup.html")
        pass
    except:
        pass
    finally:
        pass

##############################
@app.get("/home")
def view_home():
    pass

##############################
# @app.get("/explore")
# def view_explore():
#     pass

##############################
@app.get("/messages")
def view_messages():
    pass

##############################
@app.get("/notifications")
def view_notifications():
    pass

##############################
@app.get("/bookmarks")
def view_explore():
    pass

##############################
@app.get("/profile")
def view_profile():
    pass

##############################
@app.get("/lists")
def view_lists():
    pass

##############################
@app.get("/more")
def view_more():
    pass

##############################
##############################
##############################
@app.post("/tweet")
def post_tweet():
    pass

##############################
##############################
##############################
@app.post("/search")
def post_search():
    pass

##############################
##############################
##############################
@app.post("/login")
def post_login():
    try:
        user_email = request.form.get("user_email", "")
        user_password = request.form.get("user_password", "")
        return f"{user_email} {user_password}"
    except: 
        pass
    finally:
        pass




##############################
##############################
##############################
@app.post("/signup")
def post_signup():
    try:
        user_email = request.form.get("user_email", "")
        user_password = request.form.get("user_password", "")
        hashed_password = x.hash_password(user_password)
        db, cursor = x.db()
        # INSERT INTO users VALUES(NULL, "@b", "secret")
        q = 'INSERT INTO users VALUES(NULL, %s, %s)'
        cursor.execute(q, (user_email, hashed_password))
        db.commit()
        return "true"
    except Exception as ex:
        ic(ex)
        return str(ex)
    finally:
        if "cursor" in locals():
            cursor.close()
        if "db" in locals():
            db.close()


##############################
##############################
##############################
@app.delete("/delete")
def unlike_tweet():
    pass

##############################
##############################
##############################
@app.put("/profile")
def update_profile():
    pass

# GET       Is to get html
# POST      Is used for saving data in the system
# Put       Is used to update all rows except the ID
# Patch     Is used to update on or more cell
# Delete    Is used to delete a resource




# Main page
# friendly url inspired by twitter.com
# 127.0.0.1/whatever 
"""
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
"""

# 127.0.0.1/search?first-name
# in flask, args is everything after the questionmark
# @app.get("/search")
# def view_search():
#     name = request.args.get("first-name", "")
#     last_name = request.args.get("last-name", "")
#     year = request.args.get("year", "")
#     fav_color = request.args.get("fav-color", "")
#     return f"Hi {name} {last_name}, the year is {year}. My favorite color is {fav_color}"

