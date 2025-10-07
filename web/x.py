from flask import request, make_response, render_template
import mysql.connector
import re
from functools import wraps
 
import os
 
from icecream import ic
ic.configureOutput(prefix=f'----- | ', includeContext=True)
 
UPLOAD_ITEM_FOLDER = './images'
 
##############################
def db():
    try:
        host = "fullweb.mysql.eu.pythonanywhere-services.com" if "PYTHONANYWHERE_DOMAIN" in os.environ else "mysql"
        password = "MyPasswordForYou" if "PYTHONANYWHERE_DOMAIN" in os.environ else "password"
       
        db = mysql.connector.connect(
            host = host,
            user = "root",  
            password = password,
            database = "twitter"
        )
        cursor = db.cursor(dictionary=True)
        return db, cursor
    except Exception as e:
        print(e, flush=True)
        raise Exception("Twitter exception - Database under maintenance", 500)
 
 
##############################
def no_cache(view):
    @wraps(view)
    def no_cache_view(*args, **kwargs):
        response = make_response(view(*args, **kwargs))
        response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
        response.headers["Pragma"] = "no-cache"
        response.headers["Expires"] = "0"
        return response
    return no_cache_view
 
 
##############################
REGEX_EMAIL = "^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$"
def validate_user_email():
    user_email = request.form.get("user_email", "").strip()
    if not re.match(REGEX_EMAIL, user_email): raise Exception("Invalid email", 400)
    return user_email
 
##############################
USER_USERNAME_MIN = 2
USER_USERNAME_MAX = 20
# REGEX_USER_USERNAME = f"^.{{{USER_USERNAME_MIN},{USER_USERNAME_MAX}}}$"
# TODO: The username can only be english letters 2 to 20 and contain 1 underscore
REGEX_USER_USERNAME = f"^(?!.*_.*_)[A-Za-z_]{{{USER_USERNAME_MIN},{USER_USERNAME_MAX}}}$"
 
 
def validate_user_username():
    user_username = request.form.get("user_username", "").strip()
    user_username = user_username.lower()
    error = f"username min {USER_USERNAME_MIN} max {USER_USERNAME_MAX} characters"
    if not re.match(REGEX_USER_USERNAME, user_username): raise Exception(error, 400)
    # if len(user_username) < USER_USERNAME_MIN: raise Exception(error, 400)
    # if len(user_username) > USER_USERNAME_MAX: raise Exception(error, 400)
    return user_username
 
##############################
USER_PASSWORD_MIN = 6
USER_PASSWORD_MAX = 50
REGEX_USER_PASSWORD = f"^.{{{USER_PASSWORD_MIN},{USER_PASSWORD_MAX}}}$"
def validate_user_password():
    user_password = request.form.get("user_password", "").strip()
    if not re.match(REGEX_USER_PASSWORD, user_password): raise Exception("Invalid password", 400)
    return user_password
 
 
 
##############################
USER_FIRST_NAME_MIN = 2
USER_FIRST_NAME_MAX = 20
def validate_user_first_name():
    user_first_name = request.form.get("user_first_name", "").strip()
    error = f"first name min {USER_FIRST_NAME_MIN} max {USER_FIRST_NAME_MAX} characters"
    if len(user_first_name) < USER_FIRST_NAME_MIN: raise Exception(error, 400)
    if len(user_first_name) > USER_FIRST_NAME_MAX: raise Exception(error, 400)
    return user_first_name
 
 
 
 
 
 
##############################
def validate_user_password_confirm():
    user_password = request.form.get("user_password_confirm", "").strip()
    if not re.match(REGEX_USER_PASSWORD, user_password): raise Exception("Twitter exception - Invalid confirm password", 400)
    return user_password
 
 
##############################
REGEX_UUID4 = "^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$"
def validate_uuid4(uuid4 = ""):
    if not uuid4:
        uuid4 = request.values.get("uuid4", "").strip()
    if not re.match(REGEX_UUID4, uuid4): raise Exception("Twitter exception - Invalid uuid4", 400)
    return uuid4
 