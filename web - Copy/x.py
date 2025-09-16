from flask import request
import mysql.connector
import hashlib

from icecream import ic
ic.configureOutput(prefix=f'***** | ', includeContext=True)



##############################
def db():
    db = mysql.connector.connect(
        host = "mysql",      # Replace with your MySQL server's address or docker service name "mysql"
        user = "root",  # Replace with your MySQL username
        password = "password",  # Replace with your MySQL password
        database = "company"   # Replace with your MySQL database name
    )
    cursor = db.cursor(dictionary=True)
    return db, cursor


##############################
##############################
def hash_password(password):
    # Create a sha256 hash object
    sha256_hash = hashlib.sha256()
    # Update the hash object with the password (encoded as bytes)
    sha256_hash.update(password.encode('utf-8'))
    # Return the hexadecimal representation of the hash
    return sha256_hash.hexdigest()