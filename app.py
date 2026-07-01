from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

# after I set my app variable...
app.debug = True
toolbar = DebugToolbarExtension(app)