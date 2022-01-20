from constants import PROBLEM_PATHS, UTILITY_FILES, PARSONS_GLOB, PARSONS_FOLDER_PATH 
import yaml
from collections import defaultdict, OrderedDict
import glob
import os

def load_config_file(paths):
  """
  Loads a YAML file.
  Args:
      path: A path to a YAML file.

  Returns: The contents of the YAML file as a defaultdict, returning None
      for unspecified attributes.

  """
  if type(paths) != list:
    paths = [paths]
  for path in paths:
    try:
      with open(os.path.abspath(path), 'r') as file:
        config = yaml.load(file, Loader=yaml.Loader)
      if type(config) == dict:
        config = defaultdict(lambda: None, config)
      return config
    except IOError as e:
      pass
  raise Exception("Cannot find files {0}".format(paths))

def load_config(file_name):
  """
  Loads a YAML file, assuming that the YAML file is located in the problems/PROBLEM_NAME.yaml directory.
  Args:
      file_name: The name of the directory in the data directory.
      root_path: Optional argument that specifies the root_path for problems.

  Returns: The contents of the YAML file as a defaultdict, returning None
      for unspecified attributes.
  """
  config_files = []
  for path in PROBLEM_PATHS:
    config_files.append(os.path.join(os.path.abspath(path), file_name + ".yaml"))
  return load_config_file(config_files)

def get_prob_names():
  """
  Returns a map from problem name to problem path for each parsons problem,
  assuming that the problem name is the function name in the parsons file.
  """
  names_to_paths = OrderedDict()
  for name in glob.glob(PARSONS_GLOB):
      if name not in UTILITY_FILES:
          fname = name[len(PARSONS_FOLDER_PATH) - 1:-3]
          with open(name, "r") as f:
              cur_lines = f.readlines()
              for line in cur_lines:
                  cur_words = line.lstrip().split()
                  if cur_words and cur_words[0] == 'def':
                      func_sig = cur_words[1]
                      names_to_paths[func_sig[:func_sig.index('(')]] = fname 
                      break
  return names_to_paths


def path_to_name(names_to_paths, path):
    for key, val in names_to_paths.items():
        if val == path:
            return key
