import os
import sys
from threading import Timer
from typing import List

from output import DisableStdout
from load import load_config, path_to_name, problem_name_from_file
from constants import *

from multiprocessing import Semaphore
import webbrowser
import logging
from datetime import datetime
import logging
import json
import re
from flask import Response, request, Flask, render_template, jsonify, redirect, url_for, send_file

log = logging.getLogger('client') # Get top-level logger

# serialize grading and analytics to avoid undesired logs in stdout due to
# interleaving of multiple analytics events or grading and analytics
sema = Semaphore(1)

app = Flask(__name__)
cache = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/problem/<path:problem_name>')
def parsons(problem_name):
    return render_template('parsons.html', problem_name=problem_name)

def open_browser():
    webbrowser.open_new(f'http://127.0.0.1:{PORT}/problem/add_in_range')

def open_in_browser():
    # parsons folder must exist
    assert os.path.isdir(PARSONS_FOLDER_PATH), "parsons folder does not exist"
    Timer(1, open_browser).start()
    run_server(PORT)

def run_server(port):
    global PORT
    # disable flask logging
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)
    for port in range(PORT, PORT + 10):
        try:
            PORT = port
            print("Press Ctrl + C to kill the process.")
            app.run(port=port)
            exit(0)
        except OSError as e:
            print(e)
            print(f"Port {port} is currently in use, trying a different port...")
