# Test 5: Specific origins specified/allowed by API in CORS Headers, html/inline script origin is one of them​. API is hosted on a different origin as the html and inline script​.

from flask import Flask, render_template_string

app = Flask(__name__)

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
        <title>CORS Demonstration Test 5</title>
    </head>
    <body>
        <h1>Testing Different-Origin API Call</h1>
        <button id="makeRequest">Make API Request</button>

        <script>
            document.getElementById('makeRequest').onclick = function() {
                fetch('http://127.0.0.1:5001/data', {
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

if __name__ == '__main__':
    # Start server on port 5000
    app.run(port=5000)
