from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import redis
import random
import string
import os

app = Flask(__name__)

load_dotenv('.env.dev')
r = redis.Redis(host=os.getenv('HOST'), port=os.getenv('PORT'), decode_responses=True)

CORS(app, origins=['http://localhost:8080', 'http://localhost:8080/url'], allow_headers=["Content-Type", "Authorization", "Access-Control-Allow-Credentials"],
supports_credentials=True)

@app.route('/url', methods=['POST'])
def create_url():
    characters = string.ascii_letters + string.digits
    url_original = request.json['urlOriginal']
    r.set(url_original, ''.join(random.choice(characters) for i in range(15)))
    url_acortada = { 'urlAcortada': r.get(url_original) }
    return jsonify(url_acortada)

@app.route('/urls', methods=['GET'])
def get_urls():
    urls  = list(map(lambda key: { key: r.get(key) }, r.keys()))
    return jsonify(urls)

# Hay que quitar 'https://' para hacer la solicitud, sino no funcionará.
@app.route('/url/<url_original>', methods=['GET'])
def get_url(url_original):
    url_original = 'https://' + url_original
    print(url_original)
    url_acortada = r.get(url_original)
    return url_acortada

# Hay que quitar 'https://' para hacer la solicitud, sino no funcionará.
@app.route('/url/<url_original>', methods=['DELETE'])
def delete_url(url_original):
    url_original = 'https://' + url_original
    r.delete(url_original)
    return 'Success'

if __name__ == "__main__":
    app.run(debug=True)