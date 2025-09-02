from flask import request
import mysql.connector

from icecream import ic
ic.configureOutput(prefix=f'***** | ', includeContext=True)


##############################
def db():
    host = "mysql"
    database = ""
    db = mysql.connector.connect(
        host = host,      # Replace with your MySQL server's address or docker service name "mysql"
        user = "",  # Replace with your MySQL username
        password = "",  # Replace with your MySQL password
        database = database   # Replace with your MySQL database name
    )
    cursor = db.cursor(dictionary=True)
    return db, cursor


##############################
