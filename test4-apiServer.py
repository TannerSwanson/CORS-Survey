# Test 4: Specific origins specified/allowed by API in CORS Headers, html/inline script origin is not one of them​. API is hosted on a different origin as the html and inline script.

from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=['http://127.0.0.1:5001', 'http://127.0.0.1:5002', 'http://127.0.0.1:5003'])

# API route, just returns some JSON message
@app.route('/data')
def data():
    return jsonify({'message': "If you see this message, then the script's API call did not violate the browser's CORS policy!"})

if __name__ == '__main__':
    # Start server on port 5001
    app.run(port=5001)
