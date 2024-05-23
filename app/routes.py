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

@app.route('/dosen/<id>', methods=['GET', 'PUT', 'DELETE'])
def dosensDetail(id):
    if request.method == 'GET':
        return DosenController.detail(id)
    elif request.method == 'PUT':
        return DosenController.updateDataDosen(id)
    elif request.method == 'DELETE':
        return DosenController.deleteDataDosen(id)


