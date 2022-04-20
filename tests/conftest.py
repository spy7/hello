from os.path import dirname as d
from os.path import abspath
import sys

root_dir = d(d(abspath(__file__)))
sys.path.append(root_dir)
