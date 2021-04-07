from flask import Flask, json, jsonify, request
from flask_cors import CORS
from database import dataB

app = Flask(__name__)
CORS(app)
myB = dataB()
myB.create({"label": "confidence"})

@app.route('/create/<key>/<value>', methods=["POST"])
def create(key, value):
    return myB.create({key: value})


@app.route('/read/<key>', methods=["GET"])
def read(key):
    return myB.read(key)


@app.route('/update/<id>/<key>/<value>', methods=["GET", "POST"])
def update(id, key, value):
    return myB.update(id, {key: value})


@app.route('/delete/<key>', methods=["DELETE"])
def delete(key):
    return myB.delete(key)


@app.route('/upload', methods=["POST"])
def upload():
    return myB.upload()


@app.route('/download', methods=["POST"])
def download():
    return myB.download()


if __name__ == "__main__":
    # run backend server on http://localhost:5000/
    app.run(host='localhost', port=5000, debug=True)
