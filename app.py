import os
from flask import Flask, render_template

# Initialize Flask app, pointing to the current directory for templates
app = Flask(__name__, template_folder='.')

@app.route('/')
def home():
    # Renders the index.html file located in the same directory
    return render_template('index.html')

if __name__ == '__main__':
    # Bind to PORT environment variable (required by cloud providers) or default to 5000
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
