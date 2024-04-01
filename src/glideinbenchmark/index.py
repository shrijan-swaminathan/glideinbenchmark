from flask import Flask, render_template, redirect, url_for
from runner import runner_config
from viewer import histograms

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/viewer')
def viewer():
    return render_template('viewer.html')

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
    app.run()