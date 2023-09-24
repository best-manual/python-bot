from flask import Blueprint

# Создаем объект Blueprint
bp = Blueprint('my_routes', __name__)

@bp.route('/update_server', methods=['POST'])
def webhook():
    if request.method == 'POST':
        repo = git.Repo('python-bot')
        origin = repo.remotes.origin
        origin.pull()
        return 'Updated PythonAnywhere successfully', 200
    else:
        return 'Wrong event type', 400

@bp.route('/')
def hello_world():
    return 'Hello New World 5!'