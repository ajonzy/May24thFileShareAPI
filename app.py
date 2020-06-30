from flask import Flask, request, jsonify, send_file
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_heroku import Heroku
import io

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = ""

db = SQLAlchemy(app)
ma = Marshmallow(app)

heroku = Heroku(app)
CORS(app)


class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    file_type = db.Column(db.String(), nullable=False)
    data = db.Column(db.LargeBinary, nullable=False)

    def __init__(self, name, file_type, data):
        self.name = name
        self.file_type = file_type
        self.data = data

class FileSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "file_type")

file_schema = FileSchema()
files_schema = FileSchema(many=True)


if __name__ == "__main__":
    app.run(debug=True)