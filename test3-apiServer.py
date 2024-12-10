# Test 3: Fully permissive CORS Headers (*) sent in the API response. API is hosted on a different origin as the html and inline script.

from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# API route, just returns some JSON message
@app.route('/data')
def data():
    return jsonify({'message': "If you see this message, then the script's API call did not violate the browser's CORS policy!"})

if __name__ == '__main__':
    # Start server on port 5001
    app.run(port=5001)