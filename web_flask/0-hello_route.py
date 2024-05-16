 #!/usr/bin/python3
"""Starts a flask application."""
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    """Serves the get request to the url /"""
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host="0.0.0.0")