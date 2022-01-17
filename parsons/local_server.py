import os
import sys
from threading import Timer
old_client_path = '/Users/tommyjoseph/desktop/okpy-work/ok-client'
show_cases_path = '/Users/Akshit/ok-client-tommy'
show_cases_path = '/Users/tommyjoseph/desktop/okpy-work/show-all-cases/ok-client'
prod_path = 'ok'
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), os.path.abspath(prod_path)))
# sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), os.path.abspath(show_cases_path)))
# in the future, ok-client modules will all be stored in single ok file 

import client.exceptions as ex
from client.sources.common import core
from client.api.assignment import load_assignment
from client.cli.common import messages
from output import DisableStdout 
from load import load_config, get_prob_names, path_to_name
from constants import *

from multiprocessing import Semaphore
import webbrowser
import logging
from datetime import datetime
import logging
import json
from flask import request, Flask, render_template, jsonify, redirect, url_for

log = logging.getLogger('client') # Get top-level logger

# done in Nate's init
read_semaphore = Semaphore(12)

# app = Flask(__name__, template_folder=f'templates', static_folder=f'static')
app = Flask(__name__)
cache = {}
names_to_paths = get_prob_names()
                
@app.route('/code_skeleton/<path:problem_name>')
def code_skeleton(problem_name):
    return parsons(problem_name, code_skeleton=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/code_arrangement/<path:problem_name>')
def parsons(problem_name, code_skeleton=False):
    problem_config = load_config(names_to_paths[problem_name])
    language = problem_config.get('language', 'python')

    code_lines = problem_config['code_lines'] + \
             '\nprint(\'DEBUG:\', !BLANK)' * 2 + '\n# !BLANK' * 2
    repr_fname = f'{PARSONS_FOLDER_PATH}/{names_to_paths[problem_name]}{PARSONS_REPR_SUFFIX}'
    if os.path.exists(repr_fname):
        with open(repr_fname, "r") as f:
            code_lines = f.read()

    cur_prob_index = list(names_to_paths.keys()).index(problem_name)
    not_last_prob = cur_prob_index < len(names_to_paths) - 1
    not_first_prob = cur_prob_index > 0
    return render_template('parsons.html',
                         problem_name=problem_name,
                         algorithm_description=problem_config[
                             'algorithm_description'],
                         problem_description=problem_config[
                             'problem_description'],
                         test_cases=problem_config['test_cases'],
                         # TODO(nweinman): Better UI for this (and comment
                         # lines as well)
                         code_lines=code_lines,
                         next_problem=None,
                         back_url=None,
                         code_skeleton=code_skeleton,
                         language=language,
                         not_first_prob=not_first_prob,
                         not_last_prob=not_last_prob
                         )

@app.route('/next_problem/<path:problem_name>', methods=['GET'])
def next_problem(problem_name):
    new_prob_name = list(names_to_paths.keys())[list(names_to_paths.keys()).index(problem_name) + 1]
    return redirect(url_for('code_skeleton', problem_name=new_prob_name))


@app.route('/prev_problem/<path:problem_name>', methods=['GET'])
def prev_problem(problem_name):
    new_prob_name = list(names_to_paths.keys())[list(names_to_paths.keys()).index(problem_name) - 1]
    return redirect(url_for('code_skeleton', problem_name=new_prob_name))

# also runs problems so students can verify correctness
@app.route('/get_problems/', methods=['GET'])
def get_problems():
    args = cache['args']

    with DisableStdout():
        assign = load_assignment(args.config, args)
    try:
        with open(PARSONS_CORRECTNESS, "r") as f:
            probs_correct = json.loads(f.read())
    except FileNotFoundError:
        probs_correct = {pname : False for pname in names_to_paths}
        with open(PARSONS_CORRECTNESS, "w") as f:
            f.write(json.dumps(probs_correct))
    req_names, req_paths = [], []
    opt_names, opt_paths = [], []
    # can assume proper structure since okpy checks for it
    assert assign.parsons != core.NoValue, "parsons param not found in .ok file"
    
    for pgroup_name, v in assign.parsons.items():
        req_lst = v.get('required', [])
        opt_lst = v.get('optional', [])
        for pname in req_lst: 
            req_names.append(f'{pname} {CHECK_MARK if probs_correct[pname] else RED_X}')
            req_paths.append(f'/code_skeleton/{pname}') 
        for pname in opt_lst: 
            opt_names.append(f'{pname} {CHECK_MARK if probs_correct[pname] else RED_X}')
            opt_paths.append(f'/code_skeleton/{pname}') 

    required = {'names': req_names, 'paths': req_paths} 
    optional = {'names': opt_names, 'paths': opt_paths}
    return {'required': required, 'optional': optional}
    # problem_paths = [f'/code_skeleton/{key}' for key in names_to_paths]
    # return { 'names': [f'{pname} {CHECK_MARK if probs_correct[pname] else RED_X}' for pname in names_to_paths], 'paths': problem_paths}

@app.route('/submit/', methods=['POST'])
def submit():
    problem_name = request.form['problem_name']
    submitted_code = request.form['submitted_code']
    parsons_repr_code = request.form['parsons_repr_code']
    write_parsons_prob_locally(problem_name, submitted_code, parsons_repr_code, True)
    test_results = grade_and_backup(problem_name)
    return jsonify({'test_results': test_results})

@app.route('/analytics_event', methods=['POST'])
def analytics_event():
    """
    {
        problem_name: string,
        event: 'start' | 'stop'
    }
    Triggered when user starts interacting with the problem and when they stop (e.g. switch tabs). 
    This data can be used to get compute analytics about time spent on parsons.
    """
    e, problem_name = request.json['event'], request.json['problem_name']
    msgs = messages.Messages()
    args = cache['args']
    args.question = [problem_name]
    with DisableStdout():
        assign = load_assignment(args.config, args)
    if e == 'start':
        msgs['action'] = 'start'
    elif e == 'stop':
        msgs['action'] = 'stop'

    msgs['problem'] = problem_name
    analytics_protocol = assign.protocol_map['analytics']
    backup_protocol = assign.protocol_map['backup']
    with DisableStdout():
        analytics_protocol.run(msgs)
        backup_protocol.run(msgs)

    msgs['timestamp'] = str(datetime.now())

    return jsonify({})

def write_parsons_prob_locally(prob_name, code, parsons_repr_code, write_repr_code):
    cur_line = -1
    in_docstring = False
    fname = f'{PARSONS_FOLDER_PATH}/{names_to_paths[prob_name]}.py'
    lines_so_far = []
    with open(fname, "r") as f:
        for i, line in enumerate(f):
            lines_so_far.append(line)
            if '"""' in line.strip():
                if in_docstring:
                    cur_line = i
                    break
                in_docstring = True

    assert cur_line >= 0, "Problem not found in file"

    code_lines = code.split("\n")
    code_lines.pop(0) # remove function def statement, is relied on elsewhere

    with open(fname, "w") as f:
        for line in lines_so_far:
            f.write(line)
        for line in code_lines:
            f.write(line + "\n")

    # write parsons repr code
    # used our own representation instead of Nate's most_recent_parsons()
    if write_repr_code:
        repr_fname = f'{PARSONS_FOLDER_PATH}/{names_to_paths[prob_name]}{PARSONS_REPR_SUFFIX}'
        with open(repr_fname, "w") as f:
            f.write(parsons_repr_code)

def store_correctness(prob_name, is_correct):
    try:
        with open(PARSONS_CORRECTNESS, "r") as f:
            probs_correct = json.loads(f.read())
    except OSError:
        probs_correct = {pname : False for pname in names_to_paths}
    probs_correct[prob_name] = is_correct

    with open(PARSONS_CORRECTNESS, "w") as f:
        f.write(json.dumps(probs_correct))
        
def grade_and_backup(problem_name):
    args = cache['args']
    args.question = [problem_name]
    msgs = messages.Messages()
    old_stdout = sys.stdout
    sys.stdout = out = open(PARSONS_OUTFILE, 'w')
    # remove syntax errors so assignment can load
    num_retries = len(names_to_paths)
    reloaded = []
    assign = None
    while num_retries > 0:
        try:
            assign = load_assignment(args.config, args)
            break
        except ex.LoadingException as e:
            # TODO: LoadingException unique with syntax error (vs missing .ok, for example)
            fname = str(e).split(" ")[-1]
            rel_path = fname.split("/")[1]
            prob_name = path_to_name(names_to_paths, rel_path[:-3])
            reloaded.append(prob_name)
            # replaces syntax-error code with error-free dummy code 
            write_parsons_prob_locally(prob_name, "def dummy():\n    print('Syntax Error')\n", None, False)
            num_retries -= 1
    assert num_retries > 0, "Rewriting '' to parsons files failed"

    for name, proto in assign.protocol_map.items():
        log.info('Execute {}.run()'.format(name))
        proto.run(msgs)
    out.close()
    sys.stdout = old_stdout
    msgs['timestamp'] = str(datetime.now())
    feedback = {}
    feedback['passed'] = assign.specified_tests[0].console.cases_passed
    feedback['failed'] = assign.specified_tests[0].console.cases_total - feedback['passed']

    # get output from doctests
    with open(PARSONS_OUTFILE, "r") as f:
        all_lines = f.readlines()
        # still need to fix ok-client show all cases to not print extra ------
        # feedback['doctest_logs'] = "".join(all_lines[3:-10])
        feedback['doctest_logs'] = "".join(all_lines[9:-10])
    
    store_correctness(problem_name, feedback['passed'] > 1 and feedback['failed'] == 0)
    return feedback

def open_browser():
    webbrowser.open_new(f'http://127.0.0.1:{PORT}/')

def open_in_browser(args):
    cache['args'] = args 
    # parsons folder must exist
    assert os.path.isdir(PARSONS_FOLDER_PATH), "parsons folder does not exist"
    Timer(1, open_browser).start()
    run_server(PORT)

def run_server(port):
    global PORT
    # disable flask logging
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)
    os.environ['WERKZEUG_RUN_MAIN'] = 'true'
    for port in range(PORT, PORT + 10):
        try:
            PORT = port
            print("Press Ctrl + C to kill the process.")
            app.run(port=port)
            exit(0)
        except OSError as e:
            print(f"Port {port} is currently in use, trying a different port...")
