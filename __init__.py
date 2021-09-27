from flask import Flask

UPLOAD_FOLDER = 'uploads'

app = Flask(__name__)
#app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379',
    RESULT_BACKEND='mongodb://localhost:27017'
)
