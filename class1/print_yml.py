import yaml
import sys
from pprint import pprint

filename = str(sys.argv[1])

def read_yaml(filename):
    with open(filename) as f:
        return yaml.load(f)

pprint(read_yaml(filename))
