from flask import Flask
app = Flask(__name__)
# ! session key is Required
app.secret_key = 'Trust the Processes'
DATABASE = "users"