from flask import Flask, render_template, redirect, url_for
from runner_config import runner_config
from output_plot_creation import create_histogram
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from io import BytesIO
import base64

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/viewer')
def viewer():
    return render_template('viewer.html')

@app.route('/viewer/histograms')
def histograms():
    figs = create_histogram()
    encoded_imgs = []
    for fig in figs:
        canvas = FigureCanvas(fig)
        output = BytesIO()
        canvas.print_png(output)
        encoded_img = base64.b64encode(output.getvalue()).decode('ascii')
        encoded_imgs.append(encoded_img)
    return render_template('viewer_histograms.html', encoded_imgs=encoded_imgs)


@app.route('/runner')
def runner():
    return render_template('runner.html')

@app.route('/runner/config', methods=["GET", "POST"])
def runner_config_route():
    return runner_config()

if __name__ == '__main__':
    app.run()