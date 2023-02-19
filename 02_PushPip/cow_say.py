import argparse
from cowsay import cowsay, list_cows

parser = argparse.ArgumentParser()
parser.add_argument('-e', type=str)
parser.add_argument('-T', type=str)
parser.add_argument('message', type=str)
args = parser.parse_args()

params = {}
if args.e is not None:
    params['eyes'] = args.e[:2]
if args.e is not None:
    params['tongue'] = args.T[:2]

params['message'] = args.message
print(cowsay(**params))