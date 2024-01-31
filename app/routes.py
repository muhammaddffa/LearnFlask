from app import app
from app.controller import DosenController



@app.route('/')
def index():
    return 'Hello Flask'


@app.route('/dosen', methods=['GET'])
def dosens():
    return DosenController.index()


@app.route('/dosen/<id>', methods=['GET'])
def dosensDetail(id):
    return DosenController.detail(id)

