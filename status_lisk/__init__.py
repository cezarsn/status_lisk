from flask import  Flask, render_template
import requests

app = Flask(__name__)

import models
import views
import controllers


if __name__ == "__main__":
    app.run()
