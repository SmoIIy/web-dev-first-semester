from flask import request, make_response, render_template
import mysql.connector
import hashlib
import re 
from functools import wraps
 
from icecream import ic
ic.configureOutput(prefix=f'----- | ', includeContext=True)

UPLOAD_ITEM_FOLDER = './images'

##############################
def db():
    try:
        db = mysql.connector.connect(
            host = "mariadb",
            user = "root",  
            password = "password",
            database = "twitter"
        )
        cursor = db.cursor(dictionary=True)
        return db, cursor
    except Exception as e:
        print(e, flush=True)
        raise Exception("Twitter exception - Database under maintenance", 500)


##############################
USER_NAME_MIN = 2
USER_NAME_MAX = 20
def validate_user_name(user_name):
    if len(user_name) < USER_NAME_MIN: 
        raise Exception("twitter exception - user name too short")
    if len(user_name) > USER_NAME_MAX:
        raise Exception("twitter exception - user name too long")
    return True

##############################
USER_FIRST_NAME_MIN = 2
USER_FIRST_NAME_MAX = 20
def validate_user_first_name(user_first_name):
    if len(user_first_name) < USER_FIRST_NAME_MIN: 
        raise Exception("twitter exception - user first name too short")
    if len(user_first_name) > USER_FIRST_NAME_MAX:
        raise Exception("twitter exception - user first name too long")
    return True

##############################
def hash_password(password):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(password.encode('utf-8'))
    return sha256_hash.hexdigest()


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
USER_PASSWORD_MIN = 6
USER_PASSWORD_MAX = 50
REGEX_USER_PASSWORD = f"^.{{{USER_PASSWORD_MIN},{USER_PASSWORD_MAX}}}$"
def validate_user_password():
    user_password = request.form.get("user_password", "").strip()
    if not re.match(REGEX_USER_PASSWORD, user_password): raise Exception("Invalid password", 400)
    return user_password


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


