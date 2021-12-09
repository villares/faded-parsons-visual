import sys
import os
from local_server import open_in_browser

# in the future, ok-client modules will all be stored in single ok file 
# old_client_path = '/Users/tommyjoseph/desktop/okpy-work/ok-client'
# show_cases_path = '/Users/tommyjoseph/desktop/okpy-work/show-all-cases/ok-client'
# sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), os.path.abspath(show_cases_path)))


from client.utils import auth 
from client.cli.ok import parse_input
args = parse_input()
args.fpp = True
if not auth.authenticate(args):
    exit(1)
open_in_browser(args)