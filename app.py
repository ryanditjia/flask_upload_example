from flask import Flask, request
from flask_cors import CORS
from werkzeug.utils import secure_filename
from pathlib import Path

app = Flask(__name__)
CORS(app)


@app.route('/melody_processing', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['filepond']
        uploads_dir = f"{Path.cwd()}/uploads/{secure_filename(f.filename)}"
        f.save(uploads_dir)
        return 'file uploaded successfully'
