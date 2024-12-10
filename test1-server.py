# Test 1: No CORS Headers in the API response. API is hosted on the same origin as the html and inline script.

from flask import Flask, render_template_string, jsonify
# Do not include CORS Headers
# from flask_cors import CORS

app = Flask(__name__)
# Do not include CORS Headers
# CORS(app)

# Route serving html with inline javascript, allows GET by default
@app.route('/')
def index():
    # html with inline javascript making API request upon button press
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>CORS Demonstration Test 1</title>
    </head>
    <body>
        <h1>Testing Same-Origin API Call</h1>
        <button id="makeRequest">Make API Request</button>

        <script>
            document.getElementById('makeRequest').onclick = function() {
                fetch('http://127.0.0.1:5000/data', {
                    method: 'GET',
                    mode: 'cors'
                })
                .then(response => response.json())
                .then(data => {
                    console.log('Successful call:', data);
                })
                .catch(error => {
                    console.error('CORS error:', error);
                });
            };
        </script>
    </body>
    </html>
    """
    return render_template_string(html_content)

# API route, just returns some JSON message
@app.route('/data')
def data():
    return jsonify({'message': "If you see this message, then the script's API call did not violate the browser's CORS policy!"})

if __name__ == '__main__':
    # Start server on port 5000
    app.run(port=5000)
