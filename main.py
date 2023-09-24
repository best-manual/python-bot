from flask import Flask, json, request
from routes import bp  # Импортируем Blueprint из routes.py
import logging
import git

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

# Регистрируем Blueprint в приложении
app.register_blueprint(bp)

if __name__ == '__main__':
    app.run()

