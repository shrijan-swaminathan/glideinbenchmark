# SPDX-FileCopyrightText: 2023 Fermi Research Alliance, LLC
# SPDX-License-Identifier: Apache-2.0

"""
This App allows to view and access benchmarks' results
"""
from flask import *
from output_plot_creation import create_histogram
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from io import BytesIO
import base64
from job_log_parsing import *

app = Flask(__name__)
def histograms():
    figs, fig_links = create_histogram()
    encoded_imgs = []
    for i, (fig, csv_link) in enumerate(zip(figs, fig_links)):
        canvas = FigureCanvas(fig)
        output = BytesIO()
        canvas.print_png(output)
        encoded_img = base64.b64encode(output.getvalue()).decode('ascii')
        session[f'file{i}'] = csv_link
        download_link = url_for('download_file_hist', filename=f'file{i}')
        # download_link = url_for('download_file', filename=csv_link)
        encoded_imgs.append((encoded_img, download_link))
    return render_template('viewer_histograms.html', encoded_imgs=encoded_imgs)

def download_file(filename):
    file_path = session.get(filename)
    directory, file_name = os.path.split(file_path) 
    # return send_file(session.get(filename), as_attachment=True, attachment_filename=f'{csv_name}.csv')
    return send_from_directory(directory, file_name, as_attachment=True)

def viewer_index():
    return render_template('viewer.html')