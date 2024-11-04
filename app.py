from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import redis
import random
import string
import os

load_dotenv('.env.prod')

app = Flask(__name__)

r = redis.Redis(host=os.getenv("DB_HOST"), port=os.getenv("DB_PORT"), decode_responses=True)

CORS(app, resources={r'/*': {'origins': [os.getenv("FRONTEND_URL_DEV"), os.getenv("FRONTEND_URL"), os.getenv("FRONTEND_URL_PROD")]}})


@app.route('/url', methods=['POST'])
def create_url():
    characters = string.ascii_letters + string.digits
    url_original = request.json['urlOriginal']

    for key in r.scan_iter():
        if r.get(key) == url_original:
            return jsonify(key)
        
    url_acortada = ''.join(random.choice(characters) for i in range(15))
    r.set(url_acortada, url_original)
    return jsonify(url_acortada)


@app.route('/urls', methods=['GET'])
def get_urls():
    urls = list(map(lambda key: {key: r.get(key)}, r.keys()))
    return jsonify(urls)


@app.route('/url/<url_acortada>', methods=['GET'])
def get_url(url_acortada):
    url_original = r.get(url_acortada)
    return jsonify(url_original)


@app.route('/url/<url_acortada>', methods=['DELETE'])
def delete_url(url_acortada):
    if r.exists(url_acortada):
        r.delete(url_acortada)
        return 'Success'
    else:
        return 'Not found'


if __name__ == '__main__':
    app.run(debug=True)
