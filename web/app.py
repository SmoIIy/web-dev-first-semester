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
@app.get("/signup")
def view_signup():
    return render_template("signup.html")

##############################
@app.get("/login")
def view_login():
    return render_template("login.html")

##############################
@app.post("/login")
def handle_login():
    try:
        user_email = x.validate_user_email()
        user_password = x.validate_user_password()
        ic(user_email, " ", user_password)
        db, cursor = x.db()
        q = "SELECT * FROM users WHERE user_email = %s and user_password = %s"
        cursor.execute(q, (user_email, user_password))
        user = cursor.fetchone()
        if not user: raise Exception("user not found", 400)
        session["user"] = user
        return redirect(url_for("view_home"))
    except Exception as ex:
        ic(ex)
        if ex.args[1] == 400: return ex.args[0]
        return "System under maintenance", 500
    finally:
        if "cursor" in locals(): cursor.close()
        if "db" in locals(): db.close()


##############################
@app.get("/home")
@x.no_cache
def view_home():
    user = session.get("user", "")
    if not user: return redirect(url_for("view_login"))
    return render_template("home.html", user=user)


##############################
@app.get("/logout")
def view_logout():
    session.clear()
    return redirect(url_for("view_login"))

##############################
@app.post("/signup")
def handle_signup():
    try:
        # Validate user name
        user_name = request.form.get("user_name", "").strip()
        x.validate_user_name(user_name)
        user_first_name = request.form.get("user_first_name", "").strip()
        user_email = request.form.get("user_email", "").strip()
        x.validate_user_first_name(user_first_name)
        user_email = x.validate_user_email()
        db, cursor = x.db()
        user_password = request.form.get("user_password", "").strip()
        hashed_password = x.hash_password(user_password)
        db.start_transaction()
        q = "INSERT INTO users VALUES(null, %s, %s, %s, %s)"
        cursor.execute(q, (user_name, user_first_name, user_email, hashed_password))
        inserted_rows = cursor.rowcount
        db.commit()
        return f"Total rows inserted: {inserted_rows}"
    except Exception as ex:
        ic(ex)
        if "db" in locals(): db.rollback()

        if "twitter exception - user name too short" in str(ex):
            return "name too short", 400

        if "twitter exception - user name too long" in str(ex):
            return "name too long", 400

        if "twitter exception - user first name too short" in str(ex):
            return "first name too short", 400

        if "twitter exception - user first name too long" in str(ex):
            return "first name too long", 400

        if "Twitter exception - Invalid email" in str(ex):
            return "Invalid email", 400

        if "Duplicate entry" and user_name in str(ex):
            return "username already registered", 400
        
        if "Duplicate entry" and user_email in str(ex):
            return "email already registered", 400   

        return "System under maintainance", 500
    finally:
        if "cursor" in locals(): cursor.close()
        if "db" in locals(): db.close()





















