from flask import Flask

from infrastructure.application.blueprints.main import main

app = Flask(__name__)
app.register_blueprint(main)
