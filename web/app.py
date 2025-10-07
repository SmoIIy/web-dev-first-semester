from flask import Flask, render_template, request, session, redirect, url_for
from flask_session import Session
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
import x 
import time
import uuid
import os

from icecream import ic
ic.configureOutput(prefix=f'----- | ', includeContext=True)

app = Flask(__name__)

# Set the maximum file size to 10 MB
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024   # 1 MB

app.config['SESSION_TYPE'] = 'filesystem'
Session(app)
 

##############################
##############################
##############################
def _____USER_____(): pass 
##############################
##############################
##############################

@app.get("/")
def view_index():
   
    return render_template("index.html")

##############################
@app.get("/login")
def view_login():
    if session.get("user", ""): return redirect(url_for("view_home"))

    message = request.args.get("message", "")
    return render_template("login.html", message=message)

##############################
@app.post("/login")
def handle_login():
    try:
        # Validate
        user_email = x.validate_user_email()
        user_password = x.validate_user_password()
        # Connect to the database
        q = "SELECT * FROM users WHERE user_email = %s"
        db, cursor = x.db()
        cursor.execute(q, (user_email,))
        user = cursor.fetchone()
        if not user: raise Exception("User not found", 400)

        if not check_password_hash(user["user_password"], user_password):
            raise Exception("Invalid credentials", 400)

        user.pop("user_password")

        session["user"] = user
        return redirect(url_for("view_home"))

    except Exception as ex:
        ic(ex)
        if ex.args[1] == 400: return redirect(url_for("view_login", message=ex.args[0]))
        return "System under maintenance", 500
    finally:
        if "cursor" in locals(): cursor.close()
        if "db" in locals(): db.close()

##############################
@app.get("/signup")
def view_signup():
    message = request.args.get("message", "")
    return render_template("signup.html", message=message, x=x)

##############################
@app.post("/signup")
def handle_signup():
    try:
        x.validate_user_username()
        return "ok"
        # Validate
        user_email = x.validate_user_email()
        user_password = x.validate_user_password()
        user_username = x.validate_user_username()
        user_first_name = x.validate_user_first_name()

        user_hashed_password = generate_password_hash(user_password)

        # Connect to the database
        q = "INSERT INTO users VALUES(%s, %s, %s, %s, %s)"
        db, cursor = x.db()
        cursor.execute(q, (None, user_email, user_hashed_password, user_username, user_first_name))
        db.commit()
        return redirect(url_for("view_login", message="Signup successful. Proceed to login"))
    except Exception as ex:
        ic(ex)
        if ex.args[1] == 400: return redirect(url_for("view_signup", message=ex.args[0]))
        if "Duplicate entry" and user_email in str(ex): return redirect(url_for("view_signup", message="Email already registered"))
        if "Duplicate entry" and user_username in str(ex): return redirect(url_for("view_signup", message="username already registered"))
        return "System under maintenance", 500
    finally:
        if "cursor" in locals(): cursor.close()
        if "db" in locals(): db.close()


##############################
@app.get("/home")
@x.no_cache
def view_home():
    try:
        # user = session.get("user", "")
        # if not user: return redirect(url_for("view_login"))
        db, cursor = x.db()
        q = "SELECT * FROM users JOIN posts ON user_pk = post_user_fk ORDER BY RAND() LIMIT 5"
        cursor.execute(q)
        tweets = cursor.fetchall()
        ic(tweets)

        q = "SELECT * FROM trends ORDER BY RAND() LIMIT 3"
        cursor.execute(q)
        trends = cursor.fetchall()
        ic(trends)



        q = "SELECT * FROM users WHERE user_pk != 1 ORDER BY RAND() LIMIT 3"
        cursor.execute(q)
        suggestions = cursor.fetchall()
        ic(suggestions)


        return render_template("home.html", tweets=tweets, trends=trends)
    except Exception as ex:
        ic(ex)
        return "error"
    finally:
        if "cursor" in locals(): cursor.close()
        if "db" in locals(): db.close()




##############################
@app.get("/logout")
def handle_logout():
    try:
        session.clear()
        return redirect(url_for("view_login"))
    except Exception as ex:
        ic(ex)
        return "error"
    finally:
        pass







##############################
@app.get("/ajax")
def view_ajax():
    try: 
        return render_template("ajax.html")
    except Exception as ex:
        ic(ex)
        return "error"
    finally:
        pass


##############################
@app.get("/tweet")
def get_tweet():
    try:
        return "tweet"
    except Exception as ex:
        ic(ex)
        return "error"
    finally:
        pass

##############################
@app.get("/ajax-post")
def view_ajax_post():
    try: 
        return render_template("ajax_post.html")
    except Exception as ex:
        ic(ex)
        return "error"
    finally:
        pass

##############################
@app.post("/save")
def handle_save_post():
    try: 
        user_name = request.form.get("user_name", "give me a name")
        user_last_name = request.form.get("user_last_name", "give me a last name")
        # Dictionary in python  is JSON in javascript
        user = {
            "user_name": user_name.title(),
            "last_name" : user_last_name.upper()
        }
       
        return user
    except Exception as ex:
        ic(ex)
        return "error"
    finally:
        pass

##############################
@app.get("/ajax-heart")
def view_ajax_heart():
    try: 
        return render_template("ajax_heart.html")
    except Exception as ex:
        ic(ex)
        return "error"
    finally:
        pass

##############################
@app.get("/api-like-tweet")
def handle_like_tweet():
    try: 
        # TODO: Validate the data
        # TODO: Get the logged user id
        # TODO: Connect to the database
        # TODO: Insert the liking of a tweet in the table
        # TODO: Check that everything went as expected
        # TODO: Disconnect from the database
        # TODO: Reply to the browser information that the tweet is liked
        return {"status": "ok"}
    except Exception as ex:
        ic(ex)
        return "error"
    finally:
        pass




