# SPDX-FileCopyrightText: 2023 Fermi Research Alliance, LLC
# SPDX-License-Identifier: Apache-2.0

"""
This App allows to view and access benchmarks' results
"""
from flask import Flask, render_template, redirect, url_for
from output_plot_creation import create_histogram
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from io import BytesIO
import base64
from job_log_parsing import *

app = Flask(__name__)
# look under /var/log/gwms-factory/client/ directory tree by default recursively
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

def viewer_index():
    
    return render_template('viewer.html')