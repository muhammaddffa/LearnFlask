from app.model.dosen import Dosen
from app.model.mahasiswa import Mahasiswa

from app import response, app, db
from flask import request

def getDosen():
    try:
        dosen = Dosen.query.all()
        data = formatarray(dosen)
        return response.success(data,"Success get data Dosen")
    except Exception as e:
        print(e)


def formatarray(datas):
    array = []

    for i in datas:
        array.append(singleObject(i))

    return array


def singleObject(data):
    data = {
        'id': data.id,
        'nidn': data.nidn,
        'name': data.name,
        'phone': data.phone,
        'address': data.address
    }

    return data

def detail(id):
    try:
        dosen = Dosen.query.filter_by(id=id).first()
        mahasiswa = Mahasiswa.query.filter((Mahasiswa.dosen_satu == id) | (Mahasiswa.dosen_dua == id))

        if not dosen:
            return response.badRequest([], 'do not data dosen')

        datamahasiswa = formatMahasiswa(mahasiswa)

        data = singleDetailMahasiswa(dosen,datamahasiswa)

        return response.success(data,'Success get data dosen')

    except Exception as e:
        print(e)


def singleDetailMahasiswa(dosen, mahasiswa):
    data = {
        'id': dosen.id,
        'nidn': dosen.nidn,
        'name': dosen.name,
        'phone': dosen.phone,
        'mahasiswa': mahasiswa
    }

    return data


def singleMahasiswa(mahasiswa):
    data = {
        'id': mahasiswa.id,
        'nim': mahasiswa.nim,
        'name': mahasiswa.name,
        'phone': mahasiswa.phone
    }

    return data

def formatMahasiswa(data):
    array = []
    for i in data:
        array.append(singleMahasiswa(i))
    return array


# Tujuannya untuk menampung data Dosen untuk di Post di db
def createDataDosen():
    try:
        nidn = request.form.get("nidn")
        name = request.form.get("name")
        phone = request.form.get("phone")
        address = request.form.get("address")

        dosens = Dosen(nidn=nidn, name=name, phone=phone, address=address)
        db.session.add(dosens)
        db.session.commit()

        return response.success('201','Succes post data Dosen')
    except Exception as e:
        print(e)


# Update Data
def updateDataDosen(id):
    try:
        nidn = request.form.get('nidn')
        name = request.form.get('name')
        phone = request.form.get('phone')
        address = request.form.get('address')

        input = [
            {
                "nidn": nidn,
                "name": name,
                "phone": phone,
                "address": address
            }
        ]

        dosen = Dosen.query.filter_by(id=id).first()

        dosen.nidn = nidn
        dosen.name = name
        dosen.phone = phone
        dosen.address = address

        db.session.commit()

        return response.success(input,'Success update data dosen')
    except Exception as e:
        print(e)

#Delete Data
def deleteDataDosen(id):
    try:
        dosen = Dosen.query.filter_by(id=id).first()

        if not dosen:
            return response.badRequest([], 'Do not Data Dosen...')
        
        db.session.delete(dosen)
        db.session.commit()

        return response.success('', 'Success Delete Data!')
    except Exception as e:
        print(e)
    