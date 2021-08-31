from urllib import request

from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/lugar', methods=['GET'])
def lugar():
    return 'Santander'


if __name__ == '__main__':
    app.run(debug=True)
