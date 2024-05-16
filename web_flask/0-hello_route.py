 #!/usr/bin/python3
from flask import Flask
"""Starts a flask application."""

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    """Serves the get request to the url /"""
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run()