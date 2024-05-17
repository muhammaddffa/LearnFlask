from app import app
from flask import request
from app.controller import DosenController



@app.route('/')
def index():
    return 'Hello Flask'


@app.route('/dosen', methods=['GET', 'POST'])
def dosens():
    if request.method == 'GET':
        return DosenController.getDosen()
    else:
        return DosenController.createDataDosen() 

@app.route('/dosen/<id>', methods=['GET'])
def dosensDetail(id):
    return DosenController.detail(id)


