from flask import Flask
from routes import bp  # Импортируем Blueprint из routes.py
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

# Регистрируем Blueprint в приложении
app.register_blueprint(bp)

if __name__ == '__main__':
    app.run()

