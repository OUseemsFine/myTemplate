from flask import Flask, render_template, send_from_directory

app = Flask(__name__, static_folder='.', template_folder='.')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/')
def home1():
    return render_template('index2.html')

@app.route('/<path:filename>')
def send_file(filename):
    return send_from_directory('.', filename)

if __name__ == '__main__':
    app.run(debug=True)