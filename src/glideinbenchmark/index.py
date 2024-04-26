from flask import Flask, render_template
from runner import *
from viewer import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/viewer')
def viewer():
    return viewer_index()

@app.route('/viewer/histograms')
def plot_histograms():
    return histograms()

@app.route('/runner')
def runner():
    return render_template('runner.html')

@app.route('/runner/config', methods=["GET", "POST"])
def runner_config_route():
    return runner_config()

if __name__ == '__main__':
    app.run(host='0.0.0.0')